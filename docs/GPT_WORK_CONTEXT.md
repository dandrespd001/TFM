# Contexto para una revisión con GPT Work

## Propósito

Este paquete permite hacer una revisión integral de la V4 del TFM sobre integración fotovoltaica y BESS en la red aislada de 34,5 kV de San Andrés. La revisión debe mejorar claridad, coherencia, formato, citación y trazabilidad sin producir resultados eléctricos nuevos ni exagerar el alcance de la evidencia.

Para comprobar formalmente la plantilla y las normas de la VIU, adjunte también los documentos enumerados en `docs/EXTERNAL_REFERENCES.md`. No están republicados en este repositorio porque son materiales institucionales externos.

## Archivo de trabajo

Use como base:

`deliverables/v4/TFM_San_Andres_APA_VIU_Diomar_Andres_Pacheco_D_FINAL_V4.docx`

El PDF V4 sirve para inspección visual. V2 y V3 son antecedentes de comparación y no deben sobrescribirse.

## Contexto técnico mínimo

- Alcance: flujo de carga estacionario y contingencias N-1 en PowerWorld Simulator 24 Evaluation.
- Red: modelo reducido de seis barras de la red aislada de San Andrés.
- Sensibilidad: dos valores GMD, escenarios fotovoltaicos y cuatro configuraciones finales BESS.
- Evidencia: parámetros documentales/observados, decisiones de especificación, proxies, hipótesis, derivados y salidas simuladas.
- Exclusiones: dinámica, estabilidad transitoria, optimización, despacho cronológico, validación de campo y modelo *as-built* certificado.

## Prompt recomendado

```text
Revisa la V4 de este TFM como un trabajo académico completo. Antes de proponer cambios, lee README.md, AGENTS.md, docs/DATA_PROVENANCE.md, docs/DATA_DICTIONARY.md, docs/KNOWN_LIMITATIONS.md y docs/EXTERNAL_REFERENCES.md. Usa results/quality/v4/matriz_coherencia_v4.csv para comprobar que cada objetivo tenga método, evidencia, discusión y conclusión, y usa results/quality/v4/matriz_afirmaciones_finales_v4.csv para verificar toda cifra material.

Trabaja sobre una copia nueva de la V4. No sobrescribas V2, V3 ni V4. Distingue siempre observaciones documentales (OBS), especificaciones (SPEC), proxies (PROXY), hipótesis (HIP), derivados (DER), resultados simulados (SIM) y observaciones visuales (VIS). No llames “datos reales” a todo el conjunto y no presentes salidas simuladas como mediciones de campo.

Comprueba coherencia interna, lógica técnica, unidades, redondeos, terminología, citas y bibliografía. Mejora el español académico de forma natural, sin inventar experiencias, fuentes, datos o resultados y sin técnicas de evasión de detectores. No atribuyas a PowerWorld análisis dinámico, optimización, despacho cronológico ni dimensionamiento energético. No trates archive/v2-planning/manifest_campana.csv como campaña ejecutada: su estado es planned.

Registra cada cambio con ubicación, problema, evidencia, corrección y prueba. Separa hechos comprobados, inferencias, recomendaciones y controles externos pendientes. Entrega una copia revisada, un informe de auditoría y una matriz de cambios; no declares aprobación VIU, Turnitin ni aptitud para depósito sin evidencia externa real.
```

## Secuencia sugerida

1. Auditar estructura y coherencia con la matriz V4.
2. Verificar afirmaciones cuantitativas contra fuentes y tablas.
3. Revisar metodología y límites del alcance.
4. Revisar discusión y conclusiones sin introducir datos nuevos.
5. Revisar citas y referencias.
6. Aplicar correcciones editoriales localizadas.
7. Actualizar campos en Word y exportar PDF.
8. Inspeccionar visualmente cada página y registrar resultados.

## Condición de salida

La revisión queda lista para el tutor cuando el nuevo documento abre correctamente, conserva objetivos y evidencia, no contiene contradicciones materiales, mantiene citas trazables y cuenta con un informe que declara con honestidad las limitaciones y controles externos pendientes.
