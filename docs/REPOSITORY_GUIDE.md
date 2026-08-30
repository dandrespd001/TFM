# Guía de las evidencias de simulación

La estructura separa parámetros, modelos, resultados y manifiestos para que cada cifra pueda seguirse hasta su archivo técnico de origen.

## `data/provenance/v2`

- `registro_parametros.csv`: valor histórico, valor V2, unidad, clase de evidencia, fuente y motivo.
- `casos_v2_validacion.json`: casos GMD, barras, líneas, software y limitaciones conocidas.
- `aux_schema_validado.json`: esquema contrastado de las exportaciones AUX.
- `EVIDENCIA_POWERWORLD_BASE.md`: acta técnica del caso base.

## `models/powerworld/v2`

Contiene los archivos PWB/PWD y las exportaciones manuales del modelo base. Los binarios requieren PowerWorld o software compatible; AUX y CSV permiten revisar parámetros y estados sin abrir el caso binario.

## `results/simulations/v2/photovoltaic`

Contiene los escenarios FV organizados por GMD. Cada bloque agrupa exportaciones de barras, ramas, cargas, generación, transformadores, islas, contingencias, desbalances y violaciones.

## `results/simulations/v2/bess`

Contiene las cuatro configuraciones finales BESS, resultados por contingencia, matrices consolidadas y sensibilidad potencia–energía. Estos cálculos no constituyen un despacho cronológico.

## `results/simulations/v2/screenshots`

Cuatro capturas de PowerWorld. Deben interpretarse como observaciones visuales con redondeo de interfaz.

## `results/summary-tables`

Tablas de lectura rápida para el caso base, parámetros de línea, escenarios FV y BESS. Si existe una discrepancia, prevalece la exportación AUX/CSV correspondiente y debe documentarse la transformación.

## Manifiestos (`manifests`) y herramientas (`tools`)

`SOURCE_MANIFEST.csv` comprueba procedencia frente al proyecto local. `REPOSITORY_MANIFEST.json` comprueba el árbol publicado. Las herramientas actualizan y validan el segundo manifiesto; no ejecutan PowerWorld.
