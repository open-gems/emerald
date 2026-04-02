<template>
  <PageSplit initialWidth="65%">
    <template #left>
      <MarkdownEditor :initialContent="htmlListo" />
    </template>
    <template #right>
      <Preview />
    </template>
  </PageSplit>
</template>

<script setup>
import { ref, onMounted } from "vue";

const htmlListo = ref(`
<div class="page-virtual" data-number="1" data-type="page" id="page-1">
<p>Contenido</p>
<ul>
<li><p>TÍTULO 1........................................................................................................................... 7 DISPOSICIONES GENERALES........................................................................................ 7</p><ul>
<li><p>CAPÍTULO 1.................................................................................................................. 7 Objeto, ámbito de aplicación y definiciones.................................................................... 7</p></li>
<li><p>CAPÍTULO 2.................................................................................................................. 7 Planeación de la función archivística ............................................................................. 7</p></li>
<li><p>CAPÍTULO 3................................................................................................................ 10 Responsabilidad con los documentos y archivos ......................................................... 10</p></li>
<li><p>CAPÍTULO 4................................................................................................................ 11 Inspección, Vigilancia y Control ................................................................................... 11</p></li>
</ul>
</li>
<li><p>TÍTULO 2......................................................................................................................... 12 ÓRGANOS ASESORES, COORDINADORES Y EJECUTORES DEL SISTEMA NACIONAL DE ARCHIVOS............................................................................................. 12</p><ul>
<li><p>CAPÍTULO 1................................................................................................................ 13 Comité Evaluador de Documentos............................................................................... 13</p></li>
<li><p>CAPÍTULO 2................................................................................................................ 15 Archivos Generales Territoriales y Consejos Territoriales de Archivo .......................... 15</p></li>
<li><p>CAPÍTULO 3................................................................................................................ 18 Comités Internos de Archivo........................................................................................ 18</p></li>
</ul>
</li>
<li><p>TÍTULO 3......................................................................................................................... 18 ADMINISTRACIÓN DE ARCHIVOS ................................................................................ 18</p><ul>
<li><p>CAPÍTULO 1................................................................................................................ 19 Requisitos para la administración de archivos.............................................................. 19</p></li>
<li><p>CAPÍTULO 2................................................................................................................ 23 Lineamientos generales para la prestación de servicios archivísticos.......................... 23</p></li>
</ul>
</li>
<li><p>TÍTULO 4......................................................................................................................... 23 GESTIÓN DE DOCUMENTOS ........................................................................................ 23</p></li>
</ul>
<ul>
<li><p>CAPÍTULO 1................................................................................................................ 24 Planeación y Producción documental .......................................................................... 24</p></li>
<li><p>CAPÍTULO 2................................................................................................................ 25 Gestión y trámite de los documentos ........................................................................... 25</p></li>
<li><p>CAPÍTULO 3................................................................................................................ 29 Principios y criterios para el proceso de organización documental............................... 29</p><ul>
<li><p>SECCIÓN 1............................................................................................ 29 Organización de archivos: clasificación, ordenación y descripción .................... 29</p></li>
<li><p>SECCIÓN 2............................................................................................ 33 Expediente electrónico ............................................................................. 33</p></li>
<li><p>SECCIÓN 3............................................................................................ 35 Expediente híbrido................................................................................... 35</p></li>
</ul>
</li>
<li><p>CAPÍTULO 4............................................................................................................ 36 Transferencias documentales .................................................................................. 36</p></li>
</ul>
</div><div class="page-virtual" data-number="2" data-type="page" id="page-2">
<ul>
<li><p>CAPÍTULO 5............................................................................................................ 38 Disposición final de los documentos......................................................................... 38</p></li>
</ul>
<ul>
<li><p>TÍTULO 5......................................................................................................................... 41 VALORACIÓN DOCUMENTAL........................................................................................ 41</p><ul>
<li><p>CAPÍTULO 1................................................................................................................ 41 Tablas de Retención Documental y Tablas de Valoración Documental........................ 41</p><ul>
<li><p>SECCIÓN 1.............................................................................................................. 41</p><p>Elaboración y aprobación de las Tablas de Retención Documental - TRD y Tablas de Valoración Documental – TVD ................................................................................. 41</p>
</li>
<li><p>SECCIÓN 2.............................................................................................................. 44</p><p>Evaluación y convalidación de Tablas de Retención Documental y Tablas de Valoración Documental............................................................................................ 44</p>
</li>
<li><p>SECCIÓN 3.............................................................................................................. 48</p><p>Inscripción en el Registro Único de Series Documentales – RUSD y publicación de las Tablas de Retención Documental - TRD y Tablas de Valoración Documental – TVD.......................................................................................................................... 48</p>
</li>
<li><p>SECCIÓN 4.............................................................................................................. 49 Actualización de las Tablas de Retención Documental – TRD ................................. 49</p></li>
<li><p>SECCIÓN 5.............................................................................................................. 51</p></li>
</ul>
<p>Implementación de las Tablas de Retención Documental – TRD y Tablas de Valoración Documental – TVD ................................................................................. 51</p>
</li>
<li><p>CAPÍTULO 2................................................................................................................ 52 Valoración de fondos documentales acumulados ........................................................ 52</p></li>
</ul>
</li>
<li><p>TÍTULO 6......................................................................................................................... 54 CONSERVACIÓN Y PRESERVACIÓN DE DOCUMENTOS........................................... 54</p><p>CAPÍTULO 1................................................................................................................ 54 Sistema Integrado de Conservación ............................................................................ 54</p>
<ul>
<li><p>SECCIÓN 1............................................................................................ 54 Generalidades ........................................................................................ 54</p></li>
<li><p>SECCIÓN 2............................................................................................ 56 Plan de Conservación Documental ............................................................. 56</p></li>
<li><p>SECCIÓN 3............................................................................................ 58 Plan de Preservación Digital a Largo Plazo .................................................. 58</p></li>
</ul>
</li>
<li><p>TÍTULO 7......................................................................................................................... 62 ACCESO Y CONSULTA DE LOS DOCUMENTOS.......................................................... 62</p></li>
</ul>
<ul>
<li><p>CAPÍTULO 1................................................................................................................ 62 Acceso a la información y los documentos................................................................... 62</p></li>
<li><p>CAPÍTULO 2................................................................................................................ 64 Reproducción de documentos por otros medios técnicos ............................................ 64</p></li>
</ul>
</div><div class="page-virtual" data-number="3" data-type="page" id="page-3">
<ul>
<li><p>TÍTULO 8......................................................................................................................... 65 PATRIMONIO DOCUMENTAL ........................................................................................ 65</p><ul>
<li><p>CAPÍTULO 1................................................................................................................ 65 Registro Nacional de Archivos Históricos Colombianos – RENAHC ............................ 65</p></li>
<li><p>CAPÍTULO 2................................................................................................................ 66 Declaratoria de Bienes de Interés Cultural de Carácter Documental Archivístico -BICCDA............................................................................................................................. 66</p></li>
</ul>
<ul>
<li><p>SECCIÓN 1............................................................................................ 66 Disposiciones generales........................................................................... 66</p></li>
<li><p>SECCIÓN 2............................................................................................ 68 Procedimiento para la declaratoria de BIC-CDA............................................ 68</p></li>
<li><p>SECCIÓN 3............................................................................................ 70 Lista Indicativa de Candidatos a Bienes de Interés Cultural de Carácter Documental Archivístico – LICBIC-CDA....................................................... 70</p></li>
<li><p>SECCIÓN 4............................................................................................ 72 Régimen Especial de Protección de los Bienes de Interés Cultural de Carácter Documental Archivístico – BIC-CDA ........................................................... 72</p></li>
</ul>
<p>CAPITULO 3................................................................................................................ 78 Adquisición y expropiación de archivos privados ......................................................... 78</p>
<ul>
<li><p>SECCIÓN 1.............................................................................................................. 79 Adquisición de archivos privados por donación o compra ........................................ 79</p></li>
<li><p>SECCIÓN 2.............................................................................................................. 80 Expropiación administrativa de archivos privados .................................................... 80</p></li>
</ul>
</li>
<li><p>TÍTULO 9......................................................................................................................... 83 DISPOSICIONES ESPECIALES...................................................................................... 83</p></li>
</ul>
<ul>
<li><p>CAPÍTULO 1................................................................................................................ 83 Archivos, Derechos Humanos - DDHH y Derecho Internacional Humanitario DIH ....... 83</p><ul>
<li><p>SECCIÓN 1.............................................................................................................. 84</p><p>Criterios para la identificación y valoración de documentos relativos a los Derechos Humanos.................................................................................................................. 84</p>
</li>
<li><p>SECCIÓN 2.............................................................................................................. 85</p></li>
</ul>
<p>Criterios para la identificación y valoración de documentos referidos a las graves y manifiestas violaciones a los Derechos Humanos, e infracciones al Derecho Internacional Humanitario, ocurridas con ocasión del conflicto armado interno........ 85</p>
</li>
<li><p>CAPÍTULO 2................................................................................................................ 87 Archivos fotográficos, sonoros y audiovisuales............................................................ 87</p></li>
<li><p>CAPÍTULO 3................................................................................................................ 88 Reconstrucción de Expedientes................................................................................... 88</p></li>
<li><p>CAPÍTULO 4................................................................................................................ 90 Expedientes Pensionales............................................................................................. 90</p></li>
<li><p>CAPÍTULO 5................................................................................................................ 92</p></li>
</ul>
</div><div class="page-virtual" data-number="4" data-type="page" id="page-4">
<ul>
<li><p>Historias Laborales ...................................................................................................... 92</p></li>
<li><p>CAPÍTULO 6................................................................................................................ 93 Cámaras de Comercio ................................................................................................. 93</p></li>
<li><p>CAPÍTULO 7................................................................................................................ 94 Licencias urbanísticas y demás documentos que se producen en ejercicio de la función pública asignada a los curadores urbanos por mandato legal...................................... 94</p></li>
</ul>
<ul>
<li><p>TÍTULO 10....................................................................................................................... 96 DISPOSICIONES FINALES............................................................................................. 96 ANEXOS DEL ACUERDO ............................................................................................... 98</p></li>
</ul>
<ul>
<li><p>ANEXO 1. “Definiciones”.............................................................................................. 98</p></li>
<li><p>ANEXO 2. “Lineamientos generales para la formulación de la Política Institucional de Gestión Documental.” ................................................................................................ 123</p></li>
<li><p>ANEXO 3. “Formato Único de Inventario Documental - FUID” ................................... 130</p></li>
<li><p>ANEXO 4. “Programa de Gestión Documental – PGD”.............................................. 134</p></li>
<li><p>ANEXO 5. “Instructivo y Formato de Cuadro de Clasificación Documental - CCD” .... 136</p></li>
<li><p>ANEXO 6. “Etapas, instructivo y formato - Tablas de Retención Documental – TRD” 139</p></li>
<li><p>ANEXO 7. “Instructivo y formato - Tabla de Valoración Documental – TVD”.............. 144</p></li>
<li><p>ANEXO 8. “Instructivo y formato para descripción de Fondos o Colecciones de documentos fotográficos”........................................................................................... 147</p></li>
<li><p>ANEXO 9. “Instructivo y formato para descripción de Fondos o Colecciones de documentos sonoros”................................................................................................. 151</p></li>
<li><p>ANEXO 10. “Instructivo y formato para descripción de Fondos o Colecciones de documentos audiovisuales”........................................................................................ 155</p></li>
</ul>
</div><div class="page-virtual" data-number="5" data-type="page" id="page-5">
<h1>EL CONSEJO DIRECTIVO DEL ARCHIVO GENERAL DE LA NACIÓN JORGE PALACIOS PRECIADO</h1>
<p>En ejercicio de sus facultades legales, en especial las que le confiere la Ley 80 de 1989, el artículo 76, literal b) de la Ley 489 de 1998, la Ley 594 de 2000, el Decreto 158 de 2022, el Decreto 1080 de 2015, el Acuerdo 09 de 2012 y,</p>
<h1>CONSIDERANDO:</h1>
<p>Que el literal b) del artículo 76 de la Ley 489 de 1998, faculta al Consejo Directivo del Archivo General de la Nación para: “Formular a propuestas del representante legal, la política de mejoramiento continuo de la entidad, así como los programas orientados a garantizar el desarrollo administrativo; (…)”.</p>
<p>Que el artículo 1º de la Ley 594 de 2000, establece las reglas y principios generales que regulan la función archivística del país.</p>
<ul>
<li><p>Que, el artículo 3 de la Ley 594 del 2000 define la Función Archivística como las “(…) actividades relacionadas con la totalidad del quehacer archivístico, que comprenden desde la elaboración del documento hasta su eliminación o conservación permanente”, por tanto, incluye todos los procesos de la gestión documental y administración de archivos sin importar el soporte o formato de los documentos.</p></li>
<li><p>Que, el artículo 4 de la mencionada Ley, designa, dentro de los principios generales de la función archivística, al Archivo General de la Nación como la Entidad: “(…) e) del Estado encargada de orientar y coordinar la función archivística para coadyuvar a la eficiencia de la gestión del Estado y salvaguardar el patrimonio documental como parte integral de la riqueza cultural de la Nación, cuya protección es obligación del Estado, según lo dispone el título I de los principios fundamentales de la Constitución Política; (…)”. “(...) g) Los archivos actúan como elementos fundamentales de la racionalidad de la administración pública y como agentes dinamizadores de la acción estatal. Así mismo, constituyen el referente natural de los procesos informativos de aquélla”;” (…).</p></li>
</ul>
<p>Que el artículo 4, en su literal a) determina que “(…) los archivos harán suyos los fines esenciales del Estado, en particular los de servir a la comunidad y garantizar la efectividad de los principios, derechos y deberes consagrados en la Constitución y los de facilitar la participación de la comunidad y el control del ciudadano en las decisiones que los afecten, en los términos previstos por la ley (…)”</p>
</div><div class="page-virtual" data-number="6" data-type="page" id="page-6">
<p>Que el artículo 34 de la Ley 594 de 2000, faculta al Archivo General de la Nación para fijar: “(…) los criterios y normas técnicas y jurídicas para hacer efectiva la creación, organización, transferencia, conservación y servicios de los archivos públicos, teniendo en cuenta lo establecido en esta ley y sus disposiciones”.</p>
<p>Que la parte VIII del Decreto 1080 de 2015, Decreto Único Reglamentario del Sector Cultura, reglamenta el Patrimonio Archivístico.</p>
<p>Que el literal i) del artículo 9º del Acuerdo 009 de noviembre 30 de 2012, faculta al Consejo Directivo del Archivo General de la Nación para: “Expedir las normas y reglamentos generales sobre el desarrollo de la función archivística del Estado, de conformidad con la Ley 594 de 2000 y en general sobre aquellos aspectos que exija la racionalización y normalización del trabajo archivístico a nivel nacional y territorial”.</p>
<p>Que, para facilitar el acceso a la información, las Entidades obligadas al cumplimiento del presente Acuerdo, deberán establecer y desarrollar criterios diferenciales, preferenciales y efectivos de acceso para personas y grupos que requieren atención diferenciada, tales como los niños, niñas y adolescentes, mujeres, adultos mayores, población LGBTIQ+, las personas en situación de discapacidad y los grupos étnicos, acatando lo ordenado en el artículo 8°, artículo 21° último inciso de la Ley 1712 de 2014 y el Decreto 1081 de 2015, artículo 2.1.1.5.4.7. numeral 1 ° y demás normas que las modifiquen, adicionen o sustituyan.</p>
<p>Que, con el fin de racionalizar las disposiciones vigentes expedidas por el Consejo Directivo del Archivo General de la Nación, se hace necesario unificar, actualizar y reglamentar otros aspectos técnicos adicionales, para establecer los criterios técnicos y jurídicos de la función archivística en el Estado Colombiano y fijar otras disposiciones.</p>
<p>Que en mérito de lo expuesto:</p>
</div><div class="page-virtual" data-number="7" data-type="page" id="page-7">
<p>ACUERDA: TÍTULO 1 DISPOSICIONES GENERALES CAPÍTULO 1 Objeto, ámbito de aplicación y definiciones</p>
<ul>
<li><p>Artículo 1.1.1. Objeto. Establecer los criterios técnicos y jurídicos para implementar la función archivística en el Estado Colombiano y fijar otras disposiciones en cumplimiento de la Ley 594 de 2000 y el Decreto 1080 de 2015 “Decreto Único del Sector Cultura” o por las normas que lo modifiquen.</p></li>
<li><p>Artículo 1.1.2. Ámbito de aplicación. El presente Acuerdo comprende a la administración pública, en sus diferentes niveles: nacional, departamental, distrital, municipal, así como las entidades privadas que cumplen funciones públicas y demás organismos regulados por la Ley 594 de 2000. Parágrafo. Para efectos del presente Acuerdo, se hará referencia al término de sujetos obligados, en concordancia con el ámbito de aplicación de la Ley 594 de 2000, Ley General de Archivos, para referir a las entidades públicas o privadas que cumplen funciones públicas, que por efecto incluye a: servidores públicos; trabajadores oficiales; personas naturales o jurídicas de derecho privado que por mandato legal cumplen una función pública.</p></li>
<li><p>Artículo 1.1.3. Definiciones. Para todos los efectos del presente Acuerdo, se tendrán en cuenta las definiciones del anexo. (Ver anexo 1 “Definiciones”). Así mismo, se tendrá como referente el glosario de términos publicado por el Archivo General de la Nación Jorge Palacios Preciado.</p></li>
</ul>
<p>Parágrafo. Los anexos que hacen parte integral del presente Acuerdo se podrán actualizar sin que sea necesaria su aprobación a través de un nuevo Acuerdo por parte del Consejo Directivo del Archivo General de la Nación Jorge Palacios Preciado.</p>
<p>CAPÍTULO 2 Planeación de la función archivística</p>
<p>Artículo: 1.2.1. Deber de la planeación. Los sujetos obligados deben establecer e implementar estrategias organizacionales dirigidas a la planeación, dirección y control de los recursos físicos, técnicos, tecnológicos, financieros y del talento humano, encaminadas al diseño, elaboración, aprobación y</p>
</div><div class="page-virtual" data-number="8" data-type="page" id="page-8">
<p>evaluación de los lineamientos de la gestión documental y administración de archivos, en concordancia con el plan nacional de desarrollo, el plan sectorial o el plan territorial, según corresponda, y con el plan estratégico institucional y planes de acción; así mismo, la planeación y desarrollo de la función archivística se debe articular con las políticas de gestión y desempeño institucional definidas en el Modelo Integrado de Planeación y Gestión - MIPG, de conformidad con el Decreto 1083 de 2015 “Decreto único reglamentario del sector Función Pública”, modificado por el Decreto 1499 de 2017, o las normas que los modifiquen, sustituyan o deroguen.</p>
<ul>
<li><p>Parágrafo 1. Las entidades que no están obligadas al cumplimiento del Modelo Integrado de Planeación y Gestión – MIPG, podrán considerar armonizar la planeación de la función archivística con los planes estratégicos que se adopten por el máximo órgano de gobierno.</p></li>
<li><p>Parágrafo 2. Representantes legales de las Entidades, secretaria/os generales o funcionarias/os administrativos de igual o superior jerarquía deben velar por la debida planeación y ejecución de los recursos tendientes al desarrollo de la función archivística, en concordancia con los componentes del Modelo de Gestión Documental y Administración de Archivos – MGDA, para la implementación de la Política Nacional de Archivos y Gestión Documental.</p></li>
</ul>
<ul>
<li><p>Artículo 1.2.2. Investigación institucional. Desde la etapa de planeación, es necesario comprender la procedencia, contexto y valores testimoniales de los documentos que genera, tramita o produce la entidad, por lo cual, se debe realizar una investigación que aborde el origen, desarrollo y transformación, a partir del análisis funcional y desde un enfoque sociocultural, político, económico, entre otros. Como resultado de la investigación se debe elaborar un documento denominado “Historia Institucional”. Dicha historia será el soporte para abordar la elaboración y actualización de los instrumentos archivísticos.</p></li>
</ul>
<ul>
<li><p>Parágrafo 1. Para elaborar la Historia Institucional se debe tener en cuenta documentos legales de creación o transformación de la entidad y por los cuales se establezcan las funciones de las unidades administrativas, oficinas productoras y cuerpos colegiados o asesores; procedimientos; documentos que permitan el estudio y análisis de contexto; entrevistas a los productores de documentos, entre otros.</p></li>
<li><p>Parágrafo 2. La Historia Institucional debe fundamentarse en las normas técnicas de descripción y presentar, como mínimo, la línea del tiempo y fechas extremas, organigramas, descripción y análisis del contexto de la creación o</p></li>
</ul>
</div><div class="page-virtual" data-number="9" data-type="page" id="page-9">
<p>transformación de la entidad y análisis de la producción documental, por cada uno de los periodos orgánico-funcionales.</p>
<ul>
<li><p>Artículo 1.2.3. Diagnóstico integral de la gestión documental y administración de archivos. Para realizar una adecuada planeación de la función archivística, los sujetos obligados deben realizar un diagnóstico integral de la gestión documental y administración de archivos. El diagnóstico debe ser elaborado considerando la totalidad de los documentos producidos o gestionados en soportes físicos o formatos electrónicos, dispuestos en diferentes medios y sistemas de información.</p><ul>
<li><p>Parágrafo 1. En el diagnóstico se debe evaluar como mínimo: los procesos de la gestión documental, aspectos administrativos, de conservación y preservación de los documentos, infraestructura física y tecnológica, estado de las diferentes políticas de gestión y desempeño institucional que inciden en el manejo de la información y en el desarrollo de la función archivística.</p></li>
<li><p>Parágrafo 2. Servirán de insumo para dicho diagnóstico los resultados del índice de medición de desempeño institucional - IDI, el índice de transparencia y acceso a la información pública - ITA, los resultados del autodiagnóstico del Modelo de Gestión Documental y Administración de Archivos – MGDA u otros modelos de madurez o mediciones realizadas a la entidad.</p></li>
<li><p>Parágrafo 3. El diagnóstico debe ser actualizado periódicamente de acuerdo con la planeación, seguimiento y evaluación que realice la entidad.</p></li>
</ul>
</li>
<li><p>Artículo 1.2.4. Instrumentos archivísticos para la planeación de la función archivística. Para la armonización de la planeación de la función archivística con la planeación estratégica institucional, los sujetos obligados deben formular, actualizar e implementar el Plan Institucional de Archivos – PINAR, el Programa de Gestión Documental – PGD con sus programas específicos y los planes del Sistema Integrado de Conservación.</p></li>
<li><p>Artículo 1.2.5. Formulación de la Política institucional de Gestión Documental. Los sujetos obligados deben formular su Política institucional de Gestión Documental, teniendo en cuenta los elementos establecidos en los artículos 2.8.2.5.6 y 2.8.2.5.7 del Decreto 1080 de 2015, Decreto Único Reglamentario del Sector Cultura, las normas que los modifiquen, deroguen o sustituyan y armonizarla con las políticas de gestión y desempeño institucional relacionadas con el manejo y seguridad de la información, sistemas administrativos y de gestión, y con el Modelo de Gestión Documental y Administración de Archivos – MGDA, para establecer el direccionamiento</p></li>
</ul>

`);


</script>

<style lang="css" scoped></style>
