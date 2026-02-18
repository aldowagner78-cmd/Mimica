# 🎭 Validación de Research - Dígalo con Mímicas PWA

## 1. Aplicaciones Similares Destacadas y Lecciones Aprendidas

### Apps Analizadas:
| App | Fortalezas | Debilidades |
|-----|-----------|-------------|
| **Heads Up!** | UX intuitiva, gran variedad de categorías, monetización con packs | Requiere giroscopio (nosotros NO lo usaremos) |
| **Charades!** | Diseño colorido, categorías temáticas, audio feedback | Ads intrusivos en versión free |
| **Charade Me** | Simple y nostálgico, fácil de usar | Pocas categorías, diseño básico |
| **PlayMime** | Personalización de tiempo/rondas | UX menos pulida |

### Lecciones Clave:
- ✅ **Pantalla completa** para mostrar la palabra → máxima visibilidad
- ✅ **Feedback visual claro**: verde = correcto, rojo = pasar/fallar
- ✅ **Categorías variadas** mantienen engagement (mínimo 10-15 categorías)
- ✅ **Decks personalizables** son un plus (custom categories)
- ✅ **Modelo freemium** con categorías bloqueables y sistema de puntos
- ❌ NO usar giroscopio → usaremos botones "Correcto" y "Pasar"
- ❌ NO ads intrusivos → monetización solo via puntos/categorías

---

## 2. Tecnologías Recomendadas por Componente

| Componente | Tecnología | Justificación |
|-----------|-----------|---------------|
| **Framework** | React 18+ con Vite | Rápido, moderno, HMR excelente |
| **Estilos** | Tailwind CSS v3 | Utility-first, rápido prototipado, responsive |
| **Animaciones** | Framer Motion | API declarativa, performance hardware-accelerated, gestos |
| **Sonidos** | Howler.js | Gestión robusta de audio, sprites, compatibilidad cross-browser |
| **i18n** | react-i18next | Más popular, hooks modernos, carga dinámica de traducciones |
| **Routing** | React Router DOM v6 | Estándar de facto para SPA React |
| **Estado** | useReducer + Context API | Ideal para lógica compleja de juego sin dependencias externas |
| **Auth** | Firebase Auth (Anónimo) | Sin fricción, persistencia de progreso entre sesiones |
| **Base de datos** | Firestore | Real-time, offline, integración nativa con Firebase |
| **Hosting** | Firebase Hosting | Gratuito, CDN global, deploy automático |
| **Iconos** | Lucide React | Lightweight, tree-shakeable, consistente |
| **PWA** | Vite PWA Plugin | Genera SW y manifest automáticamente |

---

## 3. Propuesta de Arquitectura de Datos en Firestore

```
📦 Firestore Database Structure
│
├── 📁 categories/
│   └── {categoryId}
│       ├── name_es: "Animales"
│       ├── name_en: "Animals"
│       ├── icon: "🐾"
│       ├── color: "#FF6B35"
│       ├── isLocked: true
│       ├── unlockCost: 500
│       ├── order: 1
│       └── wordCount: 50
│
├── 📁 categories/{categoryId}/words/
│   └── {wordId}
│       ├── text_es: "Elefante"
│       ├── text_en: "Elephant"
│       └── difficulty: 1
│
├── 📁 users/
│   └── {userId} (auth UID)
│       ├── totalPoints: 1250
│       ├── gamesPlayed: 15
│       ├── unlockedCategories: ["cat1", "cat2"]
│       ├── language: "es"
│       ├── soundEnabled: true
│       ├── createdAt: timestamp
│       └── lastActive: timestamp
│
├── 📁 users/{userId}/gameHistory/
│   └── {gameId}
│       ├── categoryId: "animals"
│       ├── wordsCorrect: 8
│       ├── wordsPassed: 2
│       ├── pointsEarned: 80
│       ├── duration: 60
│       └── playedAt: timestamp
│
└── 📁 rewards/
    └── {rewardId}
        ├── name_es: "Categoría Premium: Películas"
        ├── name_en: "Premium Category: Movies"
        ├── type: "category_unlock"
        ├── targetCategoryId: "movies"
        ├── pointsCost: 1000
        ├── icon: "🎬"
        └── isAvailable: true
```

---

## 4. Enfoque de UX Propuesto

### Flujo Principal del Usuario:
```
Splash Screen → Onboarding (1ra vez) → Home → Seleccionar Categoría 
→ Configurar Partida → Jugar → Resumen de Turno → Home/Jugar de nuevo
```

### Principios de UX:
1. **Diseño lúdico y colorido**: Paleta vibrante, animaciones bouncy, iconos expresivos
2. **Feedback inmediato**: Sonidos + animaciones en cada interacción
3. **Navegación de máximo 2 taps** para llegar a jugar
4. **Estados vacíos amigables** con ilustraciones y CTAs claros
5. **Modo offline**: La app debe funcionar sin conexión (datos pre-cacheados)
6. **Responsive**: Optimizado para móvil pero funcional en tablet/desktop

### Paleta de Colores Propuesta:
- **Primario**: #6C5CE7 (Violeta vibrante)
- **Secundario**: #00D2D3 (Turquesa)
- **Acierto**: #00B894 (Verde esmeralda)
- **Error/Pasar**: #FF6B6B (Rojo coral)
- **Fondo**: #1A1A2E (Azul oscuro profundo)
- **Superficie**: #16213E (Azul medio)
- **Texto**: #FFFFFF y #A0A0C0

### Categorías Iniciales (desbloqueadas):
1. 🐾 Animales / Animals
2. 🍕 Comida / Food
3. ⚽ Deportes / Sports
4. 🎬 Películas / Movies (bloqueada - 500pts)
5. 🎵 Música / Music (bloqueada - 500pts)
6. 💼 Profesiones / Professions
7. 🌍 Países / Countries
8. 🦸 Superhéroes / Superheroes (bloqueada - 750pts)
9. 📺 Series TV / TV Shows (bloqueada - 750pts)
10. 🎮 Videojuegos / Video Games (bloqueada - 1000pts)
11. 📚 Libros / Books (bloqueada - 1000pts)
12. 🎭 Teatro / Theater (bloqueada - 1500pts)

---

## 5. Configuración de Partida (Defaults)
- **Palabras por turno**: 10 (rango: 5-20)
- **Tiempo por palabra**: 60 segundos (rango: 30-120)
- **Puntos por acierto**: 10 (rango: 5-25)

---

**Estado**: ✅ Research completado y listo para aprobación
**Siguiente paso**: Prototipado visual en Google Stitch
