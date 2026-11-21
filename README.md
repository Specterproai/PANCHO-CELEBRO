# PANCHO-CELEBRO — el cerebro de todas las empresas de Pancho

Este repositorio es la cabeza pensante de Claude para **Cascade, Klasse, LexLegal, Specter y la marca personal (Empresarios de Éxito)**. Cada tarea programada en la nube clona este repo, lee sus reglas y skills, hace su trabajo y deja el resultado aquí.

## Estructura
| Carpeta | Qué hay |
| --- | --- |
| `CLAUDE.md` | Reglas para todos los agentes (se carga solo en cada sesión) |
| `empresas/<empresa>/contexto.md` | Qué es cada empresa, oferta, público, tono, datos pendientes `[DATO]` |
| `agentes/NN-nombre.md` | Ficha de cada uno de los 21 agentes: objetivo, pasos, horario, entrega |
| `.claude/skills/` | 88 skills de marketing, comercial, ventas y seguridad |
| `.claude/settings.json` + `.claude/hooks/` | Guardia SkillSpector: escanea cualquier repo antes de instalarlo |
| `scripts/setup-nube.sh` | Instala SkillSpector en el entorno en la nube |
| `salidas/` | Lo que producen los agentes + `pendiente-de-aprobar.md` |
| `SEGURIDAD.md` | Resultado del escaneo de los skills y qué se descartó |

## Skills incluidos
- **Propios:** `equipo-marketing`, `equipo-comercial`, `equipo-ventas`.
- **Seguridad (NVIDIA):** `skill-inspector` + guardia automático con SkillSpector.
- **Oficiales de Anthropic** ([knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins), Apache-2.0): marketing (brand-review, campaign-plan, competitive-brief, content-creation, draft-content, email-sequence, performance-report, seo-audit) y ventas (36 skills: call-prep, draft-outreach, lead-triage, pipeline-review, forecast…).
- **Marketing de terceros** ([coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)): 40 skills que pasaron el escaneo con riesgo bajo (copywriting, cro, social, video, launch, pricing, offers, lead-magnets…).

Licencias de terceros en `.claude/skills/_licencias/`.

## Cómo lanzar un agente en la nube
Escritorio → **Código → Programadas → Nueva tarea → Nube** (o claude.ai/code/routines):
- Repositorio: `Specterproai/pancho-celebro`
- Entorno: uno con `scripts/setup-nube.sh` como script de arranque
- Instrucciones: `Eres el agente NN. Lee CLAUDE.md y agentes/NN-nombre.md y ejecútalo.`
- Horario: el de la ficha. Conectores: solo los que pide la ficha.
