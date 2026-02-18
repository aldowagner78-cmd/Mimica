"""
SCRIPT V2: Extractor de Assets de Mímica Pro - COORDENADAS CORREGIDAS
======================================================================
Imágenes fuente:
  1.png:  589x1600  (Design System compacto)
  2.png:  768x1376  (Extra Icons Sheet)
  3.png:  768x1376  (Cómo Jugar)
  4.png:  768x1376  (Home - Héroes/Acción)
  5.png:  768x1376  (Home - Deportes/Música)
  6.png:  768x1376  (Game Screen)
  7.png:  768x1376  (Design System Full)
  8.png:  768x1376  (Icon Sheet - fondo gris)
  9.png:  768x1376  (Results)
  10.png: 768x1376  (Settings)
  11.png: 706x1600  (Splash)
  12.png: 706x1600  (Exit Modal)
"""

from PIL import Image
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

# Limpiar y recrear
import shutil
if os.path.exists(ASSETS_DIR):
    shutil.rmtree(ASSETS_DIR)

dirs = {
    "icons": os.path.join(ASSETS_DIR, "icons"),
    "icons_extra": os.path.join(ASSETS_DIR, "icons_extra"),
    "backgrounds": os.path.join(ASSETS_DIR, "backgrounds"),
    "buttons": os.path.join(ASSETS_DIR, "buttons"),
    "ui": os.path.join(ASSETS_DIR, "ui_elements"),
    "logo": os.path.join(ASSETS_DIR, "logo"),
    "screens": os.path.join(ASSETS_DIR, "screens"),
}
for d in dirs.values():
    os.makedirs(d, exist_ok=True)

def crop_save(img, box, path, label=""):
    """Crop and save with validation"""
    cropped = img.crop(box)
    cropped.save(path)
    print(f"  ✓ {label or os.path.basename(path)} ({cropped.size[0]}x{cropped.size[1]})")
    return cropped

print("=" * 60)
print("  EXTRACTOR DE ASSETS V2 - MÍMICA PRO")
print("=" * 60)

# ============================================================
# 1) ICON SHEET (8.png) - 768x1376, fondo gris claro
# Grid 2 columnas. Iconos SIN el texto label debajo.
# ============================================================
print("\n[1] Iconos principales (8.png - Icon Sheet)...")
img8 = Image.open(os.path.join(BASE_DIR, "8.png"))  # 768x1376

# Medidas verificadas visualmente:
# Columna izquierda: x=40..350, Columna derecha: x=400..720
# Cada icono ocupa ~180px de alto (solo el gráfico sin label)
# Título ocupa hasta y~190

icons_8 = [
    # (nombre, x1, y1, x2, y2) - solo el icono sin texto
    ("animales_leon",      40,  200,  350,  410),
    ("peliculas_popcorn", 400,  200,  720,  410),
    ("deportes_basket",    40,  430,  350,  630),
    ("accion_rayo",       400,  430,  720,  630),
    ("heroes_escudo",      40,  650,  350,  850),
    ("musica_headphones", 400,  650,  720,  850),
    ("profesiones_steth",  40,  880,  350, 1060),
    ("objetos_lampara",   400,  880,  720, 1060),
    ("fiesta_confetti",    40, 1080,  350, 1280),
    ("verano_sol",        400, 1080,  720, 1280),
]

for name, x1, y1, x2, y2 in icons_8:
    crop_save(img8, (x1, y1, x2, y2), os.path.join(dirs["icons"], f"{name}.png"), name)

# ============================================================
# 2) EXTRA ICONS (2.png) - 768x1376
# 3 columnas x 3 filas, con título arriba
# ============================================================
print("\n[2] Iconos extra (2.png)...")
img2 = Image.open(os.path.join(BASE_DIR, "2.png"))  # 768x1376

icons_extra = [
    # Fila 1 (y ~230..430)
    ("heroes_mask",        30, 230, 260, 430),
    ("professions_steth", 270, 230, 500, 430),
    ("magic_wand",        500, 230, 740, 430),
    # Fila 2 (y ~530..730)
    ("travel_suitcase",    30, 530, 260, 730),
    ("food_pizza",        270, 530, 500, 730),
    ("games_controller",  500, 530, 740, 730),
    # Fila 3 (y ~830..1060)
    ("space_planet",      110, 830, 370, 1060),
    ("surprise_gift",     400, 830, 650, 1060),
]

for name, x1, y1, x2, y2 in icons_extra:
    crop_save(img2, (x1, y1, x2, y2), os.path.join(dirs["icons_extra"], f"{name}.png"), name)

# ============================================================
# 3) BOTONES - De varias pantallas (todos 768x1376 excepto 12)
# ============================================================
print("\n[3] Botones...")

# --- Botón EMPEZAR verde (5.png) ---
img5 = Image.open(os.path.join(BASE_DIR, "5.png"))  # 768x1376
crop_save(img5, (55, 1120, 710, 1240), os.path.join(dirs["buttons"], "btn_empezar_green.png"), "EMPEZAR verde")

# --- Botón EMPEZAR azul (4.png) ---
img4 = Image.open(os.path.join(BASE_DIR, "4.png"))  # 768x1376
crop_save(img4, (55, 1120, 710, 1240), os.path.join(dirs["buttons"], "btn_empezar_blue.png"), "EMPEZAR azul")

# --- Botones PASAR y CORRECTO (6.png) ---
img6 = Image.open(os.path.join(BASE_DIR, "6.png"))  # 768x1376
crop_save(img6, (30, 1150, 370, 1290), os.path.join(dirs["buttons"], "btn_pasar.png"), "PASAR")
crop_save(img6, (395, 1150, 740, 1290), os.path.join(dirs["buttons"], "btn_correcto.png"), "CORRECTO")

# --- Botón ENTENDIDO (3.png) ---
img3 = Image.open(os.path.join(BASE_DIR, "3.png"))  # 768x1376
crop_save(img3, (80, 1190, 690, 1320), os.path.join(dirs["buttons"], "btn_entendido.png"), "ENTENDIDO")

# --- Botón GUARDAR (10.png) ---
img10 = Image.open(os.path.join(BASE_DIR, "10.png"))  # 768x1376
crop_save(img10, (80, 1200, 690, 1330), os.path.join(dirs["buttons"], "btn_guardar.png"), "GUARDAR")

# --- Botones VOLVER A JUGAR y MENÚ (9.png) ---
img9 = Image.open(os.path.join(BASE_DIR, "9.png"))  # 768x1376
crop_save(img9, (30, 1140, 370, 1280), os.path.join(dirs["buttons"], "btn_volver_jugar.png"), "VOLVER A JUGAR")
crop_save(img9, (395, 1140, 740, 1280), os.path.join(dirs["buttons"], "btn_menu.png"), "MENÚ")

# --- Botones modal de salida (12.png) - 706x1600 ---
img12 = Image.open(os.path.join(BASE_DIR, "12.png"))  # 706x1600
crop_save(img12, (85, 760, 620, 880), os.path.join(dirs["buttons"], "btn_no_seguir.png"), "NO, SEGUIR")
crop_save(img12, (85, 900, 620, 1020), os.path.join(dirs["buttons"], "btn_si_salir.png"), "SÍ, SALIR")

# ============================================================
# 4) UI ELEMENTS
# ============================================================
print("\n[4] Elementos UI...")

# Timer circular (6.png)
crop_save(img6, (220, 60, 550, 390), os.path.join(dirs["ui"], "timer_circle.png"), "Timer")

# Word card (6.png)
crop_save(img6, (50, 420, 720, 1100), os.path.join(dirs["ui"], "word_card.png"), "Word Card")

# Home button rojo (6.png)
crop_save(img6, (15, 40, 130, 155), os.path.join(dirs["ui"], "home_button_red.png"), "Home button")

# Trofeo + podio SIN texto (9.png)
crop_save(img9, (80, 200, 690, 830), os.path.join(dirs["ui"], "trophy_podium.png"), "Trofeo + podio")

# Score card SIN PUNTUACIÓN text invadiendo (9.png)
crop_save(img9, (50, 810, 720, 1100), os.path.join(dirs["ui"], "score_card.png"), "Score card")

# Modal de salida completo (12.png)
crop_save(img12, (45, 430, 660, 1060), os.path.join(dirs["ui"], "exit_modal.png"), "Exit modal")

# Thinking emoji (12.png)
crop_save(img12, (260, 420, 440, 620), os.path.join(dirs["ui"], "thinking_emoji.png"), "Thinking emoji")

# Settings card completo (10.png)
crop_save(img10, (55, 150, 715, 1170), os.path.join(dirs["ui"], "settings_card.png"), "Settings card")

# Close X button (10.png)
crop_save(img10, (20, 55, 170, 180), os.path.join(dirs["ui"], "close_button_x.png"), "Close X")

# How to play cards individuales (3.png)
crop_save(img3, (30, 240, 270, 1080), os.path.join(dirs["ui"], "howto_card_1.png"), "HowTo card 1")
crop_save(img3, (275, 240, 500, 1080), os.path.join(dirs["ui"], "howto_card_2.png"), "HowTo card 2")
crop_save(img3, (505, 240, 740, 1080), os.path.join(dirs["ui"], "howto_card_3.png"), "HowTo card 3")

# Icons from how-to-play cards (just the icon squares)
crop_save(img3, (65, 280, 235, 450), os.path.join(dirs["ui"], "howto_icon_leon.png"), "HowTo Icon León")
crop_save(img3, (310, 280, 470, 450), os.path.join(dirs["ui"], "howto_icon_person.png"), "HowTo Icon Persona")
crop_save(img3, (540, 280, 710, 450), os.path.join(dirs["ui"], "howto_icon_trophy.png"), "HowTo Icon Trofeo")

# Language flags from settings (10.png)
crop_save(img10, (105, 350, 365, 440), os.path.join(dirs["ui"], "lang_btn_es.png"), "Idioma ES")
crop_save(img10, (390, 350, 650, 440), os.path.join(dirs["ui"], "lang_btn_en.png"), "Idioma EN")

# Toggle switches from settings (10.png)
crop_save(img10, (420, 485, 650, 570), os.path.join(dirs["ui"], "toggle_on.png"), "Toggle ON")

# ============================================================
# 5) LOGOS
# ============================================================
print("\n[5] Logos...")

# Logo splash (11.png) - 706x1600
img11 = Image.open(os.path.join(BASE_DIR, "11.png"))
crop_save(img11, (80, 450, 630, 720), os.path.join(dirs["logo"], "logo_mimica_pro_splash.png"), "Logo Splash")

# Badge FAMILY CHARADES
crop_save(img11, (155, 730, 550, 790), os.path.join(dirs["logo"], "badge_family_charades.png"), "Badge")

# Loading bar
crop_save(img11, (55, 1370, 650, 1420), os.path.join(dirs["logo"], "loading_bar.png"), "Loading bar")

# Logo home (4.png o 5.png)
crop_save(img5, (80, 55, 680, 200), os.path.join(dirs["logo"], "logo_mimica_pro_home.png"), "Logo Home")

# Title "Cómo Jugar" (3.png)
crop_save(img3, (100, 50, 670, 220), os.path.join(dirs["logo"], "title_como_jugar.png"), "Cómo Jugar")

# Title "MÍMICA PRO RESULTADOS" (9.png)
crop_save(img9, (50, 30, 720, 200), os.path.join(dirs["logo"], "title_resultados.png"), "Resultados")

# Design system botones de referencia (7.png)
img7 = Image.open(os.path.join(BASE_DIR, "7.png"))
crop_save(img7, (40, 600, 290, 700), os.path.join(dirs["buttons"], "ref_empezar.png"), "Ref EMPEZAR")
crop_save(img7, (310, 600, 510, 700), os.path.join(dirs["buttons"], "ref_pasar.png"), "Ref PASAR")
crop_save(img7, (530, 600, 720, 700), os.path.join(dirs["buttons"], "ref_menu.png"), "Ref MENÚ")

# Category cards from design system (7.png) - UI Elements row at bottom
crop_save(img7, (25, 1080, 160, 1260), os.path.join(dirs["ui"], "card_animales.png"), "Card Animales")
crop_save(img7, (170, 1080, 310, 1260), os.path.join(dirs["ui"], "card_peliculas.png"), "Card Películas")
crop_save(img7, (320, 1080, 460, 1260), os.path.join(dirs["ui"], "card_heroes.png"), "Card Héroes")
crop_save(img7, (470, 1080, 600, 1260), os.path.join(dirs["ui"], "card_accion.png"), "Card Acción")
crop_save(img7, (610, 1080, 760, 1310), os.path.join(dirs["ui"], "card_timer_neon.png"), "Timer Neon")

# ============================================================
# 6) FONDOS
# ============================================================
print("\n[6] Fondos completos...")
bg_map = {
    "bg_home.png": "5.png",
    "bg_game.png": "6.png",
    "bg_results.png": "9.png",
    "bg_settings.png": "10.png",
    "bg_splash.png": "11.png",
    "bg_howtoplay.png": "3.png",
}
for name, src in bg_map.items():
    img = Image.open(os.path.join(BASE_DIR, src))
    img.save(os.path.join(dirs["backgrounds"], name))
    print(f"  ✓ {name} ({img.size[0]}x{img.size[1]})")

# ============================================================
# 7) SCREENS redimensionadas
# ============================================================
print("\n[7] Pantallas de referencia...")
screen_map = {
    "01_design_system.png": "1.png",
    "02_extra_icons.png": "2.png",
    "03_como_jugar.png": "3.png",
    "04_home_heroes.png": "4.png",
    "05_home_deportes.png": "5.png",
    "06_game_screen.png": "6.png",
    "07_design_system_full.png": "7.png",
    "08_icon_sheet.png": "8.png",
    "09_results.png": "9.png",
    "10_settings.png": "10.png",
    "11_splash.png": "11.png",
    "12_exit_modal.png": "12.png",
}
for name, src in screen_map.items():
    img = Image.open(os.path.join(BASE_DIR, src))
    ratio = 390 / img.width
    new_h = int(img.height * ratio)
    img_resized = img.resize((390, new_h), Image.LANCZOS)
    img_resized.save(os.path.join(dirs["screens"], name))
    print(f"  ✓ {name} (390x{new_h})")

# ============================================================
# RESUMEN
# ============================================================
print("\n" + "=" * 60)
print("  ✅ EXTRACCIÓN V2 COMPLETADA")
print("=" * 60)
total = 0
for label, d in dirs.items():
    count = len([f for f in os.listdir(d) if f.endswith('.png')])
    total += count
    print(f"  📁 {label:12s} → {count} archivos")
print(f"\n  TOTAL: {total} assets en {ASSETS_DIR}")
