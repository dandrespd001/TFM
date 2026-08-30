# Evidencia basal PowerWorld v2

Fecha de comprobación: 29 de agosto de 2026. Aplicación: PowerWorld Simulator 24 Evaluation.

## Caso GMD 0,9144 m

- Archivo: `Simulacion/Contingen/SA_AC_v2_GMD_0p9144m.pwb`.
- SHA-256 después de persistir las contingencias: `D94F78845DD75FC9DB6FE2E945FEC4FB807ABEEE298F0922082F7A3FCFAFE63D`.
- Barra slack: número 1, `PE_132`, 13,2 kV.
- Model Explorer > Islands: una fila; seis barras; `Solved = YES`; `Energized = YES`.
- Model Explorer > Mismatches: máximo visible 0,01 MVA.
- Tensiones p.u. visibles: B1 1,00000; B2 0,98924; B3 0,96769; B4 0,96559; B5 0,95977; B6 0,95511.
- Generación visible aproximada: 34,24 MW y 7,32 MVAr.

## Caso GMD 1,2192 m

- Archivo: `Simulacion/Contingen/SA_AC_v2_GMD_1p2192m.pwb`.
- SHA-256 después de corregir `Rate A`, retirar las reglas incompletas y guardar: `06595D18667B85EDA890C5898F168DE1A0CA39C052C66B0CA33C992D6859E7A0`.
- Barra slack: número 1, `PE_132`, 13,2 kV.
- Topología sin cambios respecto del caso anterior: una isla energizada de seis barras.
- Model Explorer > Mismatches: máximo visible 0,00 MVA.
- Tensiones p.u. visibles: B1 1,00000; B2 0,98919; B3 0,96750; B4 0,96537; B5 0,95958; B6 0,95489.
- Generación visible aproximada: 34,26 MW y 7,36 MVAr.

## Estado de Data Check

La pestaña `Define Checks` mostró inicialmente una única fila `None`: no existían reglas configuradas. Se ensayó la carga AUX de definiciones `SIM-*`. PowerWorld Evaluation 24 creó los nombres, pero no conservó de forma fiable las condiciones de los filtros avanzados; al seleccionar uno de los filtros incompletos también se observó `List index out of bounds (0)`. Las definiciones de prueba se retiraron mediante `reset_data_checks_sdd_v2.aux`.

La automatización de `Data Check` se clasifica por tanto como `NO VALIDADA`. Las correcciones del modelo, la solución y las contingencias sí funcionan. La aceptación de G2 se realizará provisionalmente mediante las tablas completas de buses, ramas y generadores, más Islands, Mismatches y Contingency Records, siguiendo la sección 7.2 de la guía. Por ello:

- `G3 — Solución` puede evaluarse con la evidencia anterior.
- `G2 — Parametrización` permanece pendiente hasta completar y guardar todas las tablas de evidencia manual o validar reglas reproducibles.
- Una pantalla vacía no se interpreta como ausencia de hallazgos.

## Round-trip AUX validado parcialmente

PowerWorld exportó la barra 1 mediante `Bus Information for Present > Save to Aux` en `Simulacion/Contingen/schema_bus_v2.aux`. La cabecera generada por la aplicación confirmó los campos `Number`, `Name`, `NomkV`, `Vpu`, `Vangle`, `Slack` y `Status`. El mismo archivo se cargó mediante `File > Load Auxiliary`; tras la importación se conservaron `PE_132`, 13,2 kV y las seis tensiones p.u.

El transformador 4–6 se inspeccionó en `Branch Information Dialog`: 34,5/13,2 kV, circuito 1, cerrado, `R=0,031841 p.u.`, `X=0,318412 p.u.` y `Limit A=25,000 MVA`. Su exportación AUX no se completó por un problema de entrada en el segundo diálogo de guardado, por lo que el esquema se clasifica como `partial_roundtrip`, no como validado.

## Sintaxis y piloto de contingencias

Se cargó `Simulacion/Contingen/n1_rama_v1.aux`, exportado previamente por PowerWorld. La sección `ContingencyElement` utiliza objetos `BRANCH <barra_origen> <barra_destino> <circuito>` con acción `OPEN` y estado de criterio `CHECK`. PowerWorld reconoció diez definiciones y diez elementos, todos referidos a ramas existentes, y el conjunto se guardó en los dos casos v2.

En `SA_AC_v2_GMD_1p2192m.pwb` se ejecutó un piloto basal con `Full Power Flow`. El Model Explorer mostró `Processed = YES` y `Solved = YES` en las diez filas; ninguna quedó omitida. El resumen confirmó diez acciones aplicadas y la restauración del estado inicial. `FallaTrafo1_SchoolHouse` aisló 13,06 MW de carga, por lo que deberá clasificarse como isla/carga no servida y no como tensión cero o solución corregida por un BESS PQ.

PowerWorld informó que no hubo violaciones ni contingencias irresolubles. Ese mensaje solo acredita que el lote terminó. El criterio 0,95–1,05 p.u. y la cargabilidad requieren la configuración de `Limit Monitoring` ya exportada o la comprobación tabular manual; los filtros avanzados de `Data Check` no se consideran evidencia hasta que cada condición sea visible en la interfaz.

## Límite de precisión

Los valores anteriores proceden de la interfaz visible y conservan la precisión presentada por PowerWorld. La campaña deberá exportar los campos mediante AUX/CSV para evitar transcripción manual.
