# S12 · Facturación a tiempo

- **Empresa:** Specter AI
- **Módulo:** M3 Backoffice
- **Estado:** Pendiente
- **Cuándo:** Diario 19:23
- **Herramientas:** Stripe
- **¿Necesita el OK de Pancho?** No en cargos de suscripción ya firmados

## Qué hace
Factura suscripciones (mensual u 11 cuotas, o anual de 11 meses) y recargas de tokens desde Specter AI LLC.

## Con qué trabaja
Suscripciones, recargas

## Qué entrega
Facturas emitidas

## Reglas
1. Lee antes `CLAUDE.md` y `empresas/specter/contexto.md` (y `aprendizajes.md` si existe).
2. Si falta un dato o una herramienta, escribe `[DATO]`, haz lo que puedas y dilo en la salida.
3. Lo que necesite OK va a `salidas/pendiente-de-aprobar.md`.
4. Deja la salida en `salidas/specter/AAAA-MM-DD-S12.md` y haz commit con `S12: AAAA-MM-DD`.
5. Para el informe de la mañana, termina la salida con tres líneas: `CERRADO:`, `ATASCADO:` y `DECISIÓN:` (o `-` si no hay nada).
