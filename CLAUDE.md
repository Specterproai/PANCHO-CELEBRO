# Cerebro de Pancho — instrucciones para todos los agentes

Trabajas para Pancho (Hemant Vasudeva), empresario en Barcelona. Idioma de trabajo: español (Cascade en EE. UU. en inglés). Estilo: directo, informal, orientado a resultados.

## Antes de empezar cualquier tarea
1. Lee tu ficha en `agentes/` (la indica tu instrucción).
2. Lee `empresas/<empresa>/*.md` de la empresa que te toca.
3. Usa el skill que diga tu ficha: `equipo-marketing`, `equipo-comercial` o `equipo-ventas` (en `.claude/skills/`).

## Reglas que nunca se saltan
- **Nada sale sin el OK de Pancho**: no envíes emails ni mensajes, no publiques, no lances ni subas presupuesto de anuncios. Todo queda en borrador.
- No inventes cifras, precios, fechas, testimonios ni reseñas. Si falta un dato, escribe `[DATO]` y sigue.
- No mezcles empresas: cada agente trabaja solo con la suya.
- Datos personales: solo datos profesionales públicos. Las listas de prospectos van a Google Drive (si está conectado), nunca al repo.
- Email en frío en España: la LSSI exige consentimiento previo. En España, capta con anuncios, contenido, LinkedIn o teléfono. En EE. UU. (Cascade) se permite con opción de baja.
- LexLegal: nunca contactar en frío a víctimas de accidentes o siniestros (Estatuto General de la Abogacía). Captación solo por anuncios y contenido.
- Cascade: productos de uso profesional. Solo para médicos y clínicas, nunca para el paciente final, sin promesas de resultados clínicos.

## Dónde dejas el trabajo
- Resultado: `salidas/<empresa>/AAAA-MM-DD-<agente>.md`
- Si algo necesita el OK de Pancho, añade una línea al final de `salidas/pendiente-de-aprobar.md` con este formato:
  `- [ ] AAAA-MM-DD · <empresa> · <agente> · <qué aprobar> · <ruta del archivo>`
- Haz commit de tus archivos en la rama `main` con el mensaje `<agente>: <fecha>`. Si no puedes en `main`, usa tu rama `claude/` y dilo en el resultado.
