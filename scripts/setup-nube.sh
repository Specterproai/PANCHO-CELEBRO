#!/usr/bin/env bash
# Script de arranque del entorno en la nube de Claude.
# Pégalo en: Entorno en la nube -> Setup script. Se ejecuta una vez y queda en caché.
set -e
if ! command -v uv >/dev/null 2>&1; then
  pip install -q uv --break-system-packages 2>/dev/null || pip install -q uv
fi
uv tool install -q git+https://github.com/NVIDIA/SkillSpector.git || true
export PATH="$HOME/.local/bin:$PATH"
skillspector --version || echo "AVISO: SkillSpector no se pudo instalar; el guardia avisará de que no revisa."
