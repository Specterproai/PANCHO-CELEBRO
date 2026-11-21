# C14 · Conciliación nocturna

- **Empresa:** Cascade Products
- **Módulo:** M3 Backoffice
- **Estado:** Pendiente
- **Cuándo:** Diario 23:11
- **Herramientas:** Revolut, WooPayments, Moloni
- **¿Necesita el OK de Pancho?** No

## Qué hace
Cruza cada noche pagos (Revolut, WooPayments) con pedidos y facturas.

## Con qué trabaja
Pasarelas de pago, Moloni

## Qué entrega
Informe de descuadres

## Reglas
1. Lee antes `CLAUDE.md` y `empresas/cascade/contexto.md` (y `aprendizajes.md` si existe).
2. Si falta un dato o una herramienta, escribe `[DATO]`, haz lo que puedas y dilo en la salida.
3. Lo que necesite OK va a `salidas/pendiente-de-aprobar.md`.
4. Deja la salida en `salidas/cascade/AAAA-MM-DD-C14.md` y haz commit con `C14: AAAA-MM-DD`.
5. Para el informe de la mañana, termina la salida con tres líneas: `CERRADO:`, `ATASCADO:` y `DECISIÓN:` (o `-` si no hay nada).
