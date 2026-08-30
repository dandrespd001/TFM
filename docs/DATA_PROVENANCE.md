# Procedencia y clasificación de la evidencia

## Principio central

La red modelada se construyó con información pública y documental, interpretación técnica, decisiones explícitas del autor y resultados de PowerWorld. Por ello, “dato real” no debe usarse como categoría genérica. La categoría correcta depende del origen de cada campo.

## Clases de evidencia

| Código | Significado | Puede presentarse como medición de campo |
|---|---|---|
| `OBS` | Observado o documentado en una fuente, archivo o interfaz | Solo si la fuente demuestra que es una medición; no por el código en sí |
| `SPEC` | Especificación o decisión explícita del modelo | No |
| `PROXY` | Aproximación adoptada por ausencia de un dato primario | No |
| `HIP` | Hipótesis de trabajo o escenario | No |
| `DER` | Valor calculado a partir de otros parámetros | No |
| `SIM` | Salida de PowerWorld o resumen directo de la simulación | No |
| `VIS` | Lectura visual de una captura o interfaz, sujeta a redondeo | No |

Un campo puede combinar clases, por ejemplo `OBS/SPEC` o `DER/HIP`. La combinación obliga a explicar ambas partes, no a escoger la más conveniente.

## Fuentes primarias dentro del paquete

- `data/provenance/v2/registro_parametros.csv` es la tabla principal para saber qué se observó, especificó, aproximó o derivó.
- `data/provenance/v2/casos_v2_validacion.json` documenta la configuración validada y las limitaciones conocidas.
- `models/powerworld/v2` y `results/simulations/v2` contienen modelos, exportaciones y resultados.
- `results/quality/v4/matriz_afirmaciones_finales_v4.csv` enlaza afirmaciones, transformaciones y redondeos.
- `manifests/SOURCE_MANIFEST.csv` verifica que los artefactos publicados son copias exactas de las fuentes seleccionadas.

## Separación entre entradas y resultados

Las entradas del modelo incluyen topología, tensiones nominales, parámetros de líneas y transformadores, demandas, generación y escenarios. Su naturaleza se determina campo a campo con `registro_parametros.csv`.

Los resultados incluyen tensiones por unidad, ángulos, pérdidas, cargabilidad, estados de isla, desbalances y criterios de cumplimiento. Son resultados estacionarios simulados o derivados de dichas simulaciones.

La evaluación potencia–energía del BESS es un cálculo derivado. No representa un despacho cronológico ni una optimización del almacenamiento.

## Integridad y transformaciones

Los archivos fuente seleccionados no se editaron al reorganizarlos. Su SHA-256 se registró antes de incorporarlos. Los documentos explicativos y manifiestos del repositorio son nuevos; no alteran la evidencia original.

Cuando una ruta interna siga apuntando a la estructura histórica, debe resolverse mediante el manifiesto de fuentes. No se sustituyeron rutas dentro de los CSV/JSON porque eso cambiaría su hash y debilitaría la trazabilidad.
