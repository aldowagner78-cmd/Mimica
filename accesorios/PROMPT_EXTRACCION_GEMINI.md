# PROMPT PARA GEMINI - COPIAR TODO LO DE ABAJO
# =============================================

Eres un experto diseñador UI/UX y desarrollador frontend. Te estoy enviando capturas de pantalla de una aplicación móvil llamada "Mímica Pro" diseñada en Google Stitch. 

## TU MISIÓN:
Necesito que analices CADA captura y me generes el código HTML+CSS COMPLETO Y AUTÓNOMO de CADA pantalla, en archivos HTML individuales que se puedan abrir en el navegador y se vean IDÉNTICOS a las capturas.

## REQUISITOS CRÍTICOS:

### Para CADA pantalla, genera un archivo HTML completo que incluya:

1. **FONDO**: Replica el gradiente exacto del fondo (azul mágico → teal → púrpura). Incluye las partículas flotantes (esferas 3D, estrellas, cubos) usando CSS puro con animaciones.

2. **ICONOS/ILUSTRACIONES 3D**: Como no puedo extraer los iconos 3D directamente, NECESITO que:
   - Uses emojis de alta calidad como placeholders temporales (🦁 para león, 🍿 para palomitas, 🏀 para basquet, 🎧 para auriculares, 🏆 para trofeo, ⚡ para rayo, 🛡️ para escudo)
   - O que generes SVGs inline que se aproximen al estilo 3D claymorphism
   - Cada "icono" debe estar dentro de un contenedor circular/redondeado con sombra y brillo

3. **TIPOGRAFÍA**: 
   - Título "MÍMICA PRO" con efecto 3D: texto con gradiente blanco-a-dorado, borde/stroke grueso azul o rojo, sombra de texto para profundidad
   - Fuente principal: 'Fredoka One', 'Baloo 2', o similar (bold, redondeada, lúdica)
   - Importa las fuentes de Google Fonts

4. **BOTONES**: Estilo 3D glossy con:
   - "EMPEZAR" / "COMENZAR": Gradiente verde (#98BB1C) con borde dorado, sombra 3D
   - "PASAR": Gradiente rojo (#F63B3F) con sombra
   - "CORRECTO": Gradiente verde con sombra
   - "MENÚ": Gradiente azul
   - "GUARDAR": Naranja/dorado (#FFAD00)
   - "ENTENDIDO": Gradiente azul
   - Todos con border-radius alto (pill shape), box-shadow múltiple para efecto 3D

5. **PALETA DE COLORES EXACTA**:
   - Magical Blue: #444AB2
   - Teal: #4CA5B8  
   - Vibrant Green: #98BB1C
   - Red: #F63B3F
   - Gold: #FFAD00
   - Background gradient: linear-gradient(135deg, #1a0533, #444AB2, #4CA5B8)

6. **TARJETAS/CARDS**: 
   - Fondo blanco o semi-transparente (rgba(255,255,255,0.9))
   - Border-radius: 24px-32px
   - Box-shadow suave y difusa
   - Efecto glassmorphism donde aplique

7. **ELEMENTOS DECORATIVOS** (CSS puro con @keyframes):
   - Esferas flotantes azules/púrpuras con animación de movimiento suave
   - Estrellas amarillas pequeñas que brillan
   - Partículas de luz blanca
   - Background con efecto de burbujas/bokeh

## PANTALLAS QUE NECESITO (un HTML por cada una):

1. **splash.html** - Splash Screen: Logo "MÍMICA PRO" centrado, barra de carga verde animada, texto "Loading Assets...", versión "v2.4.0"
2. **home.html** - Menú Principal: Grid 2x2 de categorías (Animales, Películas, Deportes, Música) con iconos, botón "EMPEZAR", iconos de Config y Ayuda abajo
3. **categories.html** - Selección de Categoría: Lista/grid de más categorías con precios en monedas
4. **game.html** - Pantalla de Juego: Timer circular "0:45" con glow, carta grande blanca con la palabra "LEÓN" en dorado, botones "PASAR" (rojo) y "CORRECTO" (verde)
5. **results.html** - Resultados: Trofeo dorado en podio, confetti, "PUNTUACIÓN TOTAL: 12", botones "VOLVER A JUGAR" y "MENÚ"
6. **howtoplay.html** - Cómo Jugar: 3 tarjetas verticales con pasos (Elige categoría, Actúa, Gana puntos), botón "ENTENDIDO"
7. **settings.html** - Configuración: Modal blanco con toggles de idioma (banderas 🇪🇸/🇬🇧), música, vibración, slider de tiempo de juego, botón "GUARDAR"
8. **gameconfig.html** - Config de Partida: Selección Equipos/Individual, indicador equipo, botón "COMENZAR"
9. **store.html** - Tienda de Packs: Pack destacado arriba, grid de categorías con precio en monedas, sección "¿Necesitas monedas?"
10. **exit_modal.html** - Modal de Salida: "¿QUIERES SALIR?", mensaje, botones Sí (rojo) y No (verde) con estilo 3D

## FORMATO DE SALIDA:
Para CADA pantalla, dame el código HTML COMPLETO (incluyendo DOCTYPE, head con meta viewport 390px, styles inline en <style>, y body). Cada archivo debe ser standalone (no depender de archivos externos excepto Google Fonts).

## EJEMPLO DE ESTRUCTURA:
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Mímica Pro - [Nombre de Pantalla]</title>
    <link href="https://fonts.googleapis.com/css2?family=Fredoka+One&family=Baloo+2:wght@400;600;800&display=swap" rel="stylesheet">
    <style>
        /* TODOS los estilos aquí */
    </style>
</head>
<body>
    <!-- CONTENIDO QUE REPLICA EXACTAMENTE LA CAPTURA -->
</body>
</html>
```

## PRIORIDAD ABSOLUTA:
- Que se vea IDÉNTICO a las capturas adjuntas
- Cada elemento en la MISMA POSICIÓN
- Los MISMOS colores, gradientes, sombras
- Las MISMAS proporciones y tamaños
- Mobile-first (width: 390px máximo)
- NO usar frameworks (ni Tailwind, ni Bootstrap) - solo CSS puro
- NO usar JavaScript salvo para animaciones que CSS no pueda hacer
- Todos los estilos deben ser INLINE en el mismo archivo HTML

Dame los 10 archivos HTML completos, uno por uno.
