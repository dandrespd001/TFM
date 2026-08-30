# Procedencia de la evidencia

El repositorio no contiene una colección homogénea de “datos reales”. Las entradas combinan información pública o documental, observaciones de archivos/interfaz, especificaciones, proxies, hipótesis y cálculos derivados. Las salidas son resultados de simulación.

| Código | Significado | ¿Medición de campo? |
|---|---|---|
| `OBS` | Observado o documentado | Solo si la fuente concreta lo demuestra |
| `SPEC` | Especificación o decisión del modelo | No |
| `PROXY` | Aproximación por falta de dato primario | No |
| `HIP` | Hipótesis o escenario | No |
| `DER` | Cálculo derivado | No |
| `SIM` | Salida de PowerWorld | No |
| `VIS` | Lectura visual redondeada | No |

La clasificación campo a campo se encuentra en `data/provenance/v2/registro_parametros.csv`. Los resultados se contrastan primero con AUX/CSV, después con las tablas consolidadas y, por último, con capturas si solo existe evidencia visual.

Los archivos fuente seleccionados se copiaron sin edición. `manifests/SOURCE_MANIFEST.csv` conserva ruta relativa, SHA-256, tamaño, categoría y nota de interpretación.
