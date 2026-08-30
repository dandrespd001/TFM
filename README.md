# TFM — integración fotovoltaica y BESS en la red aislada de San Andrés

Este repositorio reúne, de forma ordenada y trazable, los entregables académicos, modelos, entradas, resultados y controles de calidad producidos desde la versión 2 del Trabajo Fin de Máster de Diomar Andrés Pacheco D. Su finalidad es permitir una nueva revisión técnica y editorial —incluida una pasada con GPT Work— sin confundir evidencia documental con hipótesis de modelado ni salidas simuladas con mediciones reales.

## Lectura recomendada

1. [`docs/GPT_WORK_CONTEXT.md`](docs/GPT_WORK_CONTEXT.md): contexto, límites y prompt inicial para la revisión.
2. [`docs/REPOSITORY_GUIDE.md`](docs/REPOSITORY_GUIDE.md): explicación de cada carpeta.
3. [`docs/DATA_PROVENANCE.md`](docs/DATA_PROVENANCE.md): procedencia y jerarquía de evidencia.
4. [`docs/DATA_DICTIONARY.md`](docs/DATA_DICTIONARY.md): códigos, campos y unidades principales.
5. [`docs/KNOWN_LIMITATIONS.md`](docs/KNOWN_LIMITATIONS.md): alcance real y afirmaciones que no deben extrapolarse.
6. [`docs/EXTERNAL_REFERENCES.md`](docs/EXTERNAL_REFERENCES.md): documentos VIU que deben aportarse por separado.
7. [`AGENTS.md`](AGENTS.md): instrucciones operativas para asistentes y agentes de revisión.

## Contenido principal

| Ruta | Contenido | Uso recomendado |
|---|---|---|
| `deliverables/v2` | DOCX V2 e informe de auditoría canónico | Punto de partida histórico |
| `deliverables/v3` | DOCX, PDF e informe V3 | Ampliación académica y trazabilidad |
| `deliverables/v4` | DOCX, PDF e informe V4 | Versión más reciente para revisión |
| `data/provenance/v2` | Parámetros, clasificación de evidencia y validación de casos | Interpretar de dónde procede cada dato |
| `models/powerworld/v2` | Casos y exportaciones de PowerWorld | Inspección del modelo eléctrico |
| `results/simulations/v2` | Resultados FV, BESS y capturas | Recalcular y contrastar resultados simulados |
| `results/summary-tables` | Tablas consolidadas | Lectura rápida de resultados gobernantes |
| `results/quality/v2..v4` | Matrices de afirmaciones, coherencia y controles | Auditoría académica y cuantitativa |
| `references/v2..v4` | Exportaciones bibliográficas | Verificación de autores, DOI y correspondencia de citas |
| `archive/v2-planning` | Planes e históricos no gobernantes | Contexto; no tratarlos como ejecuciones finales |
| `manifests` | Inventarios y SHA-256 | Comprobar integridad y procedencia |

## Advertencia sobre los “datos reales”

El repositorio no contiene una base SCADA, mediciones horarias de campo ni un modelo *as-built* certificado por el operador. Incluye información pública o documental, observaciones obtenidas de archivos y de la interfaz, decisiones de especificación, aproximaciones (*proxies*), hipótesis, cálculos derivados y resultados de simulación. Cada clase se explica en [`docs/DATA_PROVENANCE.md`](docs/DATA_PROVENANCE.md).

Los archivos de `archive/v2-planning` describen una campaña planeada de 4.400 corridas cuyo estado conservado es `planned`. No prueban que esas corridas se hayan ejecutado. Los resultados efectivamente disponibles deben determinarse a partir de los archivos de `results/simulations/v2`, las tablas consolidadas y las matrices de afirmaciones.

## Reproducción y verificación

La simulación se realizó con PowerWorld Simulator 24 Evaluation. Los CSV, JSON y AUX son legibles sin PowerWorld; los formatos PWB/PWD requieren software compatible. Para regenerar el inventario del repositorio:

```powershell
python tools/update_repository_manifest.py
```

Después, compare `manifests/REPOSITORY_MANIFEST.json` y `manifests/SOURCE_MANIFEST.csv`. El primer archivo inventaría el paquete publicado; el segundo conserva la correspondencia y el SHA-256 entre cada artefacto seleccionado y su fuente local.

## Estado académico

La V4 es la versión más reciente incluida, pero sigue siendo material de trabajo para revisión. No equivale a aprobación del tutor, informe Turnitin institucional ni autorización de depósito. El archivo `results/quality/v4/turnitin_status_v4.json` registra el estado real del control externo.

## Derechos y reutilización

No se incorpora una licencia de reutilización. Los derechos del texto, modelos y resultados permanecen con sus respectivos autores y titulares. Las fuentes externas deben consultarse y citarse desde sus publicaciones originales.
