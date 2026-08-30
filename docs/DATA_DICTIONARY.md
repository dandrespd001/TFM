# Diccionario mínimo de datos

## Unidades

| Campo o sufijo | Significado |
|---|---|
| `MW` | Potencia activa |
| `MVAr` / `Mvar` | Potencia reactiva |
| `MVA` | Potencia aparente o desbalance |
| `kV` | Tensión nominal o calculada |
| `pu` | Magnitud en por unidad |
| `pct` | Porcentaje |
| `deg` | Ángulo en grados |
| `gmd_m` | Separación media geométrica en metros |

## Parámetros

`registro_parametros.csv` usa `objeto`, `clave`, `campo`, `unidad`, `valor_historico`, `valor_v2`, `clase_evidencia`, `fuente` y `motivo`.

## Resultados FV

`tabla_resultados_por_escenario.csv` resume ubicación y penetración FV, tensión mínima, pérdidas, cargabilidad, contingencia gobernante, número de contingencias procesadas y criterios de tensión/térmico. `clase_dato=SIM` identifica resultados simulados.

## Resultados BESS

`resultados_bess_por_contingencia.csv` incluye barra y potencia BESS, estado de procesamiento/solución, islas, tensión mínima de barras energizadas, margen a 0,95 pu, cargabilidad máxima y rutas AUX de evidencia.

Los decimales en CSV usan punto o, en exportaciones directas de PowerWorld, coma dentro de campos entrecomillados. No convertirlos sin identificar el formato de origen.
