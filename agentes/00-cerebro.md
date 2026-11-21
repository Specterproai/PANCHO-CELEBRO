# 00-cerebro

- Empresa: todas
- Skill: —
- Cuándo: Diario 7:31
- Conectores: Claude Docs (panel), Gmail y Calendar (lectura, si están)

## Objetivo
Informe de la mañana de Pancho y sincronizar el panel de aprobaciones.

## Pasos
1. Lee el doc "Panel de Pancho · Informe y aprobaciones" (Claude Docs, id `bbf7fce6-d9a3-4a45-adca-70dea1f0eba3`). Las casillas que Pancho marcó en "Pendiente de aprobar" → márcalas [x] en `salidas/pendiente-de-aprobar.md` y muévelas en el doc a "Aprobado" con la fecha.
2. Lee las salidas de las últimas 24 h en `salidas/` de todas las empresas.
3. Si Calendar está conectado, lista las reuniones de hoy.
4. Reescribe la sección "Informe de hoy" del doc (una pantalla): lo más importante hoy, una línea por empresa, alertas (agentes que no dejaron salida o fallaron).
5. Añade a "Pendiente de aprobar" del doc las líneas nuevas sin marcar de `salidas/pendiente-de-aprobar.md`, cada una con su ruta. Borra la línea de ejemplo si sigue ahí.
6. Guarda también el informe en `salidas/cerebro/AAAA-MM-DD-informe.md`.

## Entrega
- Doc actualizado + informe en el repo.
- Commit y push al terminar.
