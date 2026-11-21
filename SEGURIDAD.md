# Seguridad de los skills

Todos los skills se escanearon con [NVIDIA SkillSpector](https://github.com/NVIDIA/SkillSpector) (análisis estático, `--no-llm`) el 21 nov 2026 antes de subirlos.

## Criterio
- **LOW** → instalado.
- **MEDIUM** → instalado solo si es de un editor oficial (Anthropic, NVIDIA). Los de terceros con MEDIUM se descartaron.
- **HIGH / CRITICAL** → descartado.

## Resultado
| Origen | Escaneados | Instalados | Descartados |
| --- | --- | --- | --- |
| Propios (equipo-marketing, comercial, ventas) | 3 | 3 (LOW) | 0 |
| Anthropic knowledge-work-plugins (marketing + ventas) | 44 | 44 (8 LOW, 36 MEDIUM oficiales) | 0 |
| NVIDIA skill-inspector | 1 | 1 (MEDIUM oficial) | 0 |
| coreyhaines31/marketingskills | 53 | 40 (LOW) | 13 |

Descartados de marketingskills:
- **CRITICAL** (no instalar): ad-creative, ads, attribution, conversion-tracking, marketing-loops, marketing-plan, reverse-engineer-marketing.
- **MEDIUM de terceros**: cold-email, directory-submissions, events, paywalls, prospecting.
- **Duplicado**: seo-audit (se usa el oficial de Anthropic).

Los hallazgos HIGH suelen venir de instrucciones que ejecutan comandos, llaman a APIs externas o piden credenciales. No implica que sean maliciosos, pero no se instalan sin revisión manual.

## Guardia automático
`.claude/settings.json` registra `.claude/hooks/skillspector-guard.py` como hook PreToolUse (Bash):
- Actúa solo en `git clone`, `gh repo clone`, `npx skills add`, `claude mcp add`, `pip install git+`, `uv tool install git+` y `curl/wget | sh`.
- LOW pasa · MEDIUM pasa con aviso · HIGH/CRITICAL se **bloquea**.
- Si el escaneo falla o tarda más de 110 s, deja pasar pero avisa de que el repo **no** se revisó.
- Necesita SkillSpector instalado: `scripts/setup-nube.sh` en el entorno en la nube.
