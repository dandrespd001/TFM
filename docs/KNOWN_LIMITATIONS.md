# Limitaciones conocidas

1. **No hay mediciones de campo en bruto.** El paquete no contiene SCADA, registros horarios del operador ni campañas instrumentales propias.
2. **No es un modelo *as-built* certificado.** La topología y los parámetros proceden de fuentes públicas/documentales, interpretación, decisiones y proxies declarados.
3. **El análisis es estacionario.** Las salidas corresponden a flujo de carga y contingencias N-1; no demuestran estabilidad transitoria, respuesta de frecuencia ni desempeño dinámico de inversores.
4. **La campaña de 4.400 filas fue planeada.** `archive/v2-planning/resumen_manifest_campana.json` conserva `status: planned`; no debe citarse como ejecución completada.
5. **Los esquemas vacíos no son resultados.** Los tres CSV `resultados_barras`, `resultados_ramas` y `resultados_runs` conservados en `results/quality/v2` solo contienen encabezados.
6. **La validación de PowerWorld es parcial.** El acta V2 indica que la comprobación avanzada de datos no quedó validada y que “Initialized” o cero violaciones no bastan por sí solos.
7. **Las capturas tienen precisión de interfaz.** Los porcentajes visibles deben describirse como valores redondeados observados en PowerWorld.
8. **El BESS no tiene despacho cronológico.** La relación potencia–energía es un cálculo de sensibilidad, no una optimización ni un dimensionamiento definitivo.
9. **Las normas IEEE son referencias técnicas.** No deben presentarse como normativa colombiana obligatoria salvo respaldo jurídico específico.
10. **Turnitin es externo.** El repositorio no demuestra un porcentaje de similitud ni de detección de IA; el estado real se registra en `turnitin_status_v4.json`.
11. **V4 no equivale a depósito.** Quedan sujetos a confirmación externa la aprobación del tutor, los formularios y los controles institucionales.
