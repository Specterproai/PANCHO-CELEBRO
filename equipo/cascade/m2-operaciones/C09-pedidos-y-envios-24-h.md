# C09 · Pedidos y envíos 24 h

- **Empresa:** Cascade Products
- **Módulo:** M2 Operaciones
- **Estado:** Pendiente
- **Cuándo:** Diario 9:41 y 17:13
- **Herramientas:** WooCommerce, Gmail
- **¿Necesita el OK de Pancho?** Sí en compras a proveedor

## Qué hace
Comprueba que cada pedido pagado se compra al proveedor y sale en 24 h; avisa si algo se retrasa.

## Con qué trabaja
Pedidos pagados, proveedores

## Qué entrega
Estado de cada pedido y alerta de retrasos

## Reglas
1. Lee antes `CLAUDE.md` y `empresas/cascade/contexto.md` (y `aprendizajes.md` si existe).
2. Si falta un dato o una herramienta, escribe `[DATO]`, haz lo que puedas y dilo en la salida.
3. Lo que necesite OK va a `salidas/pendiente-de-aprobar.md`.
4. Deja la salida en `salidas/cascade/AAAA-MM-DD-C09.md` y haz commit con `C09: AAAA-MM-DD`.
5. Para el informe de la mañana, termina la salida con tres líneas: `CERRADO:`, `ATASCADO:` y `DECISIÓN:` (o `-` si no hay nada).
