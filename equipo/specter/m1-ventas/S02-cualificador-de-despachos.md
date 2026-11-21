# S02 · Cualificador de despachos

- **Empresa:** Specter AI
- **Módulo:** M1 Ventas
- **Estado:** Activo
- **Cuándo:** Cada hora 9-20 h
- **Herramientas:** Drive
- **¿Necesita el OK de Pancho?** No

## Qué hace
Clasifica por tipo (autónomo, pequeño, mediano, grande, procurador), nº de abogados y urgencia.

## Con qué trabaja
Leads y lista de espera

## Qué entrega
Lead puntuado

## Reglas
1. Lee antes `CLAUDE.md` y `empresas/specter/contexto.md` (y `aprendizajes.md` si existe).
2. Si falta un dato o una herramienta, escribe `[DATO]`, haz lo que puedas y dilo en la salida.
3. Lo que necesite OK va a `salidas/pendiente-de-aprobar.md`.
4. Deja la salida en `salidas/specter/AAAA-MM-DD-S02.md` y haz commit con `S02: AAAA-MM-DD`.
5. Para el informe de la mañana, termina la salida con tres líneas: `CERRADO:`, `ATASCADO:` y `DECISIÓN:` (o `-` si no hay nada).
