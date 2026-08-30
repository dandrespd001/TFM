# Evidencias de simulación — red aislada de San Andrés

Este repositorio conserva exclusivamente la evidencia técnica de las simulaciones eléctricas desarrolladas para estudiar integración fotovoltaica y BESS en un modelo reducido de la red aislada de San Andrés. El árbol actual no contiene el manuscrito del TFM, auditorías editoriales, bibliografía Zotero ni documentación institucional de la VIU.

## Qué contiene

| Ruta | Contenido |
|---|---|
| `data/provenance/v2` | Parámetros, clases de evidencia, configuración validada y acta del caso base |
| `models/powerworld/v2` | Modelos PWB/PWD y exportaciones manuales de PowerWorld |
| `results/simulations/v2/photovoltaic` | Salidas AUX/CSV de los escenarios fotovoltaicos |
| `results/simulations/v2/bess` | Salidas, contingencias y cálculos derivados del BESS |
| `results/simulations/v2/screenshots` | Cuatro capturas de la interfaz de PowerWorld |
| `results/summary-tables` | Tablas consolidadas de parámetros y resultados |
| `manifests` | Inventarios SHA-256 de fuentes y del árbol publicado |
| `docs` | Guía, diccionario, procedencia, alcance y limitaciones |
| `tools` | Actualización y validación local del manifiesto |

## Qué no contiene

No contiene mediciones SCADA, series horarias reales, un modelo *as-built* certificado, el documento académico, PDFs, referencias bibliográficas ni controles editoriales. Tampoco conserva en el árbol actual la campaña de 4.400 corridas que solo estaba planificada.

Los resultados son flujos de carga estacionarios y contingencias N-1 producidos con PowerWorld Simulator 24 Evaluation. No demuestran estabilidad dinámica, optimización, despacho cronológico ni dimensionamiento definitivo de almacenamiento.

## Lectura recomendada

1. [`docs/SIMULATION_EVIDENCE_SCOPE.md`](docs/SIMULATION_EVIDENCE_SCOPE.md)
2. [`docs/REPOSITORY_GUIDE.md`](docs/REPOSITORY_GUIDE.md)
3. [`docs/DATA_PROVENANCE.md`](docs/DATA_PROVENANCE.md)
4. [`docs/DATA_DICTIONARY.md`](docs/DATA_DICTIONARY.md)
5. [`docs/KNOWN_LIMITATIONS.md`](docs/KNOWN_LIMITATIONS.md)

## Verificación

```powershell
python tools/update_repository_manifest.py
python tools/validate_repository.py
```

`SOURCE_MANIFEST.csv` relaciona cada artefacto técnico con su fuente local y SHA-256. `REPOSITORY_MANIFEST.json` inventaría el árbol publicado. Los archivos CSV, JSON y AUX se conservaron sin normalizar saltos de línea para no alterar sus hashes.

No se incluye una licencia de reutilización. Los derechos permanecen con sus respectivos autores y titulares.
