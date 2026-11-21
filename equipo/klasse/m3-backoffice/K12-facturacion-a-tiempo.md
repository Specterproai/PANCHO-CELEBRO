# K12 · Facturación a tiempo

- **Empresa:** Klasse / EUROPE 2027
- **Módulo:** M3 Backoffice
- **Estado:** Pausado
- **Cuándo:** Diario 19:13
- **Herramientas:** Facturación: [DATO]
- **¿Necesita el OK de Pancho?** Sí

## Qué hace
Factura cada inscripción y cada sponsor en su fecha (Klasse Automotive S.L.U.).

## Con qué trabaja
Contratos, pagos

## Qué entrega
Facturas emitidas

## Reglas
1. Lee antes `CLAUDE.md` y `empresas/klasse/contexto.md` (y `aprendizajes.md` si existe).
2. Si falta un dato o una herramienta, escribe `[DATO]`, haz lo que puedas y dilo en la salida.
3. Lo que necesite OK va a `salidas/pendiente-de-aprobar.md`.
4. Deja la salida en `salidas/klasse/AAAA-MM-DD-K12.md` y haz commit con `K12: AAAA-MM-DD`.
5. Para el informe de la mañana, termina la salida con tres líneas: `CERRADO:`, `ATASCADO:` y `DECISIÓN:` (o `-` si no hay nada).
