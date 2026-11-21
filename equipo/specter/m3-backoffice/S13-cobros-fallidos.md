# S13 · Cobros fallidos

- **Empresa:** Specter AI
- **Módulo:** M3 Backoffice
- **Estado:** Pausado
- **Cuándo:** Diario 10:47 y día 15
- **Herramientas:** Stripe, Gmail
- **¿Necesita el OK de Pancho?** No en recordatorios

## Qué hace
Persigue pagos fallidos y tarjetas caducadas; el seguimiento de pagos es el día 15.

## Con qué trabaja
Stripe

## Qué entrega
Recordatorios + lista de impagos

## Reglas
1. Lee antes `CLAUDE.md` y `empresas/specter/contexto.md` (y `aprendizajes.md` si existe).
2. Si falta un dato o una herramienta, escribe `[DATO]`, haz lo que puedas y dilo en la salida.
3. Lo que necesite OK va a `salidas/pendiente-de-aprobar.md`.
4. Deja la salida en `salidas/specter/AAAA-MM-DD-S13.md` y haz commit con `S13: AAAA-MM-DD`.
5. Para el informe de la mañana, termina la salida con tres líneas: `CERRADO:`, `ATASCADO:` y `DECISIÓN:` (o `-` si no hay nada).
