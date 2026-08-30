# Informe de auditoría final — TFM San Andrés (v2)

**Documento auditado:** `TFM_San_Andres_APA_VIU_Diomar_Andres_Pacheco_D_FINAL_V2.docx` (maestro, sin modificar)
**Fecha de auditoría:** 2026-08-30
**Veredicto global:** **REQUIERE CORRECCIÓN MENOR → LISTO_PARA_CIERRE_DEL_AUTOR** tras aplicar los ajustes localizados indicados. No se declara APTO_PARA_ENTREGA: faltan DNI real, Turnitin <20 %, actualización de campos y exportación PDF desde Microsoft Word, e inspección del PDF definitivo (G12).

---

## 1. Preflight

**Archivos recibidos:** DOCX maestro; SPEC/PLAN/TASKS/GATES v3; matriz de afirmaciones (82 filas); energia_bess.csv (8); matriz_resultados_bess_v23.csv (4); matriz_resultados_bess.csv (4); resultados_bess_por_contingencia.csv (40); consolidado_bess_final.xlsx (7 hojas, consistente con los CSV).

**Fuentes ausentes (limitan verificación):** `casos_v2_validacion.json`, `audit_fv_results.json`, `tabla_estado_base_v2.csv`, `tabla_resultados_por_escenario.csv`, la plantilla VIU oficial y la biblioteca Zotero (.bib/CSL del proyecto). Las cifras que solo existen en esas fuentes (p. ej. DG 34,24/34,26 MW, pérdidas FV por escenario) se verificaron por consistencia interna, no contra el archivo primario.

**Contradicciones entre fuentes recibidas:** ninguna. El XLSX consolidado coincide con los CSV v2.

**Qué NO se hizo (por seguridad):** no se reconstruyó el DOCX, no se tocó ningún campo (Zotero, TOC, SEQ, REF), no se ejecutó Zotero Refresh ni Ctrl+A/F9 (requieren Word + Zotero del autor).

---

## 2. Verificaciones SUPERADAS (con evidencia)

| # | Criterio | Resultado |
|---|----------|-----------|
| 1 | Objetivos literales (1 general + 5 específicos) | Coinciden carácter a carácter con los aprobados, incluida puntuación |
| 2 | Valores v1 prohibidos (0,939222; 9,119585771; 4,519756455; 13,8 kV; "BESS no simulado"; "P_BESS > 10 MW") | 0 apariciones en todo el documento |
| 3 | Dos casos base GMD | Tabla 9: 0,95511 p.u./0,010 MVA (0,9144 m) y 0,95489 p.u./0,000 MVA (1,2192 m) ✓ vs. matriz |
| 4 | 18 escenarios FV (Tabla 10) | Las 18 filas coinciden con la matriz de afirmaciones (P, Vmin, carga máx.); el escenario 1p2192_B1_FV30 figura como NR ✓ |
| 5 | 4 casos BESS (Tabla 11) | Vmin, márgenes y cargas coinciden con matriz_resultados_bess_v23.csv a 6 decimales |
| 6 | 40/40 contingencias BESS | Tabla 12 coincide con resultados_bess_por_contingencia.csv (resueltas, violaciones, isla 13,06 MW) |
| 7 | 8 sensibilidades energéticas (Tabla 13) | Recalculadas con E_nom = P·t/(0,93·0,80): las 8 coinciden con tolerancia <1×10⁻⁸ MWh |
| 8 | Matemática de red | Z_base = 11,9025 Ω ✓; las 8 filas R/X de la Tabla 4 recalculadas ✓; penetraciones 5,138298/10,276596/17,127660 MW ✓; márgenes y diferencias citados en prosa (0,007044; 0,011349; 0,000175; 0,000344; etc.) ✓ |
| 9 | Interpretación 5,25 MW | Todas las apariciones de "potencia mínima/óptima/umbral" son negaciones explícitas (p. ej. §5.6, §6.3, conclusiones OE5). Uso conforme |
| 10 | Isla SchoolHouse | Clasificada como isla/carga no servida de 13,06 MW; excluida del mínimo energizado; sin atribuir energización al BESS PQ ✓ |
| 11 | Resumen/Abstract | 257 y 255 palabras (rango 200–300) ✓; 5 palabras clave y 5 keywords ✓ |
| 12 | Referencias | 27 entradas; PowerWorld s. f.-a / s. f.-b ✓; CREG-058 como informe ✓; CREG 2009 sin sufijos a/b innecesarios (las dos fuentes 2009 tienen cadenas de autor distintas) ✓; formato legal para leyes/resoluciones ✓; alineación izquierda + sangría francesa ✓; sin justificar ✓ |
| 13 | Campos dinámicos | 32 CSL_CITATION + 1 bibliografía ZOTERO_BIBL; 3 TOC; 17 SEQ Tabla + 2 SEQ Figura; 17 REF cruzadas. Nada convertido a texto plano |
| 14 | Ecuaciones | 10 OMML nativas con Cambria Math y numeración (1)–(10) alineada a la derecha |
| 15 | Formato | A4; cuerpo 3 cm los 4 márgenes (la portada conserva geometría especial de plantilla); Normal = Arial 12, interlineado 1,5, justificado; tablas a 10 pt; las 28 tablas con encabezado repetible; sin rellenos de color (monocromas); 0 subrayados; 0 texto oculto; 0 revisiones; 0 comentarios; 0 resaltados |
| 16 | Accesibilidad | Figuras 1 y 2 con texto alternativo científico; logotipo VIU marcado como decorativo |
| 17 | Menciones previas | Las 17 tablas y 2 figuras se mencionan individualmente antes de aparecer |
| 18 | Marcador DNI | Presente como "[PENDIENTE DEL AUTOR]", sin valor inventado |
| 19 | Formulación normativa | "criterio contractual de calidad documentado para el ASE en 2009" y sin afirmación de vigencia regulatoria actual ✓ |
| 20 | Pie de página | "Página X de Y" con campos PAGE/NUMPAGES; portada sin número |

---

## 3. PROBLEMAS DETECTADOS y cómo solucionarlos

### P1 — CRÍTICO (G7 / Zotero): las 5 normas legales no tienen cita Zotero
Las 22 referencias no legales (incluido CREG-058) se citan mediante campos `CSL_CITATION`, pero **Ley 1715/2014, Ley 2099/2021, Resolución CREG 018/2003, Resolución CREG 068/2009 y Resolución CREG 091/2007 solo aparecen como texto narrativo plano** (§3.2, §3.7, §6.8). La bibliografía es un campo dinámico ZOTERO_BIBL que solo conserva lo citado con Zotero: **al ejecutar Zotero Refresh esas 5 entradas desaparecerían de la bibliografía** (o ya fueron editadas a mano, lo que es igual de frágil).
**Solución (Word + Zotero del autor):** insertar `Add/Edit Citation` en cada mención narrativa (se puede suprimir el autor para conservar la forma narrativa, p. ej. "La Resolución CREG 018 de 2003 (…)"), verificar que la bibliografía siga mostrando 27 entradas tras Refresh y que las leyes conserven el formato legal VIU vía metadatos/CSL del proyecto. No corregir la bibliografía a mano.

### P2 — ALTO (maquetación, REQ-WORD-007): palabras y cifras partidas en tablas
Verificado en render a tamaño real:
- **Tabla 10 (pág. ~34-36):** "NO_CUMPLE" se parte como "NO_CU/MPLE" y el encabezado "Barra" como "Barr/a".
- **Tabla 11 (pág. ~39-40):** los márgenes se parten ("0,00032/1", "0,00041/8", "0,00066/3", "0,00007/4") y "SchoolHouse" se parte como "Sch/oolHouse" en la columna de contingencia.
- **Tabla 12 (pág. ~42):** el encabezado "Resueltas" se parte como "Resuelt/as".
**Solución (localizada, segura):**
1. Tabla 10: sustituir `NO_CUMPLE`/`CUMPLE` por `No cumple`/`Cumple` (además unifica criterio editorial con la Tabla 11, que ya los usa).
2. Tablas 11 y 12: ensanchar las columnas Margen/Contingencia/Resueltas a costa de las columnas sobrantes (GMD, Caso), o abreviar la contingencia como "L1 PE–SH" con nota al pie de tabla. No reducir el cuerpo por debajo de 10 pt.
3. Volver a renderizar esas tres páginas y confirmar que no queda ninguna cifra ni palabra partida.

### P3 — MEDIO (REQ-QA-003 / redondeo): porcentajes con 6 decimales en prosa
§5.3 (pág. ~36): "…conservan 0,937519 p.u. y **91,367287 %**…" y "…0,937064 p.u. y **91,400468 %**". La matriz de afirmaciones fija para esas cifras la forma mostrada "91,37 %" y "91,40 %" (2 decimales). El propio §6.12 dice que dos o tres decimales bastan en la narrativa.
**Solución:** reemplazar por "91,37 %" y "91,40 %" en esa frase. Es la única desviación de redondeo detectada.

### P4 — MEDIO (trazabilidad, REQ-DAT-007): cifras publicadas sin fila en la matriz
La matriz no cubre: DG del estado base (34,24/34,26 MW; 7,32/7,36 MVAr), Vmin y carga del estado inicial BESS (0,96259–0,96373 p.u.; 48,014–53,181 %), pérdidas iniciales BESS (0,485/0,654 MW) y las pérdidas FV por escenario de la Tabla 10 (0,931; 0,677; 0,290; …). Son consistentes con los CSV, pero rompen la regla "cada cifra publicada tiene fila en la matriz".
**Solución:** añadir esas filas a `matriz_afirmaciones_finales.csv` (fuente: matriz_resultados_bess_v23.csv / tabla_resultados_por_escenario.csv) o añadir una nota de alcance en el anexo 9.2 declarando qué bloques cubre la matriz.

### P5 — MEDIO (G9): extensión en el límite inferior
Word registró 63 páginas en el último guardado; LibreOffice repagina a 65. El TOC indica Anexos en pág. 62 → cuerpo sin anexos ≈ 61 páginas (cómputo VIU completo) o ≈ 53 si se contara desde Introducción. El requisito es 60–100 sin anexos.
**Solución (autor, en Word):** tras F9 y Zotero Refresh, verificar el criterio de cómputo de la VIU y la paginación real. Si el cómputo excluye preliminares, el documento estaría bajo el mínimo y habría que valorar ampliar discusión/anexos con el tutor. Anexos = 2-4 páginas (<10 % ✓).

### P6 — BAJO: campos e índices desactualizados
El TOC muestra 63 páginas pero el documento repagina a 65; los campos no se actualizaron tras la última edición. **Solución (autor, en Word):** Zotero Refresh → Ctrl+A → F9 → guardar, cerrar, reabrir, y solo entonces exportar el PDF definitivo.

### P7 — BAJO (editorial): "&" en citas parentéticas en español
El CSL de Zotero genera "(UPME & IDEAM, 2005; …)". APA 7 en español usa habitualmente "y". **No editar a mano** (se perdería con Refresh): verificar si el CSL aprobado por la VIU localiza el conector; si no, señalar la discrepancia al tutor.

### P8 — BAJO: metadatos del archivo
`lastModifiedBy` = "Diomar Adquio" (distinto de "Pacheco Durán") y `Company` = "Hewlett-Packard". Recomendable limpiar propiedades del documento antes del depósito (Archivo → Información → Propiedades).

### P9 — OBSERVACIÓN (sin acción): elementos de plantilla
Párrafos vacíos con estilo "Footer" en la portada y encabezado "Índice de figuras y gráficos" sin clase "Gráfico" propia: pertenecen a la plantilla VIU (autoridad máxima). No tocar.

---

## 4. Lista de cifras científicas verificadas contra CSV/matriz

- Base: 0,95511 / 0,95489 p.u.; 0,010 / 0,000 MVA ✓
- FV: 5,138298 / 10,276596 / 17,127660 MW ✓; las 18 filas de Vmin y carga máx. ✓; NR de 1p2192_B1_FV30 ✓
- BESS: 0,949679 / 0,950418 / 0,949337 / 0,950074 p.u.; márgenes −0,000321 / +0,000418 / −0,000663 / +0,000074 p.u.; cargas 62,70 / 83,09 / 62,71 / 83,09 % ✓
- Isla: 13,06 MW, gen. 0 / 5,25 MW ✓
- Energía: 6,720430 / 13,440860 / 26,881720 / 53,763441 / 3,528226 / 7,056452 / 14,112903 / 28,225806 MWh ✓ (recalculo independiente, tol. 1×10⁻⁸)
- Parámetros: R/X de las 8 filas de líneas ✓; Rate A 21,81085 MVA y 25 MVA ✓
- Diferencias derivadas citadas en prosa: 0,00022; 0,007044; 0,007122; 0,000854; 0,000869; 0,011349; 0,011497; 0,000175; 0,000023; 0,000363; 0,000831; 0,000506; 0,000344; ~5,1 % ✓
- No verificables contra archivo primario (no adjuntado), solo consistentes: DG 34,24–34,26 MW / 7,32–7,36 MVAr; pérdidas FV por escenario; 52,7 % IPSE 2023; 34,255320 MW de referencia (sí consta en SPEC v3 ✓).

## 5. Contradicciones o datos sin fuente

Ninguna contradicción real detectada entre objetivos, metodología, resultados, discusión y conclusiones. Datos sin fuente primaria adjunta: los listados en §4 (última línea). Ninguna cifra v1 en el documento activo.

## 6. Revisión de las 27 referencias

22/27 con citas dinámicas bidireccionales verificadas; 5/27 legales solo narrativas (ver P1). Cursivas de revistas presentes; orden alfabético correcto; DOI/URL presentes; sin fechas ni editoriales inventadas detectadas; duplicados: ninguno.

## 7. Páginas que necesitan inspección visual manual (tras F9 en Word)

1 (portada/DNI), 2-6 (índices), 7-8 (resumen/abstract), 17-18 y 24-26 (ecuaciones), 24-25 (Tabla 4), 33-36 (Tabla 10 y Figura 1), 39-42 (Tablas 11-12 y Figura 2), 55-57 (Tablas 14-15), 58-61 (referencias), 62-65 (anexos). Prioridad: las tres tablas de P2 y la paginación de P5.

## 8. Acciones exclusivas del autor (G12)

1. Insertar el DNI real en la portada.
2. Insertar citas Zotero para las 5 normas legales (P1) y ejecutar Zotero Refresh.
3. Ctrl+A → F9; verificar índices, referencias cruzadas y paginación (P5, P6).
4. Aplicar las correcciones de tablas P2-P3 (o autorizarme a aplicarlas en la copia).
5. Comprobar similitud con Turnitin (<20 %) y conservar evidencia.
6. Exportar el PDF solo desde Microsoft Word e inspeccionar el 100 % de páginas a tamaño real.
7. Completar la documentación de depósito.

**Estado final declarado:** LISTO_PARA_CIERRE_DEL_AUTOR (condicionado a P1–P3).
