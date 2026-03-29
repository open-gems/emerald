#!/bin/bash

docker cp ./services/api-document/infrastructure/debezium/config.yaml broker:/tmp/config.yaml
docker cp ./z/dev/pulsar/connectors/pulsar-io-debezium-postgres-4.1.3.nar broker:/tmp/debezium.nar

docker exec -it broker bin/pulsar-admin source localrun \
  --archive /tmp/debezium.nar \
  --source-config-file /tmp/config.yaml