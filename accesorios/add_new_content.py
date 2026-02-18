import csv
import os

# New Data to Append
# Categories: Animales, Películas, Héroes, Acción, Deportes, Música, Profesiones, Objetos, Comida
# PLUS New: Fiesta, Viajes, Sorpresa, Verano, Juegos

new_rows = []

def add_row(cat, level, es, en):
    lvl_str = "Baja" if level == 1 else "Media" if level == 2 else "Alta"
    new_rows.append({'Categoría': cat, 'Nivel': lvl_str, 'Español (Latino)': es, 'Inglés': en})

# --- FIESTA ---
# Nivel 1
fiesta_l1_es = ["Piñata", "Globo", "Pastel", "Regalo", "Antifaz", "Confeti", "Vela", "Disfraz", "Brindis", "Música", "Baile", "DJ", "Invitación", "Guirnalda", "Gorro", "Payaso", "Mago", "Karaoke", "Foto", "Risa", "Torta", "Bebida", "Amigos", "Familia", "Juegos", "Sorpresa", "Luces", "Noche", "Boda", "Vals", "Despedida", "Cotillón", "Serpentina", "Matasuegras", "Bocaditos", "Refresco", "Hielo", "Vaso", "Plato", "Servilleta", "Mesa", "Silla", "Pista", "Bola (Disco)", "Vestido", "Traje", "Zapatos", "Maquillaje", "Peinado", "Perfume"]
fiesta_l1_en = ["Piñata", "Balloon", "Cake", "Gift", "Mask", "Confetti", "Candle", "Costume", "Toast", "Music", "Dance", "DJ", "Invitation", "Garland", "Hat", "Clown", "Magician", "Karaoke", "Photo", "Laughter", "Cake", "Drink", "Friends", "Family", "Games", "Surprise", "Lights", "Night", "Wedding", "Waltz", "Farewell", "Party favors", "Streamer", "Noisemaker", "Snacks", "Soda", "Ice", "Cup", "Plate", "Napkin", "Table", "Chair", "Dance floor", "Disco ball", "Dress", "Suit", "Shoes", "Makeup", "Hairstyle", "Perfume"]
for i in range(len(fiesta_l1_es)): add_row("Fiesta", 1, fiesta_l1_es[i], fiesta_l1_en[i])

# Nivel 2
fiesta_l2_es = ["Romper la piñata", "Soplar las velas", "Abrir los regalos", "Bailar el vals", "Comer pastel", "Cantar cumpleaños feliz", "Inflar un globo", "Ponerse un disfraz", "Lanzar confeti", "Brindar con copas", "Repartir invitaciones", "Decorar el salón", "Envolver un regalo", "Sacar una foto", "Jugar a las sillas", "Bailar con la abuela", "Contar un chiste", "Hacer magia", "Servir la comida", "Limpiar el desastre"]
fiesta_l2_en = ["Breaking the piñata", "Blowing out candles", "Opening gifts", "Dancing the waltz", "Eating cake", "Singing happy birthday", "Inflating a balloon", "Putting on a costume", "Throwing confetti", "Toasting with glasses", "Handing out invitations", "Decorating the room", "Wrapping a gift", "Taking a photo", "Playing musical chairs", "Dancing with grandma", "Telling a joke", "Doing magic", "Serving food", "Cleaning the mess"]
for i in range(len(fiesta_l2_es)): add_row("Fiesta", 2, fiesta_l2_es[i], fiesta_l2_en[i])

# Nivel 3
fiesta_l3_es = ["Un payaso perdiendo sus zapatos", "Intentar morder la manzana colgada", "Una sorpresa que sale mal", "Bailar la conga con la abuela", "El DJ que se queda dormido", "Abrir un regalo que no te gusta", "Caerse encima del pastel", "Un mago revelando su truco", "Cantar karaoke desafinado", "Quedarse encerrado en el baño de la fiesta"]
fiesta_l3_en = ["A clown losing his shoes", "Trying to bite the hanging apple", "A surprise going wrong", "Dancing the conga with grandma", "The DJ falling asleep", "Opening a gift you don't like", "Falling on the cake", "A magician revealing his trick", "Singing karaoke out of tune", "Getting locked in the party bathroom"]
for i in range(len(fiesta_l3_es)): add_row("Fiesta", 3, fiesta_l3_es[i], fiesta_l3_en[i])


# --- VIAJES ---
# Nivel 1
viajes_l1_es = ["Avión", "Maleta", "Pasaporte", "Playa", "Montaña", "Hotel", "Mapa", "Tren", "Foto", "Turista", "Mochila", "Carpa", "Brújula", "Aeropuerto", "Isla", "Boleto", "Guía", "Museo", "Souvenir", "Cámara", "Selva", "Desierto", "Nieve", "Esquí", "Crucero", "Bote", "Remo", "Salvavidas", "Sol", "Arena", "Mar", "Ola", "Piscina", "Bikini", "Lentes", "Gorra", "Protector", "Toalla", "Sandalia", "Caminata", "Excursión", "Safari", "Zoológico", "Parque", "Monumento", "Estatua", "Puente", "Edificio", "Calle", "Taxi"]
viajes_l1_en = ["Airplane", "Suitcase", "Passport", "Beach", "Mountain", "Hotel", "Map", "Train", "Photo", "Tourist", "Backpack", "Tent", "Compass", "Airport", "Island", "Ticket", "Guide", "Museum", "Souvenir", "Camera", "Jungle", "Desert", "Snow", "Ski", "Cruise", "Boat", "Paddle", "Life jacket", "Sun", "Sand", "Sea", "Wave", "Pool", "Bikini", "Glasses", "Cap", "Sunscreen", "Towel", "Sandal", "Hike", "Excursion", "Safari", "Zoo", "Park", "Monument", "Statue", "Bridge", "Building", "Street", "Taxi"]
for i in range(len(viajes_l1_es)): add_row("Viajes", 1, viajes_l1_es[i], viajes_l1_en[i])

# Nivel 2
viajes_l2_es = ["Perder el vuelo", "Armar la carpa", "Sacar una foto", "Nadar en el mar", "Subir la montaña", "Hacer la maleta", "Pedir un taxi", "Mirar el mapa", "Comprar recuerdos", "Dormir en el avión", "Esperar el autobús", "Alquilar un auto", "Probar comida rara", "Leer una guía", "Cruzar un puente", "Visitar un museo", "Hacer senderismo", "Encender una fogata", "Buscar el hotel", "Perder el pasaporte"]
viajes_l2_en = ["Missing the flight", "Setting up the tent", "Taking a photo", "Swimming in the sea", "Climbing the mountain", "Packing the suitcase", "Ordering a taxi", "Looking at the map", "Buying souvenirs", "Sleeping on the plane", "Waiting for the bus", "Renting a car", "Trying weird food", "Reading a guide", "Crossing a bridge", "Visiting a museum", "Hiking", "Starting a bonfire", "Looking for the hotel", "Losing the passport"]
for i in range(len(viajes_l2_es)): add_row("Viajes", 2, viajes_l2_es[i], viajes_l2_en[i])

# Nivel 3
viajes_l3_es = ["Un turista perdido en la selva", "Corriendo con las maletas por el aeropuerto", "Intentando hablar otro idioma con señas", "Un mosquito molestando en la carpa", "La maleta que no cierra", "Dormir en el aeropuerto incómodo", "Un guía turístico aburrido", "Tomarse una selfie con un animal peligroso", "Perder el grupo de excursión", "El auto se descompone en la ruta"]
viajes_l3_en = ["A tourist lost in the jungle", "Running with suitcases through the airport", "Trying to speak another language with signs", "A mosquito annoying in the tent", "The suitcase that won't close", "Sleeping uncomfortably at the airport", "A boring tour guide", "Taking a selfie with a dangerous animal", "Losing the tour group", "Car breaking down on the road"]
for i in range(len(viajes_l3_es)): add_row("Viajes", 3, viajes_l3_es[i], viajes_l3_en[i])


# --- SORPRESA ---
# Nivel 1
sorpresa_l1_es = ["Regalo", "Grito", "Susto", "Mago", "Conejo", "Carta", "Anillo", "Lotería", "Truco", "Escondite", "Fantasma", "Monstruo", "Sombra", "Disparo", "Explosión", "Noticia", "Broma", "Caja", "Misterio", "Secreto", "Espía", "Lupa", "Huella", "Pista", "Llave", "Candado", "Cofre", "Tesoro", "Mapa", "X", "Pirata", "Loro", "Parche", "Pata", "Garfio", "Barco", "Bandera", "Calavera", "Espada", "Cañón", "Bomba", "Mecha", "Fuego", "Humo", "Ceniza", "Volcán", "Lava", "Terremoto", "Rayo", "Trueno"]
sorpresa_l1_en = ["Gift", "Scream", "Scare", "Magician", "Rabbit", "Letter", "Ring", "Lottery", "Trick", "Hideout", "Ghost", "Monster", "Shadow", "Shot", "Explosion", "News", "Prank", "Box", "Mystery", "Secret", "Spy", "Magnifying glass", "Footprint", "Clue", "Key", "Padlock", "Chest", "Treasure", "Map", "X", "Pirate", "Parrot", "Patch", "Leg", "Hook", "Boat", "Flag", "Skull", "Sword", "Cannon", "Bomb", "Fuse", "Fire", "Smoke", "Ash", "Volcano", "Lava", "Earthquake", "Lightning", "Thunder"]
for i in range(len(sorpresa_l1_es)): add_row("Sorpresa", 1, sorpresa_l1_es[i], sorpresa_l1_en[i])

# Nivel 2
sorpresa_l2_es = ["Salir de la torta", "Encontrar un tesoro", "Ganar la lotería", "Recibir una carta", "Abrir una caja sorpresa", "Asustar a alguien", "Esconderse en el armario", "Hacer un truco de magia", "Descubrir un secreto", "Recibir una mala noticia", "Ganar un premio", "Perder la billetera", "Ver un fantasma", "Escuchar un ruido extraño", "Apagar la luz", "Romper un espejo", "Gritar de miedo", "Llorar de alegría", "Saltar de susto", "Desmayarse de impresión"]
sorpresa_l2_en = ["Coming out of the cake", "Finding a treasure", "Winning the lottery", "Receiving a letter", "Opening a surprise box", "Scaring someone", "Hiding in the closet", "Doing a magic trick", "Discovering a secret", "Receiving bad news", "Winning a prize", "Losing the wallet", "Seeing a ghost", "Hearing a strange noise", "Turning off the light", "Breaking a mirror", "Screaming in fear", "Crying with joy", "Jumping from scare", "Fainting from shock"]
for i in range(len(sorpresa_l2_es)): add_row("Sorpresa", 2, sorpresa_l2_es[i], sorpresa_l2_en[i])

# Nivel 3
sorpresa_l3_es = ["Un mago que falla el truco", "Descubrir que eres millonario", "Una propuesta de matrimonio en público", "Encontrar un animal en la cama", "Caminar con los ojos vendados", "Un regalo que explota (broma)", "Confundir a una persona con otra", "Olvidar el cumpleaños de alguien", "Encontrar dinero en un pantalón viejo", "Ver un ovni en el cielo"]
sorpresa_l3_en = ["A magician failing the trick", "Discovering you are a millionaire", "A public marriage proposal", "Finding an animal in the bed", "Walking blindfolded", "A gift that explodes (prank)", "Mistaking a person for another", "Forgetting someone's birthday", "Finding money in old pants", "Seeing a UFO in the sky"]
for i in range(len(sorpresa_l3_es)): add_row("Sorpresa", 3, sorpresa_l3_es[i], sorpresa_l3_en[i])


# --- VERANO ---
# Nivel 1
verano_l1_es = ["Sol", "Playa", "Arena", "Mar", "Helado", "Sombrilla", "Ventilador", "Mosquito", "Calor", "Piscina", "Gafas", "Bikini", "Toalla", "Coco", "Surf", "Ola", "Pez", "Barco", "Vela", "Ancla", "Red", "Pesca", "Caña", "Carnada", "Balde", "Pala", "Castillo", "Cangrejo", "Caracol", "Estrella", "Medusa", "Alga", "Coral", "Tiburón", "Delfín", "Ballena", "Pulpo", "Calamar", "Langosta", "Camarón", "Ostra", "Perla", "Buzo", "Tanque", "Aletas", "Visor", "Snorkel", "Salvavidas", "Flotador", "Trampolín"]
verano_l1_en = ["Sun", "Beach", "Sand", "Sea", "Ice Cream", "Umbrella", "Fan", "Mosquito", "Heat", "Pool", "Glasses", "Bikini", "Towel", "Coconut", "Surf", "Wave", "Fish", "Boat", "Sail", "Anchor", "Net", "Fishing", "Rod", "Bait", "Bucket", "Shovel", "Castle", "Crab", "Snail", "Starfish", "Jellyfish", "Algae", "Coral", "Shark", "Dolphin", "Whale", "Octopus", "Squid", "Lobster", "Shrimp", "Oyster", "Pearl", "Diver", "Tank", "Fins", "Mask", "Snorkel", "Lifebuoy", "Float", "Diving board"]
for i in range(len(verano_l1_es)): add_row("Verano", 1, verano_l1_es[i], verano_l1_en[i])

# Nivel 2
verano_l2_es = ["Tomar sol", "Comer helado", "Quemarse con arena", "Nadar en la piscina", "Echarse bronceador", "Espantar mosquitos", "Construir castillo de arena", "Tirarse de bomba", "Surfear una ola", "Pescar un pez", "Remar en bote", "Bucear en el mar", "Jugar al voley playa", "Enterrarse en la arena", "Buscar caracoles", "Comer sandía", "Beber agua de coco", "Usar gafas de sol", "Sacudir la toalla", "Inflar el flotador"]
verano_l2_en = ["Sunbathing", "Eating ice cream", "Burning with sand", "Swimming in the pool", "Putting on sunscreen", "Shooing mosquitoes", "Building a sandcastle", "Doing a cannonball", "Surfing a wave", "Catching a fish", "Rowing a boat", "Diving in the sea", "Playing beach volleyball", "Burying in the sand", "Looking for seashells", "Eating watermelon", "Drinking coconut water", "Wearing sunglasses", "Shaking the towel", "Inflating the float"]
for i in range(len(verano_l2_es)): add_row("Verano", 2, verano_l2_es[i], verano_l2_en[i])

# Nivel 3
verano_l3_es = ["Caminando descalzo por arena caliente", "Un mosquito que no te deja dormir", "Tratando de abrir una sombrilla con viento", "Comiendo sandía y escupiendo las semillas", "Un cangrejo pellizcándote el pie", "Ponerse protector solar en la espalda solo", "Sacarse agua del oído saltando", "Tratar de subir al inflable y caerse", "Perder las gafas en el mar", "Correr hacia el mar quemándose los pies"]
verano_l3_en = ["Walking barefoot on hot sand", "A mosquito not letting you sleep", "Trying to open an umbrella in the wind", "Eating watermelon and spitting seeds", "A crab pinching your foot", "Putting sunscreen on your back alone", "Getting water out of ear jumping", "Trying to get on the inflatable and falling", "Losing glasses in the sea", "Running to the sea burning feet"]
for i in range(len(verano_l3_es)): add_row("Verano", 3, verano_l3_es[i], verano_l3_en[i])


# --- JUEGOS ---
# Nivel 1
juegos_l1_es = ["Dado", "Carta", "Ajedrez", "Dominó", "Ficha", "Tablero", "Videojuego", "Control", "Rompecabezas", "Canicas", "Rayuela", "Escondite", "Mancha", "Soga", "Ula-ula", "Trompo", "Yo-yo", "Barrilete", "Muñeca", "Oso", "Pelota", "Arco", "Flecha", "Espada", "Escudo", "Casco", "Poción", "Vida", "Puntos", "Nivel", "Misión", "Mapa", "Tesoro", "Moneda", "Gema", "Copa", "Medalla", "Trofeo", "Podio", "Ganador", "Perdedor", "Árbitro", "Silbato", "Tarjeta", "Gol", "Falta", "Penal", "Tiempo", "Pausa", "Fin"]
juegos_l1_en = ["Dice", "Card", "Chess", "Dominoes", "Chip", "Board", "Video game", "Controller", "Puzzle", "Marbles", "Hopscotch", "Hide and seek", "Tag", "Rope", "Hula hoop", "Spinning top", "Yo-yo", "Kite", "Doll", "Bear", "Ball", "Bow", "Arrow", "Sword", "Shield", "Helmet", "Potion", "Life", "Points", "Level", "Mission", "Map", "Treasure", "Coin", "Gem", "Cup", "Medal", "Trophy", "Podium", "Winner", "Loser", "Referee", "Whistle", "Card", "Goal", "Foul", "Penalty", "Time", "Pause", "End"]
for i in range(len(juegos_l1_es)): add_row("Juegos", 1, juegos_l1_es[i], juegos_l1_en[i])

# Nivel 2
juegos_l2_es = ["Tirar los dados", "Mezclar las cartas", "Mover el peón", "Saltar la soga", "Jugar a las escondidas", "Armar un rompecabezas", "Jugar videojuegos", "Ganar la partida", "Perder el turno", "Hacer trampa", "Apostar dinero", "Contar hasta diez", "Correr la base", "Meter un gol", "Atajar el penal", "Sacar tarjeta roja", "Pedir tiempo", "Celebrar la victoria", "Llorar la derrota", "Cambiar de jugador"]
juegos_l2_en = ["Rolling the dice", "Shuffling cards", "Moving the pawn", "Jumping rope", "Playing hide and seek", "Assembling a puzzle", "Playing video games", "Winning the match", "Losing the turn", "Cheating", "Betting money", "Counting to ten", "Running the base", "Scoring a goal", "Saving the penalty", "Showing red card", "Calling timeout", "Celebrating victory", "Crying defeat", "Changing player"]
for i in range(len(juegos_l2_es)): add_row("Juegos", 2, juegos_l2_es[i], juegos_l2_en[i])

# Nivel 3
juegos_l3_es = ["Un personaje de videojuego trabado", "Haciendo trampa en las cartas disimuladamente", "La torre de Jenga cayéndose", "Perdiendo en el Monopoly y enojándose", "Jugando realidad virtual y chocando", "Soplanso el cartucho del juego", "Festejando un gol antes de tiempo", "Tratando de entender las reglas del juego", "Escondiéndose en un lugar muy pequeño", "Saltando la soga y tropezando"]
juegos_l3_en = ["A video game character stuck", "Cheating at cards sneakily", "The Jenga tower falling", "Losing at Monopoly and getting angry", "Playing VR and crashing", "Blowing the game cartridge", "Celebrating a goal too early", "Trying to understand game rules", "Hiding in a very small place", "Jumping rope and tripping"]
for i in range(len(juegos_l3_es)): add_row("Juegos", 3, juegos_l3_es[i], juegos_l3_en[i])


# === EXISTING CATEGORIES (Sample Additions) ===
# Animales
add_row("Animales", 1, "Hámster", "Hamster")
add_row("Animales", 1, "Loro", "Parrot")
add_row("Animales", 2, "Ordeñar una vaca", "Milking a cow")
add_row("Animales", 3, "Un pingüino resbalando en hielo", "A penguin slipping on ice")

# Películas
add_row("Películas", 1, "Shrek", "Shrek")
add_row("Películas", 1, "Minions", "Minions")
add_row("Películas", 2, "Huir de un dinosaurio", "Running from a dinosaur")
add_row("Películas", 3, "James Bond pidiendo un martini", "James Bond ordering a martini")

# Profesiones
add_row("Profesiones", 1, "Astronauta", "Astronaut")
add_row("Profesiones", 2, "Arreglar el auto", "Fixing the car")
add_row("Profesiones", 3, "Un cirujano operando con temblor", "A surgeon operating with shaking hands")


csv_path = 'charadas_latam_database.csv'
header = ['Categoría', 'Nivel', 'Español (Latino)', 'Inglés']

# Append to file
file_exists = os.path.isfile(csv_path)

with open(csv_path, 'a', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=header)
    if not file_exists:
        writer.writeheader()
    for row in new_rows:
        writer.writerow(row)

print(f"Appended {len(new_rows)} new entries to {csv_path}")
