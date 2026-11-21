# 00-cerebro — Director

- Empresa: todas
- Cuándo: Diario 7:31 (después de los agentes de Inteligencia, que corren de 7:07 a 7:29)
- Conectores: Claude Docs (panel), Calendar (lectura, si está)

## Objetivo
UNA página cada mañana para Pancho: qué cerró, qué está atascado y 3 decisiones que necesitan su llamada.

## Pasos
1. Lee el panel "Panel de Pancho · Informe y aprobaciones" (Claude Docs, id `bbf7fce6-d9a3-4a45-adca-70dea1f0eba3`). Las casillas que Pancho marcó → márcalas [x] en `salidas/pendiente-de-aprobar.md` y muévelas a "Aprobado" con la fecha.
2. Lee las salidas de las últimas 24 h de `salidas/` de las 5 empresas, sobre todo las de los agentes M4 (Qué cerró, Qué está atascado, Qué costó dinero) y las líneas `CERRADO:` / `ATASCADO:` / `DECISIÓN:` al final de cada salida.
3. Reescribe la sección "Informe de hoy" del panel con EXACTAMENTE este formato (una pantalla, sin relleno):

   **Qué cerró** — una línea por empresa con lo cerrado y su importe si lo hay (Cascade, Klasse, LexLegal, Specter, Empresarios de Éxito). Si no cerró nada: «—».

   **Qué está atascado** — máximo 5 líneas, lo más caro primero: qué, desde cuándo y qué agente lo vigila.

   **3 decisiones para ti** — exactamente 3, numeradas, ordenadas por impacto en dinero. Cada una: la decisión en una frase, las opciones (A/B) y la recomendación del Cerebro.

   **Hoy en agenda** — reuniones de Calendar, si está conectado.
4. Añade a "Pendiente de aprobar" del panel las líneas nuevas sin marcar de `salidas/pendiente-de-aprobar.md`, con su ruta.
5. Si un agente activo no dejó salida en 24 h, ponlo en "Qué está atascado".
6. Guarda la misma página en `salidas/cerebro/AAAA-MM-DD-informe.md`, haz commit y push.
