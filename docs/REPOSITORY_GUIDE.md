# Guía del repositorio

## Mapa general

### `deliverables/`

Contiene las versiones académicas canónicas desde V2. Cada subcarpeta conserva el documento Word y, cuando existe, el PDF de control y el informe de auditoría. No existe un PDF V2 dentro de las fuentes seleccionadas, por lo que no se creó uno artificialmente.

- `v2/`: primera versión incluida en este paquete y su auditoría.
- `v3/`: ampliación académica, PDF de control y auditoría V3.
- `v4/`: versión más reciente, PDF de control y auditoría V4.

### `data/provenance/v2/`

Reúne el núcleo que permite interpretar los parámetros del modelo:

- `registro_parametros.csv`: valor histórico, valor V2, unidad, clase de evidencia, fuente y motivo.
- `casos_v2_validacion.json`: casos GMD, barras, líneas y limitaciones de validación.
- `aux_schema_validado.json`: estructura contrastada de las exportaciones AUX.
- `EVIDENCIA_POWERWORLD_BASE.md`: acta técnica del caso base y advertencias de uso.
- `hashes_originales.csv`: hashes históricos producidos durante el cierre V2; sus rutas son las originales del entorno de trabajo.

### `models/powerworld/v2/`

Conserva los modelos PWB/PWD y exportaciones manuales AUX/CSV. Los archivos binarios requieren PowerWorld o software compatible; los AUX y CSV permiten revisar parámetros y resultados sin abrir el caso binario.

### `results/simulations/v2/`

- `photovoltaic/`: escenarios FV para dos separaciones medias geométricas (GMD) y ubicaciones/penetraciones consideradas.
- `bess/`: cuatro configuraciones finales de ubicación/GMD, contingencias, tablas consolidadas y cálculo potencia–energía.
- `screenshots/`: cuatro capturas de PowerWorld usadas como evidencia visual en el documento.

Estas carpetas contienen resultados simulados o cálculos derivados, no mediciones reales de la red.

### `results/summary-tables/`

Tablas consolidadas para el caso base, parámetros de línea, escenarios FV, contingencias BESS y sensibilidad energética. Son la entrada más práctica para contrastar cifras del TFM, pero toda discrepancia debe resolverse acudiendo a la evidencia AUX/CSV y a la matriz de afirmaciones.

### `results/quality/`

- `v2/`: trazabilidad inicial, resultados de ejecución y registro de figuras/tablas.
- `v3/`: matriz ampliada de afirmaciones y manifiesto de cierre V3.
- `v4/`: matriz de coherencia, requisitos VIU, revisión visual, cambios V3–V4 y controles automáticos.

### `references/`

Exportaciones BibTeX, CSL JSON e inventarios bibliográficos por versión. Sirven para auditar metadatos; las citas dinámicas del DOCX y la publicación original siguen siendo la autoridad para la forma final de la referencia.

### `archive/v2-planning/`

Material histórico o de planificación que se conserva para trazabilidad, pero no gobierna las conclusiones. Incluye el manifiesto de 4.400 ejecuciones planeadas (`status: planned`) y cálculos BESS preliminares.

### `manifests/`

- `SOURCE_MANIFEST.csv`: ruta fuente relativa al proyecto local, destino en GitHub, hash, tamaño, clase y nota de cada artefacto copiado.
- `REPOSITORY_MANIFEST.json`: inventario autocontenido de los archivos publicados y sus hashes.

### `tools/`

Herramientas locales y sin dependencias externas para actualizar el inventario del repositorio. No ejecutan PowerWorld ni recalculan resultados eléctricos.

## Cómo localizar una cifra

1. Buscar el valor o `claim_id` en `results/quality/v4/matriz_afirmaciones_finales_v4.csv`.
2. Revisar `fuente`, `campo_origen`, `transformacion` y `redondeo`.
3. Consultar la tabla consolidada correspondiente.
4. Contrastar con el AUX/CSV de la simulación si la afirmación es material.
5. Si solo aparece en una captura, describirla como observación visual y respetar el redondeo de interfaz.

## Rutas históricas

Algunos CSV y JSON conservan rutas originales como `TFM/Entrega_final/...`. Se mantienen sin modificar para preservar hashes y procedencia. Use `SOURCE_MANIFEST.csv` y esta guía para resolverlas a las rutas organizadas del repositorio.
