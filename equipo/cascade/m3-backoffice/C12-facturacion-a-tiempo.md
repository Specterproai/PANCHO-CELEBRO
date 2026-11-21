# C12 · Facturación a tiempo

- **Empresa:** Cascade Products
- **Módulo:** M3 Backoffice
- **Estado:** Pendiente
- **Cuándo:** Diario 19:07
- **Herramientas:** Moloni, WooCommerce
- **¿Necesita el OK de Pancho?** Sí hasta validar el flujo

## Qué hace
Emite la factura de cada pedido pagado en Moloni el mismo día.

## Con qué trabaja
Pedidos pagados

## Qué entrega
Factura emitida y enviada

## Reglas
1. Lee antes `CLAUDE.md` y `empresas/cascade/contexto.md` (y `aprendizajes.md` si existe).
2. Si falta un dato o una herramienta, escribe `[DATO]`, haz lo que puedas y dilo en la salida.
3. Lo que necesite OK va a `salidas/pendiente-de-aprobar.md`.
4. Deja la salida en `salidas/cascade/AAAA-MM-DD-C12.md` y haz commit con `C12: AAAA-MM-DD`.
5. Para el informe de la mañana, termina la salida con tres líneas: `CERRADO:`, `ATASCADO:` y `DECISIÓN:` (o `-` si no hay nada).
