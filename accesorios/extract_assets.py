"""
SCRIPT: Extractor de Assets de Mímica Pro
==========================================
Extrae iconos, fondos, botones y elementos UI de las capturas de Stitch.
Recorta regiones específicas de cada imagen basándose en las posiciones de los elementos.
"""

from PIL import Image
import os

# Crear estructura de carpetas para assets
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

dirs = [
    os.path.join(ASSETS_DIR, "icons"),         # Iconos 3D de categorías
    os.path.join(ASSETS_DIR, "icons_extra"),    # Iconos extra (imagen 2)
    os.path.join(ASSETS_DIR, "backgrounds"),    # Fondos completos
    os.path.join(ASSETS_DIR, "buttons"),        # Botones recortados
    os.path.join(ASSETS_DIR, "ui_elements"),    # Elementos UI (timer, cards, etc.)
    os.path.join(ASSETS_DIR, "screens"),        # Pantallas completas redimensionadas
    os.path.join(ASSETS_DIR, "logo"),           # Logo del juego
]

for d in dirs:
    os.makedirs(d, exist_ok=True)

print("=" * 60)
print("  EXTRACTOR DE ASSETS - MÍMICA PRO")
print("=" * 60)

# ====================================================================
# IMAGEN 8 (8.png) - Icon Sheet principal (fondo gris, iconos limpios)
# Esta es la MEJOR fuente para extraer iconos individuales
# ====================================================================
print("\n[1/7] Extrayendo iconos del Icon Sheet (8.png)...")
try:
    img8 = Image.open(os.path.join(BASE_DIR, "8.png"))
    w, h = img8.size
    print(f"  Tamaño: {w}x{h}")
    
    # Los iconos están en un grid 2x5 con labels debajo
    # Basándonos en la imagen vista: grid de 2 columnas
    # Fila 1: Animales (león), Películas (popcorn)
    # Fila 2: Deportes (basket), Acción (rayo)
    # Fila 3: Héroes (escudo), Música (headphones)
    # Fila 4: Profesiones (estetoscopio), Objetos (lámpara)
    # Fila 5: Fiesta (confetti), Verano (sol)
    
    col_left = int(w * 0.05)
    col_right = int(w * 0.5)
    col_left_end = int(w * 0.48)
    col_right_end = int(w * 0.95)
    
    icon_defs = [
        # (name, col_start, col_end, row_start_pct, row_end_pct)
        ("animales_leon",     col_left,  col_left_end,  0.14, 0.30),
        ("peliculas_popcorn", col_right, col_right_end, 0.14, 0.30),
        ("deportes_basket",   col_left,  col_left_end,  0.31, 0.47),
        ("accion_rayo",       col_right, col_right_end, 0.31, 0.47),
        ("heroes_escudo",     col_left,  col_left_end,  0.48, 0.63),
        ("musica_headphones", col_right, col_right_end, 0.48, 0.63),
        ("profesiones_steth", col_left,  col_left_end,  0.64, 0.79),
        ("objetos_lampara",   col_right, col_right_end, 0.64, 0.79),
        ("fiesta_confetti",   col_left,  col_left_end,  0.80, 0.96),
        ("verano_sol",        col_right, col_right_end, 0.80, 0.96),
    ]
    
    for name, x1, x2, y1_pct, y2_pct in icon_defs:
        y1 = int(h * y1_pct)
        y2 = int(h * y2_pct)
        icon = img8.crop((x1, y1, x2, y2))
        icon_path = os.path.join(ASSETS_DIR, "icons", f"{name}.png")
        icon.save(icon_path)
        print(f"  ✓ {name}.png ({icon.size[0]}x{icon.size[1]})")
    
except Exception as e:
    print(f"  ✗ Error: {e}")

# ====================================================================
# IMAGEN 2 (2.png) - Extra Icons Sheet (Heroes, Professions, etc.)
# ====================================================================
print("\n[2/7] Extrayendo iconos extra (2.png)...")
try:
    img2 = Image.open(os.path.join(BASE_DIR, "2.png"))
    w, h = img2.size
    print(f"  Tamaño: {w}x{h}")
    
    extra_defs = [
        ("heroes_mask",       0.02, 0.33, 0.15, 0.35),
        ("professions_steth", 0.33, 0.66, 0.15, 0.35),
        ("magic_wand",        0.55, 0.95, 0.15, 0.35),
        ("travel_suitcase",   0.02, 0.33, 0.42, 0.60),
        ("food_pizza",        0.33, 0.66, 0.42, 0.60),
        ("games_controller",  0.55, 0.95, 0.42, 0.60),
        ("space_planet",      0.10, 0.48, 0.68, 0.88),
        ("surprise_gift",     0.48, 0.85, 0.68, 0.88),
    ]
    
    for name, x1_pct, x2_pct, y1_pct, y2_pct in extra_defs:
        x1, x2 = int(w * x1_pct), int(w * x2_pct)
        y1, y2 = int(h * y1_pct), int(h * y2_pct)
        icon = img2.crop((x1, y1, x2, y2))
        icon_path = os.path.join(ASSETS_DIR, "icons_extra", f"{name}.png")
        icon.save(icon_path)
        print(f"  ✓ {name}.png ({icon.size[0]}x{icon.size[1]})")
        
except Exception as e:
    print(f"  ✗ Error: {e}")

# ====================================================================
# FONDOS - Extraer fondos completos de pantallas clave
# ====================================================================
print("\n[3/7] Guardando fondos de pantallas...")
try:
    backgrounds = {
        "bg_home": "5.png",        # Home con gradiente azul mágico
        "bg_game": "6.png",        # Game screen
        "bg_results": "9.png",     # Results (gradiente azul-púrpura)
        "bg_settings": "10.png",   # Settings (fondo colorido con engranajes)
        "bg_splash": "11.png",     # Splash screen
        "bg_howtoplay": "3.png",   # Cómo jugar
    }
    
    for name, filename in backgrounds.items():
        filepath = os.path.join(BASE_DIR, filename)
        if os.path.exists(filepath):
            img = Image.open(filepath)
            # Guardar en tamaño completo como fondo de referencia
            bg_path = os.path.join(ASSETS_DIR, "backgrounds", f"{name}.png")
            img.save(bg_path)
            print(f"  ✓ {name}.png ({img.size[0]}x{img.size[1]})")
except Exception as e:
    print(f"  ✗ Error: {e}")

# ====================================================================
# BOTONES - Extraer botones de las pantallas
# ====================================================================
print("\n[4/7] Extrayendo botones...")
try:
    # Botón EMPEZAR del home (5.png) - verde con borde dorado
    img5 = Image.open(os.path.join(BASE_DIR, "5.png"))
    w, h = img5.size
    btn_empezar = img5.crop((int(w*0.08), int(h*0.82), int(w*0.92), int(h*0.91)))
    btn_empezar.save(os.path.join(ASSETS_DIR, "buttons", "btn_empezar_green.png"))
    print(f"  ✓ btn_empezar_green.png")
    
    # Botón EMPEZAR azul del home variante (4.png)
    img4 = Image.open(os.path.join(BASE_DIR, "4.png"))
    w, h = img4.size
    btn_empezar2 = img4.crop((int(w*0.08), int(h*0.82), int(w*0.92), int(h*0.91)))
    btn_empezar2.save(os.path.join(ASSETS_DIR, "buttons", "btn_empezar_blue.png"))
    print(f"  ✓ btn_empezar_blue.png")
    
    # Botones PASAR y CORRECTO del game screen (6.png)
    img6 = Image.open(os.path.join(BASE_DIR, "6.png"))
    w, h = img6.size
    btn_pasar = img6.crop((int(w*0.04), int(h*0.85), int(w*0.48), int(h*0.94)))
    btn_pasar.save(os.path.join(ASSETS_DIR, "buttons", "btn_pasar.png"))
    print(f"  ✓ btn_pasar.png")
    
    btn_correcto = img6.crop((int(w*0.52), int(h*0.85), int(w*0.96), int(h*0.94)))
    btn_correcto.save(os.path.join(ASSETS_DIR, "buttons", "btn_correcto.png"))
    print(f"  ✓ btn_correcto.png")
    
    # Botón ENTENDIDO del how to play (3.png)
    img3 = Image.open(os.path.join(BASE_DIR, "3.png"))
    w, h = img3.size
    btn_entendido = img3.crop((int(w*0.08), int(h*0.88), int(w*0.92), int(h*0.96)))
    btn_entendido.save(os.path.join(ASSETS_DIR, "buttons", "btn_entendido.png"))
    print(f"  ✓ btn_entendido.png")
    
    # Botón GUARDAR del settings (10.png)
    img10 = Image.open(os.path.join(BASE_DIR, "10.png"))
    w, h = img10.size
    btn_guardar = img10.crop((int(w*0.10), int(h*0.88), int(w*0.90), int(h*0.96)))
    btn_guardar.save(os.path.join(ASSETS_DIR, "buttons", "btn_guardar.png"))
    print(f"  ✓ btn_guardar.png")
    
    # Botones VOLVER A JUGAR y MENÚ del results (9.png)
    img9 = Image.open(os.path.join(BASE_DIR, "9.png"))
    w, h = img9.size
    btn_volver = img9.crop((int(w*0.04), int(h*0.84), int(w*0.48), int(h*0.94)))
    btn_volver.save(os.path.join(ASSETS_DIR, "buttons", "btn_volver_jugar.png"))
    print(f"  ✓ btn_volver_jugar.png")
    
    btn_menu = img9.crop((int(w*0.52), int(h*0.84), int(w*0.96), int(h*0.94)))
    btn_menu.save(os.path.join(ASSETS_DIR, "buttons", "btn_menu.png"))
    print(f"  ✓ btn_menu.png")
    
    # Botones del modal de salida (12.png)
    img12 = Image.open(os.path.join(BASE_DIR, "12.png"))
    w, h = img12.size
    btn_no_seguir = img12.crop((int(w*0.12), int(h*0.49), int(w*0.88), int(h*0.57)))
    btn_no_seguir.save(os.path.join(ASSETS_DIR, "buttons", "btn_no_seguir.png"))
    print(f"  ✓ btn_no_seguir.png")
    
    btn_si_salir = img12.crop((int(w*0.12), int(h*0.58), int(w*0.88), int(h*0.66)))
    btn_si_salir.save(os.path.join(ASSETS_DIR, "buttons", "btn_si_salir.png"))
    print(f"  ✓ btn_si_salir.png")

except Exception as e:
    print(f"  ✗ Error: {e}")

# ====================================================================
# UI ELEMENTS - Timer, Cards, Logo, etc.
# ====================================================================
print("\n[5/7] Extrayendo elementos UI...")
try:
    # Timer circular del game screen (6.png)
    img6 = Image.open(os.path.join(BASE_DIR, "6.png"))
    w, h = img6.size
    timer = img6.crop((int(w*0.22), int(h*0.06), int(w*0.78), int(h*0.28)))
    timer.save(os.path.join(ASSETS_DIR, "ui_elements", "timer_circle.png"))
    print(f"  ✓ timer_circle.png")
    
    # Word card del game screen
    card = img6.crop((int(w*0.06), int(h*0.30), int(w*0.94), int(h*0.82)))
    card.save(os.path.join(ASSETS_DIR, "ui_elements", "word_card.png"))
    print(f"  ✓ word_card.png")
    
    # Home button rojo del game screen
    home_btn = img6.crop((int(w*0.02), int(h*0.03), int(w*0.16), int(h*0.11)))
    home_btn.save(os.path.join(ASSETS_DIR, "ui_elements", "home_button_red.png"))
    print(f"  ✓ home_button_red.png")
    
    # Trofeo del results (9.png) 
    img9 = Image.open(os.path.join(BASE_DIR, "9.png"))
    w, h = img9.size
    trophy = img9.crop((int(w*0.15), int(h*0.15), int(w*0.85), int(h*0.65)))
    trophy.save(os.path.join(ASSETS_DIR, "ui_elements", "trophy_podium.png"))
    print(f"  ✓ trophy_podium.png")
    
    # Score card del results
    score_card = img9.crop((int(w*0.05), int(h*0.58), int(w*0.95), int(h*0.82)))
    score_card.save(os.path.join(ASSETS_DIR, "ui_elements", "score_card.png"))
    print(f"  ✓ score_card.png")
    
    # Modal de salida completo (12.png)
    img12 = Image.open(os.path.join(BASE_DIR, "12.png"))
    w, h = img12.size
    modal = img12.crop((int(w*0.05), int(h*0.22), int(w*0.95), int(h*0.72)))
    modal.save(os.path.join(ASSETS_DIR, "ui_elements", "exit_modal.png"))
    print(f"  ✓ exit_modal.png")
    
    # Thinking emoji del modal
    emoji = img12.crop((int(w*0.32), int(h*0.22), int(w*0.68), int(h*0.35)))
    emoji.save(os.path.join(ASSETS_DIR, "ui_elements", "thinking_emoji.png"))
    print(f"  ✓ thinking_emoji.png")
    
    # Settings modal card (10.png)
    img10 = Image.open(os.path.join(BASE_DIR, "10.png"))
    w, h = img10.size
    settings_card = img10.crop((int(w*0.08), int(h*0.12), int(w*0.92), int(h*0.85)))
    settings_card.save(os.path.join(ASSETS_DIR, "ui_elements", "settings_card.png"))
    print(f"  ✓ settings_card.png")
    
    # Close X button del settings
    close_btn = img10.crop((int(w*0.02), int(h*0.04), int(w*0.22), int(h*0.12)))
    close_btn.save(os.path.join(ASSETS_DIR, "ui_elements", "close_button_x.png"))
    print(f"  ✓ close_button_x.png")

except Exception as e:
    print(f"  ✗ Error: {e}")

# ====================================================================
# LOGO - Extraer logo de diferentes pantallas
# ====================================================================
print("\n[6/7] Extrayendo logos...")
try:
    # Logo del splash (11.png) - grande y limpio
    img11 = Image.open(os.path.join(BASE_DIR, "11.png"))
    w, h = img11.size
    logo_splash = img11.crop((int(w*0.05), int(h*0.28), int(w*0.95), int(h*0.50)))
    logo_splash.save(os.path.join(ASSETS_DIR, "logo", "logo_mimica_pro_splash.png"))
    print(f"  ✓ logo_mimica_pro_splash.png")
    
    # Badge "FAMILY CHARADES" del splash
    badge = img11.crop((int(w*0.20), int(h*0.48), int(w*0.80), int(h*0.53)))
    badge.save(os.path.join(ASSETS_DIR, "logo", "badge_family_charades.png"))
    print(f"  ✓ badge_family_charades.png")
    
    # Loading bar del splash
    loadbar = img11.crop((int(w*0.08), int(h*0.87), int(w*0.92), int(h*0.92)))
    loadbar.save(os.path.join(ASSETS_DIR, "logo", "loading_bar.png"))
    print(f"  ✓ loading_bar.png")
    
    # Logo del home (5.png) - más pequeño
    img5 = Image.open(os.path.join(BASE_DIR, "5.png"))
    w, h = img5.size
    logo_home = img5.crop((int(w*0.10), int(h*0.04), int(w*0.90), int(h*0.16)))
    logo_home.save(os.path.join(ASSETS_DIR, "logo", "logo_mimica_pro_home.png"))
    print(f"  ✓ logo_mimica_pro_home.png")

except Exception as e:
    print(f"  ✗ Error: {e}")

# ====================================================================
# SCREENS - Guardar pantallas redimensionadas para referencia
# ====================================================================
print("\n[7/7] Guardando pantallas de referencia (390px width)...")
try:
    screen_map = {
        "01_design_system": "1.png",
        "02_extra_icons": "2.png",
        "03_como_jugar": "3.png",
        "04_home_heroes": "4.png",
        "05_home_deportes": "5.png",
        "06_game_screen": "6.png",
        "07_design_system_full": "7.png",
        "08_icon_sheet": "8.png",
        "09_results": "9.png",
        "10_settings": "10.png",
        "11_splash": "11.png",
        "12_exit_modal": "12.png",
    }
    
    for name, filename in screen_map.items():
        filepath = os.path.join(BASE_DIR, filename)
        if os.path.exists(filepath):
            img = Image.open(filepath)
            # Redimensionar a 390px de ancho manteniendo proporción
            ratio = 390 / img.width
            new_h = int(img.height * ratio)
            img_resized = img.resize((390, new_h), Image.LANCZOS)
            screen_path = os.path.join(ASSETS_DIR, "screens", f"{name}.png")
            img_resized.save(screen_path)
            print(f"  ✓ {name}.png (390x{new_h})")
except Exception as e:
    print(f"  ✗ Error: {e}")

# ====================================================================
# RESUMEN
# ====================================================================
print("\n" + "=" * 60)
print("  ✅ EXTRACCIÓN COMPLETADA")
print("=" * 60)
print(f"\n  Assets guardados en: {ASSETS_DIR}")
print(f"  Carpetas creadas:")
for d in dirs:
    count = len([f for f in os.listdir(d) if f.endswith('.png')]) if os.path.exists(d) else 0
    print(f"    📁 {os.path.basename(d)}/  ({count} archivos)")
print()
