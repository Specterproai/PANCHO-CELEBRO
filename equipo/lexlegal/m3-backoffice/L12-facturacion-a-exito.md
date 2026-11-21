# L12 · Facturación a éxito

- **Empresa:** LexLegal Advisors
- **Módulo:** M3 Backoffice
- **Estado:** Pausado
- **Cuándo:** Diario 19:17
- **Herramientas:** Stripe, facturación: [DATO]
- **¿Necesita el OK de Pancho?** Sí hasta validar el flujo

## Qué hace
Emite la factura del 10 % + IVA en cuanto el cliente cobra; LEX 360 cada mes.

## Con qué trabaja
Cobros recuperados, suscripciones

## Qué entrega
Facturas emitidas

## Reglas
1. Lee antes `CLAUDE.md` y `empresas/lexlegal/contexto.md` (y `aprendizajes.md` si existe).
2. Si falta un dato o una herramienta, escribe `[DATO]`, haz lo que puedas y dilo en la salida.
3. Lo que necesite OK va a `salidas/pendiente-de-aprobar.md`.
4. Deja la salida en `salidas/lexlegal/AAAA-MM-DD-L12.md` y haz commit con `L12: AAAA-MM-DD`.
5. Para el informe de la mañana, termina la salida con tres líneas: `CERRADO:`, `ATASCADO:` y `DECISIÓN:` (o `-` si no hay nada).
