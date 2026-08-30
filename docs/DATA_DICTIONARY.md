# Diccionario de datos

## Convenciones generales

| Convención | Interpretación |
|---|---|
| `MW` | Potencia activa |
| `MVAr` o `Mvar` | Potencia reactiva |
| `MVA` | Potencia aparente o desbalance, según el campo |
| `kV` | Tensión nominal |
| `pu` | Magnitud en por unidad |
| `pct` / `%` | Porcentaje |
| `deg` | Ángulo eléctrico en grados |
| `m` | Distancia en metros, incluida la GMD |
| `YES/NO`, `CUMPLE/NO_CUMPLE` | Estado lógico o criterio evaluado |

Los decimales en CSV usan punto. El documento académico puede mostrarlos con coma por la convención española.

## `registro_parametros.csv`

| Campo | Descripción |
|---|---|
| `objeto` | Tipo de elemento de red |
| `clave` | Identificador del elemento |
| `campo` | Propiedad configurada |
| `unidad` | Unidad física o `text` |
| `valor_historico` | Valor previo o estado antes de V2 |
| `valor_v2` | Valor aplicado/registrado en V2 |
| `clase_evidencia` | `OBS`, `SPEC`, `PROXY`, `DER`, `HIP` o combinación |
| `fuente` | Documento, archivo o decisión de procedencia |
| `motivo` | Justificación del cambio o adopción |

## Matrices de afirmaciones

| Campo | Descripción |
|---|---|
| `claim_id` | Identificador estable de la afirmación |
| `seccion` | Sección o familia de resultados |
| `valor` | Valor numérico con precisión de cálculo |
| `unidad` | Unidad correspondiente |
| `valor_mostrado` | Redondeo usado en el TFM |
| `fuente` | Archivo o evidencia de origen |
| `campo_origen` | Variable extraída de la fuente |
| `transformacion` | Fórmula o regla aplicada |
| `redondeo` | Precisión de presentación |
| `estado` | Resultado del control de trazabilidad |

## Resultados por escenario FV

Campos principales de `tabla_resultados_por_escenario.csv`:

- `case_id`: identificador del caso.
- `gmd_m`: separación media geométrica considerada.
- `ubicacion_fv`, `penetracion_pct`, `fv_mw`: ubicación y magnitud FV.
- `v_min_base_pu`, `v_min_n1_pu`: tensión mínima en base y bajo N-1.
- `carga_max_n1_pct`: mayor cargabilidad bajo contingencia.
- `perdidas_base_mw`: pérdidas activas del caso base del escenario.
- `contingencia_gobernante`, `elemento_termico_gobernante`: condición o elemento limitante.
- `criterio_tension`, `criterio_termico`: evaluación según los umbrales adoptados.
- `clase_dato`: normalmente `SIM`.

## Resultados BESS por contingencia

Campos principales de `resultados_bess_por_contingencia.csv`:

- `bess_bus`, `bess_mw`: ubicación y potencia del BESS.
- `processed`, `solved`: si la contingencia fue procesada y resuelta.
- `island_status`, `islanded_load_mw`, `islanded_gen_mw`: información de isla.
- `v_min_energized_pu`: mínimo solo entre barras energizadas.
- `margin_to_0p95_pu`: diferencia respecto del umbral 0,95 pu.
- `max_loading_pct`: cargabilidad máxima.
- `evidence_bus_aux`, `evidence_branch_aux`: archivos AUX de respaldo.
- `data_class`: clase del dato, típicamente `SIM`.

## Resultados de ejecución V2

- `resultados_barras.csv`: esquema de resultados nodales; en la copia conservada solo contiene encabezado.
- `resultados_ramas.csv`: esquema de resultados de ramas; en la copia conservada solo contiene encabezado.
- `resultados_runs.csv`: esquema de resumen por corrida; en la copia conservada solo contiene encabezado.

La presencia del esquema no demuestra que existan filas de ejecución. Para los resultados disponibles use las carpetas FV/BESS y las tablas consolidadas.
