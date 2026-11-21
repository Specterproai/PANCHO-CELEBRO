# S11 · Salud de clientes

- **Empresa:** Specter AI
- **Módulo:** M2 Operaciones
- **Estado:** Pendiente
- **Cuándo:** Semanal miércoles 11:23
- **Herramientas:** Drive
- **¿Necesita el OK de Pancho?** No

## Qué hace
Detecta despachos con riesgo de baja (poco uso, tokens agotados) y avisa antes del día 15.

## Con qué trabaja
Uso, pagos

## Qué entrega
Lista de riesgo + acción

## Reglas
1. Lee antes `CLAUDE.md` y `empresas/specter/contexto.md` (y `aprendizajes.md` si existe).
2. Si falta un dato o una herramienta, escribe `[DATO]`, haz lo que puedas y dilo en la salida.
3. Lo que necesite OK va a `salidas/pendiente-de-aprobar.md`.
4. Deja la salida en `salidas/specter/AAAA-MM-DD-S11.md` y haz commit con `S11: AAAA-MM-DD`.
5. Para el informe de la mañana, termina la salida con tres líneas: `CERRADO:`, `ATASCADO:` y `DECISIÓN:` (o `-` si no hay nada).
