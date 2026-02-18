'; $idx = $f.IndexOf($m) + $m.Length; $prompt = $f.Substring($idx).Trim(); [System.IO.File]::WriteAllText((Join-Path '%targetDir%' 'INSTRUCCIONES.md'), $prompt, [System.Text.Encoding]::UTF8)"
if not exist "%targetDir%\INSTRUCCIONES.md" (
    echo [ERROR] No se pudo generar INSTRUCCIONES.md
    pause
    exit /b 1
)
echo [OK] INSTRUCCIONES.md generado correctamente.

:: ===========================================================
:: PASO 4: Abrir Antigravity con la carpeta del proyecto
:: ===========================================================
echo [INFO] Abriendo Antigravity con el proyecto...
start "" antigravity "%targetDir%" -n
echo [OK] Antigravity abierto en ventana nueva.

:: Esperar a que Antigravity cargue completamente
echo [INFO] Esperando a que Antigravity cargue (5 segundos)...
timeout /t 5 /nobreak >nul

:: ===========================================================
:: PASO 5: Enviar el prompt al chat en Modo Agente
:: ===========================================================
echo [INFO] Enviando prompt al chat de Antigravity (Modo Agente)...
type "%targetDir%\INSTRUCCIONES.md" | antigravity chat - -r --mode agent --maximize
echo [OK] Prompt enviado al chat.

:: ===========================================================
:: PASO 6: Log del lanzamiento
:: ===========================================================
echo [%date% %time%] Lanzado: Disenar_desarrollar_e_implementar (nuevo) >> "%USERPROFILE%\Desktop\promptmaster_launches.log"

echo.
echo  ========================================================
echo       LANZAMIENTO COMPLETADO EXITOSAMENTE
echo  ========================================================
echo   Antigravity ya esta trabajando en tu proyecto.
echo   El prompt completo esta en: %targetDir%\INSTRUCCIONES.md
echo   Esta ventana se cerrara automaticamente en 10 segundos.
echo  ========================================================
echo.
timeout /t 10
goto :eof

:: ============================================================
:: NO BORRAR LA LINEA SIGUIENTE - CONTIENE EL PROMPT COMPLETO
:: ============================================================
#BEGIN_PROMPT#
<role>
Desarrollador Senior Full-Stack especializado en React/Vite/Tailwind, diseño de interfaz de usuario (UI/UX) y arquitectura de Progressive Web Apps (PWA) con Firebase, con una capacidad demostrada para replicar diseños de Google Stitch con precisión pixel-perfecta y desarrollar aplicaciones bilingües interactivas.
</role>

<objective>
Diseñar, desarrollar e implementar una Progressive Web App (PWA) bilingüe (español/inglés) para el juego "Dígalo con Mímicas". La aplicación deberá permitir la gestión de múltiples categorías y palabras, configuración avanzada de partidas (palabras por turno, tiempo, puntos), un sistema de premios y la posibilidad de canjear puntos por categorías ocultas. La interfaz será visualmente atractiva, interactiva con animaciones y sonidos en los botones y a lo largo de la app, y replicará al 100% los diseños aprobados en Google Stitch. La aplicación será desplegada gratuitamente en Firebase Hosting, accesible desde navegadores web en Android e iOS, y no utilizará el giroscopio del dispositivo.
</objective>

<workflow>
### Fase 0: INVESTIGACIÓN (NotebookLM)
*   Crea un cuaderno en NotebookLM denominado "Investigación MimicasGamePWA".
*   Realiza una "Deep Research" sobre:
    *   Aplicaciones de juegos de mímicas/charadas existentes: mecánicas, monetización (si aplica), UX/UI, categorías de palabras comunes.
    *   Mejores prácticas para Progressive Web Apps (PWA) en 2024: manifest.json, Service Workers para cache y offline, compatibilidad iOS.
    *   Estrategias de internacionalización (i18n) en React para una aplicación bilingüe (español/inglés).
    *   Patrones de diseño de base de datos en Firestore para almacenar categorías, palabras, progreso del usuario, puntos y premios.
    *   Implementación de sonidos y animaciones en React con Tailwind CSS.
    *   Estrategias para gestionar el estado del juego (turnos, temporizador, puntuación) en una aplicación React.

### Fase 0.5: VALIDACIÓN DEL RESEARCH
*   Prepara un resumen conciso de los hallazgos de la investigación:
    *   Aplicaciones similares destacadas y lecciones aprendidas.
    *   Tecnologías recomendadas para cada componente (ej. biblioteca i18n, librerías de audio/animación).
    *   Propuesta de arquitectura de datos inicial para Firestore.
    *   Enfoque propuesto para la experiencia de usuario (UX) basada en las mejores prácticas.
*   Presenta este resumen al usuario para su aprobación antes de proceder.

### Fase 1: PROTOTIPADO VISUAL (Google Stitch)
*   Una vez aprobado el research, crea **TODAS** las interfaces visuales de la aplicación en Google Stitch, siguiendo los principios de un diseño moderno, intuitivo y lúdico, adaptado a una audiencia general de jugadores.
*   **CHECKLIST MÍNIMO DE PANTALLAS A DISEÑAR:**
    *   **Splash / Loading screen:** Pantalla inicial con logo del juego.
    *   **Onboarding (si aplica):** Pantalla(s) de bienvenida o tutorial "Cómo Jugar" para la primera vez.
    *   **Home / Menú Principal:** Opciones para "Jugar", "Categorías", "Premios", "Configuración".
    *   **Pantalla de Selección de Categoría:** Lista de categorías disponibles, indicando cuáles están bloqueadas/desbloqueadas.
    *   **Pantalla de Configuración de Partida:** Sliders o inputs para definir "Palabras por turno", "Tiempo de juego", "Puntos por palabra correcta".
    *   **Pantalla de Juego (en curso):** Área para mostrar la palabra a adivinar, temporizador, botones claros para "Correcto" y "Pasar", botón de pausa.
    *   **Pantalla de Resumen de Turno/Partida:** Muestra las palabras acertadas, falladas/pasadas, puntuación total y premios obtenidos.
    *   **Pantalla de Premios / Tienda:** Muestra los premios disponibles para canjear (ej. nuevas categorías), con el costo en puntos y el saldo actual del jugador.
    *   **Pantalla de Configuración General:** Opciones para cambiar el idioma (español/inglés), activar/desactivar sonidos, restablecer progreso (con confirmación).
    *   **Estados Vacíos:** (Ej. "No hay categorías disponibles", "Aún no has ganado premios").
    *   **Estados de Error:** (Ej. "Error al cargar los datos", "Problema de conexión").
    *   **Modales / Diálogos:** Confirmación de acciones (ej. "Canjear premio", "Restablecer progreso").
*   Presenta los diseños al usuario para su aprobación. Los diseños aprobados en Stitch son INMUTABLES.

### Fase 2: IMPLEMENTACIÓN (React/Vite/Tailwind)
*   **Creación del proyecto:** Inicializa un proyecto React con Vite y configura Tailwind CSS.
*   **Orden A-E-F estricto:**
    1.  **ESTÉTICA:** Replicación pixel-perfecta de los diseños de Stitch usando Tailwind CSS para estilos, asegurando que cada botón, fuente, tamaño, color, layout, icono y animación sea idéntico a lo aprobado. Implementa las animaciones de botones y efectos de transición visuales.
    2.  **ESTRUCTURA:** Construye la estructura de componentes de React, enrutamiento (React Router DOM) para las diferentes pantallas y la arquitectura de internacionalización.
    3.  **FUNCIÓN:** Implementa la lógica de negocio del juego: gestión de categorías y palabras, motor de juego (temporizador, conteo de palabras, puntuación), sistema de premios y canje, persistencia de datos y soporte de múltiples idiomas.
*   **Soporte Multilingüe:** Implementa la funcionalidad completa para cambiar la interfaz entre español e inglés en tiempo real.
*   **Sonidos:** Integra los sonidos de la aplicación (clics de botones, inicio/fin de turno, acierto/fallo).
*   **No Uso de Giroscopio:** Asegura que no se utilice ninguna API de giroscopio o acelerómetro.

### Fase 3: PERSISTENCIA Y BACKEND (Firebase)
*   **Configuración de Firebase:**
    *   **Firebase Authentication:** Configura un método de autenticación anónimo para mantener el progreso del usuario sin requerir registro explícito, o bien un sistema de autenticación simple si se considera necesario para la persistencia entre dispositivos.
    *   **Firestore Database:** Diseña y configura la estructura de la base de datos para almacenar:
        *   Categorías de palabras (con metadatos como "bloqueada/desbloqueada", costo en puntos).
        *   Listas de palabras asociadas a cada categoría.
        *   Progreso del usuario (puntos acumulados, categorías desbloqueadas, configuraciones preferidas).
    *   **Firebase Hosting:** Configura el proyecto para ser desplegado en Firebase Hosting.
*   **PWA OBLIGATORIA:**
    *   Crea el archivo `manifest.json` con:
        *   `name`, `short_name`, `icons` (múltiples tamaños), `theme_color`, `background_color`, `display: "standalone"`, `start_url`.
    *   Configura un `Service Worker` para:
        *   Cacheo de recursos estáticos (HTML, CSS, JS, imágenes, fuentes, sonidos) para un rendimiento rápido.
        *   Soporte offline básico (al menos la shell de la aplicación).
    *   Agrega las meta tags necesarias en el `index.html` para iOS:
        *   `apple-touch-icon`
        *   `apple-mobile-web-app-capable`
        *   `apple-mobile-web-app-status-bar-style`
        *   `apple-mobile-web-app-title`
*   Despliega la aplicación como una PWA funcional en Firebase Hosting, accesible desde cualquier navegador compatible con PWA en Android e iOS.
</workflow>

<rules>
*   **ORDEN DE DESARROLLO A-E-F INVIOLABLE:** La prioridad es siempre 1° ESTÉTICA → 2° ESTRUCTURA → 3° FUNCIÓN. Primero se diseña algo hermoso y moderno (en Stitch), luego se organiza el código (componentes, rutas), y finalmente se programa la lógica.
*   **STITCH ES LEY (INMUTABLE):** Los diseños creados y aprobados en Google Stitch son SAGRADOS. El agente NO DEBE inventar elementos visuales nuevos. Debe programar EXACTAMENTE lo que Stitch diseñó: los mismos botones, fuentes, tamaños, colores, layouts, iconos, y estilos. Si Stitch lo diseñó, se implementa tal cual. Si no lo diseñó, NO EXISTE.
*   **PWA OBLIGATORIA Y GRATUITA:** Toda aplicación debe ser una Progressive Web App (PWA) instalable desde Chrome o Safari. NO generar APK ni IPA. Debe ser GRATUITA, para Android e iOS vía navegador.
    *   Configuración completa de `manifest.json`.
    *   Configuración de `Service Worker` para cache y soporte offline básico.
    *   Adición de meta tags para iOS (`apple-touch-icon`, `apple-mobile-web-app-capable`).
*   **ADAPTACIÓN A LA AUDIENCIA:** La interfaz debe ser intuitiva, visualmente atractiva y fácil de usar para una audiencia general, con tamaños de fuente legibles y navegación clara.
*   **STACK GRATUITO EXCLUSIVO:** Priorizar el uso de Firebase (Auth, Firestore, Hosting), Vercel (si se requiere para serverless functions, aunque Firebase Hosting es suficiente), NotebookLM, Google Stitch y herramientas sin costo.
*   **SIN CHARLATANERÍA:** No se permiten saludos, despedidas o explicaciones sobre el prompt. La respuesta debe ser directamente el prompt ejecutable.
*   **DELIMITADORES CLAROS:** Uso obligatorio de `###` y bloques de código para facilitar el parseo por parte del agente.
*   **IDIOMA Y MULTILINGÜISMO:** La aplicación debe ser completamente en español por defecto, con la capacidad de cambiar a inglés de manera completa en la configuración.
*   **NO GIROSCOPIO:** La aplicación no debe hacer uso de las capacidades del giroscopio o acelerómetro del dispositivo bajo ninguna circunstancia.
*   **ANIMACIONES Y SONIDOS:** Los botones deben tener animaciones visuales y efectos de sonido al interactuar, y la aplicación debe integrar sonidos relevantes según el diseño de Stitch.
*   **CONTEXTO DE DESARROLLO:** El proyecto es nuevo y debe ser desarrollado desde cero en una carpeta dedicada en el Escritorio de Windows.
</rules>

<next_steps>
Crea la carpeta "%USERPROFILE%\Desktop\MimicasGamePWA". Una vez creada, el siguiente paso es iniciar la Fase 0: INVESTIGACIÓN en NotebookLM dentro de esa carpeta para comenzar la recopilación de información según las directivas establecidas.
</next_steps>