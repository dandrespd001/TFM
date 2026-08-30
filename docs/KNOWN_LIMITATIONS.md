# Limitaciones conocidas

1. No contiene SCADA, mediciones horarias de campo ni un modelo *as-built* certificado.
2. El análisis es estacionario: flujo de carga y contingencias N-1.
3. No demuestra estabilidad transitoria, respuesta de frecuencia ni dinámica de inversores.
4. La validación avanzada de datos de PowerWorld no quedó acreditada en el acta V2.
5. “Initialized” o cero violaciones no bastan sin revisar barras energizadas, islas y límites.
6. Las capturas presentan valores redondeados por la interfaz.
7. La relación potencia–energía del BESS es un cálculo derivado, no una optimización ni un despacho cronológico.
8. Los parámetros `SPEC`, `PROXY` e `HIP` deben mantenerse identificados como decisiones, aproximaciones o hipótesis.
9. La ausencia del manuscrito y de controles editoriales es deliberada: este repositorio se limita a evidencia de simulación.
