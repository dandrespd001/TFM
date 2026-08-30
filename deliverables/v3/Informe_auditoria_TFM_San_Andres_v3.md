# Informe de auditoría integral — TFM San Andrés (V3)

**Documento auditado:** `TFM_San_Andres_APA_VIU_Diomar_Andres_Pacheco_D_FINAL_V3.docx`  
**PDF de control:** `TFM_San_Andres_APA_VIU_Diomar_Andres_Pacheco_D_FINAL_V3.pdf`  
**Fecha:** 30 de agosto de 2026  
**Veredicto:** **LISTO_PARA_REVISION_VIU**. El manuscrito supera los controles académicos, matemáticos, bibliográficos, formales y visuales definidos para la V3. El depósito definitivo continúa condicionado a las acciones personales del autor indicadas en la sección 10.

## 1. Alcance y jerarquía aplicada

La revisión respetó la jerarquía acordada: la plantilla y las guías institucionales de la VIU gobiernan la forma; el borrador V1 revisado gobierna la primera parte hasta el marco teórico; la V2 y sus archivos reproducibles gobiernan metodología, escenarios y resultados; y las fuentes científicas u oficiales verificadas sustentan la ampliación. La V2 no se sobrescribió. Su SHA-256 permanece en `BEE726BF2481D6FA47189705F2271EF4CD021522B33B091177E16203FDF0509C`, y la plantilla VIU conserva `6C38C3777B39626A9DF6E4D846D12B12531460C41438A6FFD60C2BF7A8C9B8A5`.

La edición no aplicó una normalización global destructiva. Se conservaron las secciones, numeración, portada, encabezados, pies, campos y estilos institucionales, y se realizaron cambios localizados mediante OOXML y Microsoft Word. La exportación definitiva se efectuó con Word.

## 2. Resultado cuantitativo

| Indicador | V2 | V3 final | Resultado |
|---|---:|---:|---|
| Palabras extraídas del DOCX | 16.703 | 22.084 | +5.381 palabras sustantivas |
| Páginas totales Word/PDF | 63–65 según la auditoría anterior | 84 | Conforme |
| Páginas antes de anexos | ≈61 en V2 | 82 | Conforme al objetivo 82–85 |
| Anexos | 2–4 según repaginación V2 | 2 | 2,38 % del total; inferior al 10 % |
| Referencias | 27 | 42 | Dentro del objetivo 40–45 |
| Citas Zotero dinámicas | 32 | 53 | 42 claves únicas; cero huérfanas |
| Ecuaciones OMML | 10 | 19 | Dentro del objetivo 18–20 |
| Figuras | 2 | 6 | Cuatro capturas nuevas |
| Tablas científicas | 17 | 17 | Conservadas y corregidas |
| Filas de la matriz de afirmaciones | 82 | 166 | Cobertura ampliada |
| Resumen / abstract | 257 / 255 palabras | 287 / 290 palabras | Ambos entre 200 y 300 |

## 3. Contenido y coherencia académica

Los cinco objetivos específicos aprobados se conservaron literalmente y el objetivo general se mantuvo sin alteración sustantiva. La Tabla 1 vincula cada objetivo con actividad, evidencia y producto. La discusión y la Tabla 15 cierran la misma cadena: OE1 con los dos modelos base; OE2 con la revisión bibliográfica y el alcance estacionario; OE3 con los 18 escenarios FV; OE4 con las contingencias N-1; y OE5 con los cuatro puntos BESS y la sensibilidad energética.

La ampliación desarrolla el contexto insular, la capacidad de acogida, la influencia de la localización, la incertidumbre de GMD, el control de microrredes, la baja inercia, los inversores formadores de red, la diferencia potencia–energía del BESS y el papel comparativo de IEEE 1547, 1547.9 y 2030.7. Los estándares IEEE se presentan como orientación técnica internacional, no como normativa obligatoria colombiana.

La discusión diferencia coincidencia conceptual y comparación numérica. No traslada valores de redes ajenas a San Andrés. También separa repetibilidad numérica, validez del modelo y transferibilidad al sistema real. Las conclusiones no introducen resultados nuevos y distinguen aportaciones, limitaciones y trabajo posterior.

No se afirma que PowerWorld haya realizado dinámica, frecuencia, optimización, despacho cronológico, coordinación de protecciones o dimensionamiento comercial. El alcance demostrado continúa siendo flujo AC estacionario y contingencias deterministas. El BESS se interpreta como inyección PQ con Q=0, sin atribuirle formación de red ni continuidad de isla.

## 4. Auditoría matemática y de resultados

Las diez ecuaciones originales se conservaron y se añadieron nueve ecuaciones nativas. El conjunto cubre balance nodal complejo, desbalances, actualización Newton–Raphson, convergencia, pérdidas, utilización térmica, sensibilidad, potencia aparente del convertidor y restricciones P–Q. Cada expresión se acompaña de propósito, variables, unidades, aplicación y límite de interpretación.

Se recalcularon y contrastaron los bloques materiales:

- penetraciones FV de 5,138298; 10,276596 y 17,127660 MW a partir de 34,255320 MW;
- parámetros por unidad con base de 100 MVA y 34,5 kV;
- márgenes respecto de 0,95 p.u. para los cuatro casos BESS;
- energía nominal mediante `E = P·t/(0,93·0,80)` para ocho sensibilidades;
- 18 escenarios FV, cuatro configuraciones BESS y 40 contingencias BESS;
- clasificación separada de tensión, utilización térmica, isla, carga no servida y convergencia.

La matriz V3 contiene 166 afirmaciones. Todas incluyen sección, valor, unidad, forma mostrada, archivo fuente, campo de origen, transformación, redondeo y estado. Sus cuatro archivos de procedencia existen y permanecen en el paquete: `audit_fv_results.json`, `casos_v2_validacion.json`, `matriz_resultados_bess_v23.csv` y `energia_bess.csv`.

## 5. Figuras, tablas y accesibilidad

Las cuatro capturas de `Imagenes simulacion_1p2192` se insertaron como Figuras 3–6 independientes: estado base, apertura de un circuito Punta Evans–El Bight, apertura Punta Evans–SchoolHouse y apertura El Bight–SchoolHouse. Cada figura tiene mención previa, número, título, nota de elaboración propia a partir de PowerWorld, texto alternativo científico y análisis posterior. Los porcentajes de interfaz se tratan como observaciones redondeadas; las decisiones numéricas se remiten a los CSV.

Las Tablas 10–12 fueron recompuestas sin reducir el texto por debajo de 10 puntos. La inspección del PDF confirma que `No cumple`, `Barra`, los márgenes, `SchoolHouse` y `Resueltas` ya no quedan partidos de manera problemática. Las 37 tablas OOXML —incluidas las 19 tablas de disposición de ecuaciones— conservan encabezado repetible. Los siete objetos gráficos del cuerpo tienen descripción o función decorativa; no hay imágenes sin texto alternativo.

## 6. Zotero y bibliografía

Se incorporaron 15 fuentes verificadas a la biblioteca local de Zotero, elevando el inventario a 42. Entre ellas se encuentran el *Research Roadmap on Grid-Forming Inverters* de NREL; Dubey et al. y Ding y Mather sobre capacidad de acogida; Torquato et al.; Ismael et al.; Bollen y Rönnberg; Lasseter; Guerrero et al.; Rocabert et al.; Parhizi et al.; Ulbig et al.; Kenyon et al.; IEEE 1547-2018; IEEE 1547.9-2022; e IEEE 2030.7.

Las tres resoluciones CREG que todavía eran narrativas, el documento UPME y los dos manuales PowerWorld se enlazaron dinámicamente. Tras el ajuste, las 42 referencias tienen al menos una cita y las 53 ocurrencias contienen claves Zotero válidas. La bibliografía conserva 42 párrafos, un campo `ZOTERO_BIBL`, sangría francesa, cursivas y orden alfabético.

La prueba definitiva se ejecutó en Microsoft Word con Zotero Desktop 10.0.1. `Refresh` terminó sin error. Ante el aviso de lentitud se eligió **No**, por lo que no se deshabilitaron las actualizaciones automáticas. Word guardó el documento; la comprobación posterior encontró 53 campos de cita, 42 claves únicas, 42 entradas y un campo bibliográfico. La preferencia documental quedó fijada en APA 7 y `es-ES`. En coherencia con el estilo APA oficial de Zotero, las citas parentéticas de dos autores emplean `&`; la conjunción «y» se reserva para las citas narrativas. La guía VIU exige citar ambos autores, pero no presenta un ejemplo parentético que contradiga esta salida dinámica.

## 7. Formato VIU e integridad del archivo

El cuerpo mantiene A4, márgenes de aproximadamente 3 cm, Arial 12, interlineado 1,5 y justificación. La portada conserva su sección específica de plantilla. Los índices de contenido, tablas y figuras se actualizaron, al igual que `SEQ`, `REF`, `PAGEREF`, `PAGE` y `NUMPAGES`.

La inspección OOXML no detectó revisiones, eliminaciones, comentarios, texto oculto ni resaltado residual. Todos los objetos gráficos tienen alternativa textual o marca decorativa. Los metadatos quedaron corregidos: autor y último modificador se identifican como Diomar Andrés Pacheco Durán y el campo de empresa se dejó vacío.

## 8. Revisión del informe de auditoría V2

| Hallazgo V2 | Evaluación | Estado V3 |
|---|---|---|
| P1, cinco fuentes jurídicas sin cita dinámica | Correcto en lo esencial | Resuelto; las fuentes jurídicas y las restantes referencias tienen campos dinámicos |
| P2, cortes en Tablas 10–12 | Correcto | Resuelto y verificado visualmente |
| P3, porcentajes con seis decimales en prosa | Correcto | Resuelto mediante redondeo narrativo consistente |
| P4, cifras materiales sin fila de trazabilidad | Correcto | Resuelto; matriz ampliada de 82 a 166 filas |
| P5, extensión en el límite inferior | Correcto | Resuelto; 82 páginas antes de anexos |
| P6, campos e índices desactualizados | Correcto | Resuelto en Word |
| P7, `&` en citas parentéticas españolas | Parcialmente correcto | Aclarado: APA 7/Zotero conserva `&` en citas parentéticas; se verificó `es-ES` y «y» en la construcción narrativa |
| P8, metadatos del archivo | Correcto | Resuelto en `core.xml` y `app.xml` |
| P9, elementos propios de la plantilla | Correcto | Conservados |

La afirmación del preflight V2 según la cual faltaban `casos_v2_validacion.json`, `audit_fv_results.json`, tablas CSV, plantilla VIU y biblioteca bibliográfica partía de un contexto incompleto: esos archivos sí estaban disponibles en el proyecto o en la biblioteca local y se utilizaron en esta auditoría. No se considera un error científico del manuscrito, sino una limitación de acceso de la auditoría anterior.

## 9. Revisión visual del PDF

El PDF final de Word tiene 84 páginas. El encabezado real `Anexos` comienza en la página 83; por tanto, existen 82 páginas antes de anexos. Se renderizaron las 84 páginas a imagen y se inspeccionaron en diez hojas de contacto. La primera pasada detectó una página 57 casi vacía causada por un cierre de párrafo antes del salto a Discusión; se añadió análisis sustantivo de las cuatro topologías y se volvió a exportar. La versión final no presenta páginas vacías indebidas, superposiciones, recortes, tablas desbordadas ni figuras ilegibles.

El acta `acta_revision_visual_v3.csv` registra las 84 páginas como `APROBADA` con una observación por página o bloque funcional.

## 10. Limitaciones y acciones exclusivas del autor

La V3 queda lista para revisión académica de tutor o tribunal, no para afirmar validación operativa. Antes del depósito el autor debe:

1. sustituir el marcador de DNI por el dato real;
2. ejecutar Turnitin y conservar evidencia del porcentaje exigido por la VIU;
3. adjuntar formularios y documentación institucional de depósito;
4. confirmar con el tutor cualquier criterio particular de portada, convocatoria o extensión que no conste en la plantilla;
5. si se pretende una recomendación de ingeniería, obtener datos del operador y ejecutar perfiles horarios, dinámica, protecciones, control P–Q y evaluación económica.

Estas acciones no se completaron con datos supuestos. No afectan el veredicto **LISTO_PARA_REVISION_VIU**, pero sí condicionan el depósito definitivo y cualquier aplicación técnica real.
