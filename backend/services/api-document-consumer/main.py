import asyncio
import json
import logging
import pulsar
import asyncpg
from pulsar import ConsumerType

# Configuración básica de Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --- CONFIGURACIÓN ---
PULSAR_SERVICE_URL = 'pulsar://localhost:6650'
TOPIC_NAME = 'persistent://public/default/outbox.event.pedido'
SUBSCRIPTION_NAME = 'worker-servicio-envios'
DATABASE_URL = 'postgresql://user:password@localhost:5432/mi_db'

async def ejecutar_logica_negocio(event_payload, db_conn):
    """
    Aquí va tu lógica real: actualizar inventario, crear envío, etc.
    Se ejecuta dentro de la transacción de la DB.
    """
    logger.info(f"Ejecutando lógica para: {event_payload.get('aggregate_id')}")
    # Ejemplo:
    # await db_conn.execute("UPDATE inventario SET stock = stock - 1 WHERE prod_id = $1", ...)
    await asyncio.sleep(0.5) # Simulación de I/O

async def procesar_mensaje(msg, consumer, db_pool):
    """
    Consumidor con patrón de idempotencia (Check-and-Process).
    """
    try:
        # 1. Parsear el mensaje de Debezium
        raw_data = msg.data().decode('utf-8')
        event_data = json.loads(raw_data)
        
        # Debezium Outbox Router pone el ID en el payload
        event_id = event_data.get('id') 
        
        if not event_id:
            logger.warning("Mensaje recibido sin ID de evento. Ignorando.")
            consumer.acknowledge(msg)
            return

        # 2. Operación Atómica en la DB
        async with db_pool.acquire() as conn:
            async with conn.transaction():
                # Intentar insertar en la tabla de control
                # Si el ID ya existe, 'result' será None gracias al ON CONFLICT DO NOTHING
                result = await conn.execute(
                    """
                    INSERT INTO processed_events (event_id, status) 
                    VALUES ($1, 'SUCCESS') 
                    ON CONFLICT (event_id) DO NOTHING
                    """, 
                    event_id
                )

                if result == "INSERT 0 0":
                    logger.info(f"Evento {event_id} ya procesado anteriormente. Saltando...")
                else:
                    # 3. Solo si no estaba procesado, ejecutamos la lógica
                    await ejecutar_logica_negocio(event_data, conn)
                    logger.info(f"Evento {event_id} procesado exitosamente.")

        # 4. Confirmar a Pulsar (ACK) solo si la transacción de la DB terminó bien
        consumer.acknowledge(msg)

    except Exception as e:
        logger.error(f"Error procesando mensaje: {e}")
        # Si algo falló, informamos a Pulsar para que lo reintente luego
        consumer.negative_acknowledge(msg)

async def main():
    # Inicializar Pool de Base de Datos
    db_pool = await asyncpg.create_pool(DATABASE_URL)
    
    # Inicializar Cliente Pulsar
    client = pulsar.Client(PULSAR_SERVICE_URL)
    
    # Crear Consumidor tipo Shared (para escalar en múltiples Pods)
    consumer = client.subscribe(
        topic=TOPIC_NAME,
        subscription_name=SUBSCRIPTION_NAME,
        consumer_type=ConsumerType.Shared,
        initial_position=pulsar.InitialPosition.Earliest,
        receiver_queue_size=100  # Evita que un solo Pod acapare demasiados mensajes
    )

    logger.info(f"Worker iniciado. Escuchando {TOPIC_NAME}...")

    try:
        while True:
            # Esperar mensaje de forma asíncrona (no bloquea el loop)
            msg = await consumer.receive_async()
            
            # Lanzar el procesamiento como una tarea independiente
            # Esto permite procesar múltiples mensajes en paralelo en el mismo Pod
            asyncio.create_task(procesar_mensaje(msg, consumer, db_pool))
            
    except asyncio.CancelledError:
        logger.info("Cerrando worker...")
    finally:
        await db_pool.close()
        client.close()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass