import csv
import json

def convert_database():
    csv_path = 'charadas_latam_database.csv'
    js_path = 'gameData.js'
    
    # Mapping for Icons
    category_meta = {
        'Animales': {'id': 'animales', 'icon': 'animales_leon.png'},
        'Películas': {'id': 'peliculas', 'icon': 'peliculas_popcorn.png'},
        'Héroes': {'id': 'heroes', 'icon': 'heroes_escudo.png'},
        'Acción': {'id': 'accion', 'icon': 'accion_rayo.png'},
        'Deportes': {'id': 'deportes', 'icon': 'deportes_basket.png'},
        'Música': {'id': 'musica', 'icon': 'musica_headphones.png'},
        'Profesiones': {'id': 'profesiones', 'icon': 'profesiones_steth.png'},
        'Objetos': {'id': 'objetos', 'icon': 'objetos_lampara.png'},
        'Comida': {'id': 'comida', 'icon': 'comida_pizza.png'},
        'Fiesta': {'id': 'fiesta', 'icon': 'fiesta_confetti.png'},
        'Viajes': {'id': 'viajes', 'icon': 'viajes_maleta.png'},
        'Sorpresa': {'id': 'sorpresa', 'icon': 'sorpresa_regalo.png'},
        'Verano': {'id': 'verano', 'icon': 'verano_sol.png'},
        'Juegos': {'id': 'juegos', 'icon': 'juegos_controller.png'}
    }
    
    # Data structure: hierarchy[cat_original_name]['es'/'en'][level_int] = [list of words]
    data = {}
    
    # Initialize structure
    for cat in category_meta:
        data[cat] = {
            'es': {1: [], 2: [], 3: []},
            'en': {1: [], 2: [], 3: []}
        }

    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                cat = row['Categoría'].strip()
                lvl_str = row['Nivel'].strip().lower()
                es = row['Español (Latino)'].strip()
                en = row['Inglés'].strip()
                
                # Check category validity
                if cat not in category_meta:
                    continue 
                
                # Map Level
                level = 1
                if 'media' in lvl_str or '2' in lvl_str: level = 2
                elif 'alta' in lvl_str or 'difícil' in lvl_str or 'dificil' in lvl_str or '3' in lvl_str: level = 3
                
                # Add to lists
                if es:
                    data[cat]['es'][level].append(es)
                if en:
                    data[cat]['en'][level].append(en)
                    
    except Exception as e:
        print(f"Error reading CSV: {e}")
        return

    # Generate JS content
    js_cats = []
    
    # Helper to format list as JS array string
    def to_js_list(lst):
        # Escape single quotes and backslashes
        escaped = [f"'{w.replace('\\', '\\\\').replace("'", "\\'")}'" for w in lst]
        return "[" + ", ".join(escaped) + "]"

    order = ['Animales', 'Películas', 'Héroes', 'Acción', 'Deportes', 'Música', 'Profesiones', 
             'Objetos', 'Comida', 'Fiesta', 'Viajes', 'Sorpresa', 'Verano', 'Juegos']
    
    for cat_key in order:
        if cat_key not in data: continue
        
        meta = category_meta[cat_key]
        cat_data = data[cat_key]
        
        es_obj_parts = []
        en_obj_parts = []
        for lvl in [1, 2, 3]:
            es_list = cat_data['es'][lvl]
            en_list = cat_data['en'][lvl]
            if es_list:
                es_obj_parts.append(f"{lvl}: {to_js_list(es_list)}")
            if en_list:
                en_obj_parts.append(f"{lvl}: {to_js_list(en_list)}")
        
        es_obj_str = "{\n      " + ",\n      ".join(es_obj_parts) + "\n    }"
        en_obj_str = "{\n      " + ",\n      ".join(en_obj_parts) + "\n    }"
        
        js_block = f"""  {{
    id: '{meta['id']}', icon: '{meta['icon']}',
    words_es: {es_obj_str},
    words_en: {en_obj_str}
  }}"""
        js_cats.append(js_block)

    i18n_code = """
// ===== i18n TRANSLATIONS =====
const i18n = {
  es: {
    appTitle: 'Charadas Latam',
    categories: { 
        animales: 'Animales', peliculas: 'Películas', heroes: 'Héroes', accion: 'Acción', 
        deportes: 'Deportes', musica: 'Música', profesiones: 'Profesiones', objetos: 'Objetos', 
        comida: 'Comida', fiesta: 'Fiesta', viajes: 'Viajes', sorpresa: 'Sorpresa', 
        verano: 'Verano', juegos: 'Juegos' 
    },
    empezar: 'EMPEZAR',
    config: 'Configuración',
    ayuda: 'Ayuda',
    comoJugar: 'Cómo Jugar',
    howto1Title: 'Elige una categoría',
    howto1Desc: 'Explora los temas divertidos y selecciona uno para empezar a jugar.',
    howto2Title: 'Actúa y adivina',
    howto2Desc: '¡Describe la palabra sin hablar! Tu equipo debe adivinar en el tiempo.',
    howto3Title: 'Gana puntos',
    howto3Desc: 'Acumula puntos con cada acierto y celebra la victoria.',
    entendido: 'ENTENDIDO',
    pasar: 'PASAR',
    correcto: 'CORRECTO',
    resultados: 'RESULTADOS',
    puntuacion: 'PUNTUACIÓN OBTENIDA:',
    puntuacionGanadora: 'PUNTUACIÓN GANADORA:',
    volverJugar: 'VOLVER A JUGAR',
    menu: 'MENÚ',
    configTitle: 'Configuración',
    idioma: 'Idioma / Language',
    musicaLabel: 'Música',
    vibracion: 'Vibración',
    tiempoJuego: 'Tiempo (seg)',
    dificultad: 'Dificultad',
    diff_facil: 'Fácil',
    diff_medio: 'Medio',
    diff_dificil: 'Difícil',
    equiposLabel: 'Modo Equipos',
    segundos: 'segundos',
    guardar: 'GUARDAR',
    salirTitulo: '¿QUIERES SALIR?',
    salirDesc: 'Se perderá el progreso actual.',
    noSeguir: '▶ NO, SEGUIR',
    siSalir: '✕ SÍ, SALIR',
    seleccionaCat: '¡Selecciona al menos una categoría!',
    loading: 'Cargando...',
    equipo: 'Equipo',
    ganador: '¡GANADOR!',
    empate: '¡EMPATE!',
    ronda: 'Ronda',
    turnoDe: 'Turno de:'
  },
  en: {
    appTitle: 'Charades Latam',
    categories: { 
        animales: 'Animals', peliculas: 'Movies', heroes: 'Heroes', accion: 'Action', 
        deportes: 'Sports', musica: 'Music', profesiones: 'Professions', objetos: 'Objects', 
        comida: 'Food', fiesta: 'Party', viajes: 'Travel', sorpresa: 'Surprise', 
        verano: 'Summer', juegos: 'Games' 
    },
    empezar: 'START',
    config: 'Settings',
    ayuda: 'Help',
    comoJugar: 'How to Play',
    howto1Title: 'Choose a category',
    howto1Desc: 'Pick a fun theme to start playing.',
    howto2Title: 'Act it out',
    howto2Desc: "Describe the word without talking! Your team must guess in time.",
    howto3Title: 'Score points',
    howto3Desc: 'Earn points with every correct guess and win.',
    entendido: 'GOT IT',
    pasar: 'SKIP',
    correcto: 'CORRECT',
    resultados: 'RESULTS',
    puntuacion: 'SCORE:',
    puntuacionGanadora: 'WINNING SCORE:',
    volverJugar: 'PLAY AGAIN',
    menu: 'MENU',
    configTitle: 'Settings',
    idioma: 'Language / Idioma',
    musicaLabel: 'Music',
    vibracion: 'Vibration',
    tiempoJuego: 'Time (sec)',
    dificultad: 'Difficulty',
    diff_facil: 'Easy',
    diff_medio: 'Medium',
    diff_dificil: 'Hard',
    equiposLabel: 'Team Mode',
    segundos: 'seconds',
    guardar: 'SAVE',
    salirTitulo: 'QUIT GAME?',
    salirDesc: "You will lose current progress.",
    noSeguir: '▶ NO, CONTINUE',
    siSalir: '✕ YES, QUIT',
    seleccionaCat: 'Select at least one category!',
    loading: 'Loading...',
    equipo: 'Team',
    ganador: 'WINNER!',
    empate: 'DRAW!',
    ronda: 'Round',
    turnoDe: 'Turn of:'
  }
};
"""

    full_js = "// ===== GAME DATA - CHARADAS LATAM (Generated) =====\n\nconst CATEGORIES = [\n" + ",\n\n".join(js_cats) + "\n];\n" + i18n_code
    
    # Write to file
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(full_js)
    
    print("Successfully regenerated gameData.js from charadas_latam_database.csv")

if __name__ == "__main__":
    convert_database()
