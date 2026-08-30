# Informe de auditoría integral del TFM de San Andrés — V4

Fecha de cierre técnico: 30 de agosto de 2026  
Estado: `LISTO_PARA_REVISION_TUTOR_VIU`  
Estado de depósito: no declarado; quedan acciones externas del autor.

## 1. Alcance, jerarquía y criterio de la auditoría

La V4 se construyó como copia independiente de la V3 final. No se modificaron la V1, la V2, la V3, la plantilla VIU ni los archivos de evidencia. La jerarquía aplicada fue: documentación oficial de la VIU; objetivos y alcance aprobados; V1 revisada para la primera parte; V3 como versión académica de partida; archivos CSV, JSON, AUX y modelos reproducibles para resultados; y fuentes científicas, normativas e institucionales verificadas para la atribución.

Se leyeron y contrastaron la plantilla `P11_06_F08b`, las normas APA VIU de séptima edición, las tutorías sobre APA y escritura académica, la tutoría inicial del máster y el Anexo I de alcance. La revisión no consistió en una normalización global del DOCX. Cada cambio fue localizado para preservar estilos institucionales, ecuaciones OMML, campos Zotero, campos de índices, encabezados y elementos gráficos.

La auditoría tuvo cuatro dimensiones: coherencia académica; consistencia técnica y matemática; integridad documental de Word, Zotero y APA 7; y composición visual del PDF exportado por Microsoft Word. Los resultados eléctricos no se recalcularon para crear hallazgos nuevos. Se conservaron y reverificaron las relaciones representativas ya respaldadas por el paquete reproducible.

## 2. Inmutabilidad y trazabilidad de versiones

Los hashes SHA-256 finales de los archivos protegidos coinciden con los congelados al inicio:

- V1 revisada: `8C48A1DFC55EEC8FE93D9CD8C3F3FBEB3A038335F03CB1C0EE4E0EC43B423BA2`.
- V2: `BEE726BF2481D6FA47189705F2271EF4CD021522B33B091177E16203FDF0509C`.
- V3: `0A3C30D07306897BDA86D708D252A9CBBC1BC8895663248834A193B940B8AB95`.
- Plantilla VIU: `6C38C3777B39626A9DF6E4D846D12B12531460C41438A6FFD60C2BF7A8C9B8A5`.

La V4 final tiene hash DOCX `11C7843D51824FDF5084CF2B432B028836C61BE95D1EC045D1E2D507A13EF43E` y su PDF de control `5978E1BD8BEB3175B35EB11D025DAE4E5A618A7ECD41F1ACE335F4A1D2ABD4EF`. Los hashes se registran también en `reproducibilidad/v4/hashes_finales_v4.json`.

## 3. Hallazgos de la V3 y correcciones aplicadas

La V3 ya presentaba una estructura académica y visual sólida. La mayoría de sus resultados, figuras, tablas, ecuaciones y referencias eran correctos. La auditoría V4 detectó, sin embargo, tres tipos de inconsistencia interna que convenía resolver antes de la revisión del tutor.

Primero, tres menciones textuales indicaban 27 fuentes aunque la bibliografía dinámica contenía 42 referencias y los campos Zotero citaban las 42. La V4 corrige esas menciones a 42 sin añadir bibliografía artificial. La cifra ahora coincide en el marco teórico, las conclusiones, las tablas de cierre y el inventario bibliográfico.

Segundo, el anexo declaraba una matriz de 82 afirmaciones, pero la matriz reproducible final contiene 166 filas con identificador único. La V4 corrige la descripción del anexo y el inventario mínimo para que la cifra publicada sea 166. Se conservaron los 164 registros aprobados y los dos registros `NR`, cuya falta de dato se declara expresamente sin imputación.

Tercero, persistían expresiones propias del proceso editorial —por ejemplo, referencias a capas, borradores o versiones internas— dentro del discurso académico. Se realizaron 23 sustituciones localizadas para que el manuscrito describa modelos, evidencias y decisiones, no el historial de producción. También se tradujo la primera mención de *Specification-Driven Development* como «desarrollo guiado por especificaciones (SDD)». No se alteró el significado técnico ni se aplicaron sustituciones mecánicas de sinónimos.

## 4. Coherencia entre objetivos y capítulos

El objetivo general y los cinco objetivos específicos se compararon con la V1 revisada. Los cinco objetivos específicos permanecen literalmente intactos. La matriz `matriz_coherencia_v4.csv` vincula cada objetivo con método, evidencia, discusión y conclusión.

El OE1 se responde mediante el modelo académico de seis barras, los dos estados de GMD y la documentación de parámetros y supuestos. El OE2 se sustenta en 42 fuentes y en la síntesis crítica del estado del arte. El OE3 se verifica con los 18 escenarios FV y los indicadores de tensión, carga, pérdidas y flujo. El OE4 se responde con 180 contingencias FV y 40 evaluaciones BESS, separando tensión, isla, sobrecarga y continuidad. El OE5 se cierra con una propuesta preliminar de ubicación y potencia, sin convertirla en optimización ni dimensionamiento comercial.

Las conclusiones no introducen resultados nuevos. Distinguen alcance demostrado, aportación, limitaciones y trabajo posterior. El documento no atribuye a PowerWorld simulaciones dinámicas, despacho cronológico, optimización ni dimensionamiento energético. El BESS se interpreta como inyección PQ estacionaria y no como prueba de formación de red, frecuencia, degradación o autonomía real.

## 5. Matemática, unidades y evidencia cuantitativa

La V4 conserva las 19 ecuaciones nativas OMML. Se comprobaron la presencia y numeración de las ecuaciones de flujo AC, bases por unidad, utilización, balance, desbalances, actualización Newton–Raphson, convergencia, pérdidas, tensión mínima, sensibilidad GMD y relación potencia–energía del BESS. Las explicaciones mantienen propósito, variables, unidades, supuestos y límites de aplicación.

Las verificaciones representativas confirmaron que la potencia FV se deriva de 34,255320 MW multiplicados por el porcentaje de penetración; que el margen respecto de 0,95 p.u. coincide con la tensión mínima menos ese umbral; y que la energía nominal BESS conserva la relación entre potencia, duración, eficiencia 0,93 y ventana de estado de carga 0,80. Los redondeos visibles se distinguen de los valores conservados con seis decimales en los CSV.

La matriz de afirmaciones V4 contiene 166 filas, identificadores únicos y campos de sección, valor, unidad, valor mostrado, fuente, campo de origen, transformación, redondeo y estado. Toda cifra material queda vinculada con los cuatro archivos fuente previstos. Los dos valores no recuperados permanecen como `NR`; no se inventó ni interpoló ningún dato.

## 6. Formato VIU, ecuaciones, tablas y figuras

El DOCX final conserva dos secciones intencionadas: la portada institucional y el cuerpo académico. El cuerpo mantiene A4 y márgenes de aproximadamente 3 cm. Los estilos conservan Arial y la jerarquía institucional. La inspección visual confirma texto justificado, interlineado y espaciado coherentes, encabezados VIU, numeración de páginas, saltos y composición homogénea.

Se conservaron 37 tablas OOXML en total, entre ellas las 17 tablas científicas numeradas. Las Tablas 10, 11 y 12 se revisaron de manera especial: sus cifras, unidades y encabezados se leen sin palabras partidas, desbordes ni solapes. Se mantuvo un tamaño legible y los encabezados se repiten mediante propiedades estructurales de tabla.

Las seis figuras científicas permanecen completas. Las cuatro capturas de PowerWorld son independientes, legibles y cuentan con título, nota de elaboración propia a partir de PowerWorld Simulator, mención previa, análisis posterior y texto alternativo. Los porcentajes visibles se presentan como observaciones redondeadas de interfaz y no reemplazan los valores numéricos de los archivos reproducibles.

El control estructural encontró siete objetos gráficos en el cuerpo y los siete tienen descripción alternativa. No existe parte de comentarios, no hay cambios controlados, no hay resaltados residuales y no hay texto oculto improcedente fuera de los componentes internos de los tres índices automáticos.

## 7. Zotero, citas y bibliografía APA 7

Zotero Refresh se ejecutó en Microsoft Word con Zotero Desktop 10.0.1. No aparecieron errores. El guardado final conserva 53 campos dinámicos de cita, 42 claves Zotero únicas, una bibliografía dinámica y 42 entradas bibliográficas. La correspondencia es bidireccional: toda cita tiene referencia y las 42 referencias están citadas.

El DOCX mantiene el estilo oficial APA y la localización `es-ES`. En citas parentéticas de dos autores se conserva `&`, conforme a la salida del estilo APA de Zotero, mientras que las construcciones narrativas emplean «y». La bibliografía se mantiene en orden alfabético, con cursivas y sangría francesa. No se detectaron títulos duplicados, referencias huérfanas ni campos rotos.

No se añadieron fuentes solo para aumentar una cantidad. Las 42 fuentes verificadas de la V3 cubren la brecha bibliográfica definida, por lo que la V4 las conserva. Las normas IEEE se presentan como referencias técnicas internacionales, no como normas obligatorias para Colombia.

## 8. Extensión y revisión visual

Microsoft Word exportó un PDF de 85 páginas. El capítulo 9, Anexos, comienza en la página 84; por tanto, existen 83 páginas antes de anexos, dentro del intervalo objetivo de 82 a 85. Los anexos ocupan dos páginas, equivalentes al 2,3529 % del documento, por debajo del 10 %.

El resumen contiene 287 palabras y el abstract 290; ambos cumplen el intervalo de 200 a 300 palabras. El recuento XML del manuscrito es de 22.083 palabras. La ampliación proviene de contenido académico sustantivo y no de manipulación tipográfica.

Se renderizaron las 85 páginas del PDF final a PNG y se agruparon en ocho láminas de contacto. Cada página fue inspeccionada. No se observaron páginas vacías indebidas, objetos fuera de la caja, tablas truncadas, fórmulas cortadas, solapes, imágenes ilegibles ni saltos problemáticos. El acta `acta_revision_visual_v4.csv` contiene 85 registros aprobados con nota individual.

## 9. Originalidad, redacción y límites del control local

La redacción se revisó para mantener un español académico natural, preciso y coherente con la voz de un ingeniero que conoce el estudio. Se eliminaron expresiones editoriales y se reforzaron las relaciones entre afirmación, evidencia e interpretación. No se inventaron experiencias personales, errores, anécdotas, datos, fuentes ni resultados para aparentar autoría. Tampoco se realizaron técnicas de evasión de detectores.

El control local de atribución acredita estructura Zotero, correspondencia bidireccional, ausencia de duplicados y trazabilidad de fuentes. Este control no sustituye Turnitin ni permite afirmar un porcentaje de similitud o detección de IA. No hubo acceso institucional autorizado a Turnitin; por ello no existe informe Turnitin en el paquete y se registra `PENDIENTE_EXTERNO`. Una prueba automática de IA tampoco se utiliza como criterio de aprobación académica.

## 10. Resultado y acciones externas pendientes

Las pruebas automáticas y la revisión visual respaldan el estado `LISTO_PARA_REVISION_TUTOR_VIU`. La V4 es independiente, editable y conserva los campos dinámicos. Cumple la extensión objetivo, mantiene los objetivos literales, preserva 19 ecuaciones, seis figuras y 17 tablas científicas, y presenta 42 referencias correctamente vinculadas.

Como síntesis de integridad, la V4 conserva 53 campos de cita dinámicos y documenta 166 afirmaciones cuantitativas trazables. El estado no equivale a `LISTO_PARA_DEPOSITO`. Antes del depósito, el autor debe realizar las siguientes acciones externas pendientes:

1. Sustituir o confirmar el marcador de DNI de la portada según la instrucción de la VIU.
2. Ejecutar Turnitin institucional con acceso autorizado, conservar el informe real y revisar coincidencia por coincidencia.
3. Obtener la aprobación del tutor.
4. Completar los formularios y requisitos administrativos de entrega.

Fuera de esas acciones externas, no queda una incidencia técnica o documental abierta en la V4 entregada.
