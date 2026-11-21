#!/usr/bin/env python3
"""Guardia SkillSpector: escanea cualquier repo de GitHub antes de que entre.

Hook PreToolUse (matcher "Bash"). Solo actúa en comandos que instalan código:
git clone, gh repo clone, npx skills add, claude mcp add, pip install git+,
uv tool install git+, y curl/wget enviados a sh o bash. Todo lo demás pasa.

LOW -> pasa en silencio. MEDIUM -> pasa con aviso.
HIGH/CRITICAL -> se bloquea (las tareas en la nube corren sin nadie delante).
Si el escaneo falla o tarda demasiado, deja pasar pero avisa de que NO se revisó.
"""
import json, re, shutil, subprocess, sys

TRIGGERS = [
    r"\bgit\s+clone\b", r"\bgh\s+repo\s+clone\b", r"\bnpx\s+skills\s+add\b",
    r"\bclaude\s+mcp\s+add\b", r"\bpip3?\s+install\s+[^|;&]*git\+",
    r"\buv\s+tool\s+install\s+[^|;&]*git\+", r"\b(curl|wget)\b[^|]*\|\s*(sudo\s+)?(ba)?sh\b",
]
REPO_URL = re.compile(r"https?://github\.com/[\w.-]+/[\w.-]+")
SHORT = re.compile(r"(?:gh\s+repo\s+clone|npx\s+skills\s+add)\s+([\w.-]+/[\w.-]+)")


def out(decision=None, reason=None, context=None):
    hso = {"hookEventName": "PreToolUse"}
    if decision:
        hso["permissionDecision"] = decision
        hso["permissionDecisionReason"] = reason or ""
    if context:
        hso["additionalContext"] = context
    print(json.dumps({"hookSpecificOutput": hso}))
    sys.exit(0)


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)
    cmd = (data.get("tool_input") or {}).get("command", "") or ""
    if not any(re.search(t, cmd) for t in TRIGGERS):
        sys.exit(0)

    urls = REPO_URL.findall(cmd)
    urls += ["https://github.com/" + s for s in SHORT.findall(cmd) if "://" not in s]
    urls = [u[:-4] if u.endswith(".git") else u for u in urls]
    if not urls:
        out(context="Guardia SkillSpector: comando de instalación sin repo de GitHub reconocible. NO se revisó; extrema la precaución.")

    if not shutil.which("skillspector"):
        out(context="Guardia SkillSpector: skillspector no está instalado en este entorno. El repo NO se revisó. Ejecuta scripts/setup-nube.sh.")

    findings = []
    for url in dict.fromkeys(urls):
        try:
            r = subprocess.run(["skillspector", "scan", url, "--no-llm", "-f", "json"],
                               capture_output=True, text=True, timeout=110)
            rep = json.loads(r.stdout)
        except Exception as e:
            out(context=f"Guardia SkillSpector: el escaneo de {url} falló o no terminó a tiempo ({type(e).__name__}). Ese repo NO se revisó.")
        ra = rep.get("risk_assessment", {})
        sev = str(ra.get("severity", "")).upper()
        score = ra.get("score")
        issues = sorted(rep.get("issues", []),
                        key=lambda i: ["CRITICAL", "HIGH", "MEDIUM", "LOW"].index(str(i.get("severity", "LOW")).upper())
                        if str(i.get("severity", "LOW")).upper() in ["CRITICAL", "HIGH", "MEDIUM", "LOW"] else 9)
        top = "; ".join(f"{i.get('severity')} {i.get('rule_id') or i.get('id') or ''} {(i.get('title') or i.get('message') or '')[:80]}".strip()
                        for i in issues[:3])
        findings.append((url, sev, score, top))

    worst = max(findings, key=lambda f: ["LOW", "MEDIUM", "HIGH", "CRITICAL"].index(f[1]) if f[1] in ["LOW", "MEDIUM", "HIGH", "CRITICAL"] else 0)
    url, sev, score, top = worst
    if sev in ("HIGH", "CRITICAL"):
        out("deny", f"SkillSpector bloqueó {url}: riesgo {sev} (score {score}). Hallazgos: {top}. Pide a Pancho que lo revise.")
    if sev == "MEDIUM":
        out(context=f"Guardia SkillSpector: {url} riesgo MEDIUM (score {score}). Hallazgos: {top}. Avísalo en tu resultado.")
    sys.exit(0)


if __name__ == "__main__":
    main()
