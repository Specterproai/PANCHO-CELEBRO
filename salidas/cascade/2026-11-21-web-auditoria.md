# Cascade · Auditoría web y plan de mejora · 21-11-2026

Web: https://cascadeproducts.eu (WordPress + WooCommerce + Elementor 4.4.1)
Estado: **auditoría pública hecha. No he entrado en wp-admin**: el entorno donde trabajo tiene bloqueado el dominio cascadeproducts.eu. No he cambiado nada en la web.

---

## 0. Antes de nada

1. **Cambia la contraseña de ventas@cascadeproducts.eu en WordPress** (y en el correo si es la misma). Se ha compartido en un chat. Cuando quieras que entre, crea un usuario aparte para mí con rol Administrador o "Shop manager" y bórralo al terminar.
2. **Para que yo pueda entrar y hacer los cambios** hay dos opciones:
   - Añadir `cascadeproducts.eu` a los dominios permitidos en claude.ai (Ajustes > Capacidades). Así entro desde aquí con un navegador automático.
   - O abrir esta tarea desde la app de escritorio con Claude en Chrome conectado.
3. **Copia de seguridad completa** (archivos + base de datos) antes de tocar nada: UpdraftPlus o la del hosting.

## 1. Riesgo regulatorio: revisar antes de lanzar marketing internacional

Esto pesa más que cualquier mejora de SEO. No soy abogado; es para que lo revise LexLegal o un regulatorio especializado.

- **Venta pública a cualquiera.** Rellenos, bioestimuladores, hilos y exosomas tienen precio público y "Añadir al carrito" sin verificar que el comprador sea médico. Solo hay un aviso de texto ("debe ser administrado por profesionales autorizados"). Las normas de Cascade dicen "solo médicos y clínicas, nunca paciente final": hoy la web no lo garantiza.
- **EE. UU. (80 % de la facturación).** Varios productos del catálogo (p. ej. Rejuran, exosomas, versiones UE de rellenos) pueden no tener autorización de la FDA para EE. UU. La FDA ha enviado cartas de advertencia a distribuidores que venden rellenos o exosomas no autorizados a médicos estadounidenses. Hacer SEO y anuncios dirigidos a EE. UU. aumenta la visibilidad de ese riesgo. Hay que confirmar producto por producto qué se puede vender allí.
- **India, LATAM y el resto de Europa.** Cada mercado tiene su registro sanitario: CDSCO (India), COFEPRIS (México), ANVISA (Brasil), INVIMA (Colombia), MDR/CE (UE), MHRA (Reino Unido), Swissmedic (Suiza). Antes de "tocar puertas", definir qué referencias se pueden vender en cada país.
- **Anuncios.** Google y Meta restringen la publicidad de productos sanitarios con receta. Para clínicas, los canales seguros son SEO, LinkedIn, ferias/congresos, comerciales y email B2B donde la ley lo permita (EE. UU. sí con opción de baja; España/UE necesita consentimiento previo según LSSI/RGPD).
- **Datos legales que faltan en la web:** razón social, NIF/VAT, registro mercantil, licencia de distribución de productos sanitarios y fabricante/CE de cada producto. En la UE el aviso legal es obligatorio y da confianza a las clínicas.

**Mi recomendación:** convertir la tienda en **B2B con registro verificado**. El catálogo sigue siendo público (bueno para SEO), pero precios y carrito solo se ven al iniciar sesión con número de colegiado o licencia médica, que se aprueba a mano. Plugins: B2BKing o "WooCommerce B2B". Esto reduce el riesgo legal y refuerza el posicionamiento "solo profesionales".

## 2. Fallos detectados (arreglo rápido)

| # | Problema | Dónde | Arreglo |
|---|---|---|---|
| 1 | Título de portada "Cascade Products" sin palabras clave | Inicio | Ver textos en §5 |
| 2 | H1 "CASCADE - Tienda online de cosmética": la web se presenta como cosmética, no como distribuidor médico | Inicio | Cambiar a H1 de §5 |
| 3 | Sin meta description en inicio, tienda, contacto y fichas (la de Sculptra está vacía) | Toda la web | Plugin SEO + textos §5 |
| 4 | Tienda sin etiqueta canonical | /tienda/ | La añade el plugin SEO |
| 5 | La ficha de Sculptra dice "REJURAN HEALER BLACK cantidad" | /tienda/sculptra-2x5ml/ | Corregir en la plantilla o en el producto |
| 6 | Títulos con errores: "P(LA/CL", "EGZOSOMY", mezcla de idiomas | Catálogo | Normalizar nombres: Marca + producto + formato |
| 7 | Imágenes PNG pesadas con nombres "ChatGPT-Image-…" y `.jpg-300x300.webp` | Fichas | Convertir a WebP/AVIF y renombrar (ej. `sculptra-2x5ml.webp`) |
| 8 | Imágenes de productos relacionados sin texto alternativo (alt) | Fichas | Alt = nombre del producto |
| 9 | Sitemap de usuarios público (`wp-sitemap-users-1.xml`): muestra los nombres de usuario de admin | Seguridad | Lo desactiva el plugin SEO |
| 10 | Precio tachado en casi todos los productos ("Oferta" permanente) | Tienda | En la UE, el precio tachado debe ser el más bajo de los últimos 30 días (Directiva Ómnibus). Quitar "ofertas" que no lo cumplan |
| 11 | Mezcla de idiomas en la interfaz ("Cart", "Ordenar por") | Cabecera | Traducción del tema |
| 12 | Política de envíos sin países, plazos ni el mínimo de 8.000 € para envío gratis | /politica-de-envios/ | Completar con [DATO: países, plazos, costes] |
| 13 | Dirección "GZO-Fabriksgelände, Austria" sin razón social ni empresa | Pie y contacto | Datos legales completos |
| 14 | Sin WhatsApp, que es el canal real de los médicos en EE. UU. | Contacto | Botón de WhatsApp Business |
| 15 | No hay página "Quiénes somos" | Menú | Crear: modelo de compra bajo pedido, envío 24 h, marcas, garantía de autenticidad (con pruebas) |

## 3. Velocidad (lo que haré al entrar)

No he podido medir la velocidad (PageSpeed también está bloqueado desde aquí). Plan estándar para WooCommerce + Elementor:

1. **Caché**: si el hosting es LiteSpeed → LiteSpeed Cache; si no → WP Rocket (de pago) o W3 Total Cache. Sin cachear carrito, checkout ni mi cuenta.
2. **Imágenes**: conversión masiva a WebP/AVIF (ShortPixel, Imagify o la de LiteSpeed), lazy-load y medidas correctas.
3. **Elementor**: activar "Optimized DOM", "Improved asset loading" y "Inline font icons"; desactivar widgets que no se usen. Alojar Google Fonts en local.
4. **CSS/JS**: minificar, diferir JS y eliminar el CSS que no se usa. Quitar los scripts de WooCommerce en páginas que no son tienda.
5. **CDN**: Cloudflare gratis (también da seguridad y SSL).
6. **Limpieza**: revisiones, transients y plugins que no se usan. Actualizar WordPress, el tema y los plugins (después de la copia).
7. **Medir antes y después** con PageSpeed Insights (móvil) y dejar las cifras en este archivo.

## 4. Posicionamiento orgánico + internacional

1. **Plugin SEO**: Rank Math (gratis) o Yoast. Títulos y descripciones, canonical, sitemap limpio, schema Product/Organization y breadcrumbs.
2. **Idiomas y mercados** (lo más importante para EE. UU., LATAM, Europa e India):
   - Inglés como idioma principal internacional (EE. UU., India, Reino Unido, Suiza, Alemania) + español (LATAM/España). Portugués para Brasil más adelante.
   - Plugin: WPML (con WooCommerce Multilingual y varias monedas) o TranslatePress. URLs `/en/`, `/es/` con hreflang.
   - Monedas: EUR + USD como mínimo. Ver si interesa un dominio .com para EE. UU. y LATAM: el .eu tiene menos fuerza en Google fuera de Europa. [DATO: ¿tenéis cascadeproducts.com?]
3. **Fichas de producto con contenido propio** (no copiado del fabricante): marca, composición, presentación, conservación, documentación (CE, ficha técnica), "solo uso profesional". Sin promesas de resultados.
4. **Páginas por categoría y marca** (lo que buscan las clínicas): "Comprar Sculptra para clínicas", "Belotero wholesale", "PLLA threads supplier", "Rejuran Healer distributor". Una página con texto útil por categoría.
5. **Blog B2B / Recursos** (1-2 artículos al mes, en inglés y español): comparativas técnicas de productos, conservación y logística, cómo verificar que un relleno es auténtico. Sirve también para que te citen ChatGPT y Perplexity.
6. **Google Search Console + Bing Webmaster**: dar de alta, enviar el sitemap y vigilar errores. Google Analytics 4 con conversiones (registro de médico, pedido, clic en WhatsApp).
7. **Perfil de empresa en Google** con la dirección real.
8. **Reseñas reales** de médicos (con su permiso). El bloque actual habla de MRW; mejor centrarlo en autenticidad y rapidez.

## 5. Textos listos para pegar (Rank Math / Yoast)

**Inicio (ES)**
- Título: `Cascade Products | Distribuidor de medicina estética para clínicas`
- Descripción: `Rellenos, bioestimuladores, hilos y mesoterapia de marcas originales para médicos y clínicas. Compra profesional verificada y envío rápido internacional.`
- H1: `Distribuidor de medicina estética para profesionales`

**Home (EN)**
- Title: `Cascade Products | Aesthetic Medicine Supplier for Clinics`
- Description: `Authentic dermal fillers, biostimulators, threads and skin boosters for licensed doctors and clinics. Verified professional accounts, fast international shipping.`
- H1: `Aesthetic medicine supplies for licensed professionals`

**Tienda (ES)**: Título `Catálogo profesional de medicina estética | Cascade Products` · Descripción `Más de [DATO] referencias originales: rellenos de ácido hialurónico, PLLA, hilos tensores, PDRN y mesoterapia. Solo para profesionales sanitarios.`

**Contacto (ES)**: Título `Contacto para clínicas y médicos | Cascade Products` · Descripción `Abre tu cuenta profesional o haz tu pedido por email, teléfono o WhatsApp. Respuesta en [DATO] horas.`

**Plantilla de ficha**: Título `{Producto} {formato} – Compra profesional | Cascade Products` · Descripción `{Producto} original de {marca}, {formato}. Para médicos y clínicas acreditados. Envío internacional desde Europa.`

> Nota "envío internacional" y "24 h": en la web no hay ninguna página que lo confirme. Confírmalo antes de publicar.

## 6. Orden de trabajo propuesto

| Fase | Qué | Quién |
|---|---|---|
| Hoy | Cambiar la contraseña, dar acceso (§0), copia de seguridad | Pancho |
| Semana 1 | Arreglos §2, plugin SEO, textos §5, velocidad §3, medición antes/después | Claude (con acceso) |
| Semana 1 | Consulta regulatoria: qué productos se pueden vender en EE. UU., UE, LATAM e India | LexLegal / regulatorio |
| Semana 2 | Registro B2B verificado + datos legales + página Quiénes somos | Claude + Pancho (datos) |
| Semanas 2-4 | Versión en inglés + USD + hreflang; páginas de categoría y marca | Claude |
| Después | Blog B2B, Search Console, campaña a clínicas por país (según el OK regulatorio) | Agentes 01-03 |

## Pendiente de Pancho

- Contraseña nueva + forma de acceso (§0).
- Datos legales: razón social, NIF/VAT, dirección, licencia de distribución.
- Países a los que se envía, plazos y costes reales.
- ¿Dominio .com disponible? ¿Hosting (para elegir el plugin de caché)?
- OK para convertir la tienda en B2B con registro verificado.
