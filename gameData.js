// ===== GAME DATA - MÍMICA PRO =====

const CATEGORIES = [
  {
    id: 'animales', icon: 'animales_leon.png',
    words_es: ['León', 'Elefante', 'Jirafa', 'Serpiente', 'Águila', 'Delfín', 'Gorila', 'Canguro', 'Pingüino', 'Mariposa', 'Tiburón', 'Tortuga', 'Caballo', 'Gato', 'Perro', 'Oso', 'Conejo', 'Lobo', 'Zorro', 'Búho', 'Mono', 'Tigre', 'Cocodrilo', 'Ratón', 'Vaca', 'Cerdo', 'Gallina', 'Araña', 'Abeja', 'Pulpo', 'Loro', 'Foca', 'Camaleón', 'Rinoceronte', 'Hipopótamo'],
    words_en: ['Lion', 'Elephant', 'Giraffe', 'Snake', 'Eagle', 'Dolphin', 'Gorilla', 'Kangaroo', 'Penguin', 'Butterfly', 'Shark', 'Turtle', 'Horse', 'Cat', 'Dog', 'Bear', 'Rabbit', 'Wolf', 'Fox', 'Owl', 'Monkey', 'Tiger', 'Crocodile', 'Mouse', 'Cow', 'Pig', 'Chicken', 'Spider', 'Bee', 'Octopus', 'Parrot', 'Seal', 'Chameleon', 'Rhino', 'Hippo']
  },

  {
    id: 'peliculas', icon: 'peliculas_popcorn.png',
    words_es: ['Titanic', 'Batman', 'Spider-Man', 'Frozen', 'Shrek', 'Matrix', 'Avatar', 'Rocky', 'Pinocho', 'Aladdin', 'Cenicienta', 'Toy Story', 'Jurassic Park', 'Indiana Jones', 'Star Wars', 'Harry Potter', 'El Rey León', 'Nemo', 'Coco', 'Encanto', 'Ratatouille', 'Moana', 'Up', 'Cars', 'Rapunzel', 'Mulan', 'Terminator', 'Gladiador', 'Tarzan', 'Peter Pan', 'Dumbo', 'Bambi', 'Luca', 'Soul'],
    words_en: ['Titanic', 'Batman', 'Spider-Man', 'Frozen', 'Shrek', 'Matrix', 'Avatar', 'Rocky', 'Pinocchio', 'Aladdin', 'Cinderella', 'Toy Story', 'Jurassic Park', 'Indiana Jones', 'Star Wars', 'Harry Potter', 'The Lion King', 'Nemo', 'Coco', 'Encanto', 'Ratatouille', 'Moana', 'Up', 'Cars', 'Rapunzel', 'Mulan', 'Terminator', 'Gladiator', 'Tarzan', 'Peter Pan', 'Dumbo', 'Bambi', 'Luca', 'Soul']
  },

  {
    id: 'heroes', icon: 'heroes_escudo.png',
    words_es: ['Superman', 'Batman', 'Spider-Man', 'Iron Man', 'Thor', 'Hulk', 'Flash', 'Aquaman', 'Wonder Woman', 'Capitán América', 'Wolverine', 'Deadpool', 'Doctor Strange', 'Black Panther', 'Robin', 'Linterna Verde', 'Ant-Man', 'Hawkeye', 'Venom', 'Thanos', 'Scarlet Witch', 'Joker', 'Catwoman', 'Loki', 'Groot', 'Gamora', 'Shazam', 'Cyborg', 'Storm', 'Magneto', 'Professor X', 'Daredevil', 'Luke Cage', 'Nightwing'],
    words_en: ['Superman', 'Batman', 'Spider-Man', 'Iron Man', 'Thor', 'Hulk', 'Flash', 'Aquaman', 'Wonder Woman', 'Captain America', 'Wolverine', 'Deadpool', 'Doctor Strange', 'Black Panther', 'Robin', 'Green Lantern', 'Ant-Man', 'Hawkeye', 'Venom', 'Thanos', 'Scarlet Witch', 'Joker', 'Catwoman', 'Loki', 'Groot', 'Gamora', 'Shazam', 'Cyborg', 'Storm', 'Magneto', 'Professor X', 'Daredevil', 'Luke Cage', 'Nightwing']
  },

  {
    id: 'accion', icon: 'accion_rayo.png',
    words_es: ['Correr', 'Saltar', 'Nadar', 'Bailar', 'Cocinar', 'Dormir', 'Volar', 'Conducir', 'Escalar', 'Boxear', 'Surfear', 'Patinar', 'Cantar', 'Llorar', 'Reír', 'Estornudar', 'Aplaudir', 'Silbar', 'Bostezar', 'Pintar', 'Pescar', 'Bucear', 'Disparar', 'Lanzar', 'Atrapar', 'Empujar', 'Jalar', 'Gritar', 'Rezar', 'Meditar', 'Barrer', 'Planchar', 'Coser', 'Tejer', 'Esquiar'],
    words_en: ['Run', 'Jump', 'Swim', 'Dance', 'Cook', 'Sleep', 'Fly', 'Drive', 'Climb', 'Box', 'Surf', 'Skate', 'Sing', 'Cry', 'Laugh', 'Sneeze', 'Clap', 'Whistle', 'Yawn', 'Paint', 'Fish', 'Dive', 'Shoot', 'Throw', 'Catch', 'Push', 'Pull', 'Scream', 'Pray', 'Meditate', 'Sweep', 'Iron', 'Sew', 'Knit', 'Ski']
  },

  {
    id: 'deportes', icon: 'deportes_basket.png',
    words_es: ['Fútbol', 'Basketball', 'Tenis', 'Natación', 'Boxeo', 'Surf', 'Karate', 'Voleibol', 'Golf', 'Béisbol', 'Hockey', 'Rugby', 'Ciclismo', 'Esquí', 'Skateboard', 'Ping Pong', 'Bádminton', 'Lucha', 'Judo', 'Esgrima', 'Polo', 'Escalada', 'Remo', 'Arquería', 'Gimnasia', 'Atletismo', 'Snowboard', 'Patinaje', 'Triatlón', 'Waterpolo', 'Handball', 'Cricket', 'Salto Alto', 'Lanzamiento de Disco'],
    words_en: ['Soccer', 'Basketball', 'Tennis', 'Swimming', 'Boxing', 'Surfing', 'Karate', 'Volleyball', 'Golf', 'Baseball', 'Hockey', 'Rugby', 'Cycling', 'Skiing', 'Skateboarding', 'Ping Pong', 'Badminton', 'Wrestling', 'Judo', 'Fencing', 'Polo', 'Climbing', 'Rowing', 'Archery', 'Gymnastics', 'Athletics', 'Snowboarding', 'Skating', 'Triathlon', 'Water Polo', 'Handball', 'Cricket', 'High Jump', 'Discus Throw']
  },

  {
    id: 'musica', icon: 'musica_headphones.png',
    words_es: ['Guitarra', 'Piano', 'Batería', 'Trompeta', 'Violín', 'Flauta', 'Saxofón', 'DJ', 'Cantante', 'Director', 'Arpa', 'Bajo', 'Maracas', 'Tambor', 'Acordeón', 'Banjo', 'Xilófono', 'Micrófono', 'Rock', 'Ópera', 'Ballet', 'Tango', 'Reggaetón', 'Salsa', 'Hip Hop', 'Rap', 'Jazz', 'Blues', 'Cello', 'Órgano', 'Ukelele', 'Armónica', 'Pandereta', 'Mariachi'],
    words_en: ['Guitar', 'Piano', 'Drums', 'Trumpet', 'Violin', 'Flute', 'Saxophone', 'DJ', 'Singer', 'Conductor', 'Harp', 'Bass', 'Maracas', 'Drum', 'Accordion', 'Banjo', 'Xylophone', 'Microphone', 'Rock', 'Opera', 'Ballet', 'Tango', 'Reggaeton', 'Salsa', 'Hip Hop', 'Rap', 'Jazz', 'Blues', 'Cello', 'Organ', 'Ukulele', 'Harmonica', 'Tambourine', 'Mariachi']
  },

  {
    id: 'profesiones', icon: 'profesiones_steth.png',
    words_es: ['Doctor', 'Bombero', 'Policía', 'Chef', 'Astronauta', 'Piloto', 'Maestro', 'Dentista', 'Veterinario', 'Mago', 'Payaso', 'Pirata', 'Ninja', 'Mecánico', 'Pintor', 'Fotógrafo', 'Jardinero', 'Cartero', 'Albañil', 'Peluquero', 'Electricista', 'Carpintero', 'Plomero', 'Abogado', 'Arqueólogo', 'Panadero', 'Carnicero', 'Sastre', 'Soldado', 'Espía', 'Minero', 'Granjero', 'Enfermera', 'Detective'],
    words_en: ['Doctor', 'Firefighter', 'Police', 'Chef', 'Astronaut', 'Pilot', 'Teacher', 'Dentist', 'Veterinarian', 'Magician', 'Clown', 'Pirate', 'Ninja', 'Mechanic', 'Painter', 'Photographer', 'Gardener', 'Mailman', 'Builder', 'Barber', 'Electrician', 'Carpenter', 'Plumber', 'Lawyer', 'Archaeologist', 'Baker', 'Butcher', 'Tailor', 'Soldier', 'Spy', 'Miner', 'Farmer', 'Nurse', 'Detective']
  },

  {
    id: 'objetos', icon: 'objetos_lampara.png',
    words_es: ['Teléfono', 'Silla', 'Paraguas', 'Espejo', 'Reloj', 'Escalera', 'Martillo', 'Tijeras', 'Cámara', 'Bicicleta', 'Computadora', 'Guitarra', 'Balón', 'Mochila', 'Sombrero', 'Lentes', 'Zapatos', 'Libro', 'Lámpara', 'Llave', 'Candado', 'Linterna', 'Maleta', 'Almohada', 'Televisor', 'Control Remoto', 'Cepillo', 'Tenedor', 'Cuchillo', 'Botella', 'Globo', 'Corona', 'Espada', 'Escudo'],
    words_en: ['Phone', 'Chair', 'Umbrella', 'Mirror', 'Clock', 'Ladder', 'Hammer', 'Scissors', 'Camera', 'Bicycle', 'Computer', 'Guitar', 'Ball', 'Backpack', 'Hat', 'Glasses', 'Shoes', 'Book', 'Lamp', 'Key', 'Padlock', 'Flashlight', 'Suitcase', 'Pillow', 'TV', 'Remote Control', 'Brush', 'Fork', 'Knife', 'Bottle', 'Balloon', 'Crown', 'Sword', 'Shield']
  },

  {
    id: 'comida', icon: 'comida_pizza.png',
    words_es: ['Pizza', 'Hamburguesa', 'Hot Dog', 'Sushi', 'Taco', 'Helado', 'Pastel', 'Chocolate', 'Palomitas', 'Banana', 'Manzana', 'Sandía', 'Huevo Frito', 'Espagueti', 'Ensalada', 'Sopa', 'Asado', 'Empanada', 'Panqueque', 'Donut', 'Galleta', 'Queso', 'Pan', 'Torta', 'Café', 'Jugo', 'Batido', 'Papas Fritas', 'Pollo Frito', 'Arroz', 'Churrasco', 'Flan', 'Waffle', 'Croissant'],
    words_en: ['Pizza', 'Hamburger', 'Hot Dog', 'Sushi', 'Taco', 'Ice Cream', 'Cake', 'Chocolate', 'Popcorn', 'Banana', 'Apple', 'Watermelon', 'Fried Egg', 'Spaghetti', 'Salad', 'Soup', 'BBQ', 'Empanada', 'Pancake', 'Donut', 'Cookie', 'Cheese', 'Bread', 'Pie', 'Coffee', 'Juice', 'Smoothie', 'French Fries', 'Fried Chicken', 'Rice', 'Steak', 'Flan', 'Waffle', 'Croissant']
  },

  {
    id: 'fiesta', icon: 'fiesta_confetti.png',
    words_es: ['Cumpleaños', 'Navidad', 'Halloween', 'Carnaval', 'Boda', 'Año Nuevo', 'Piñata', 'Globos', 'Confeti', 'Pastel', 'Velas', 'Regalos', 'Música', 'Baile', 'Disfraz', 'Máscara', 'Fuegos Artificiales', 'Brindis', 'Karaoke', 'Limbo', 'Serpentinas', 'Guirnaldas', 'Sorpresa', 'Cotillón', 'DJ', 'Pista de Baile', 'Invitaciones', 'Decoración', 'Fotomatón', 'Juegos', 'Conga', 'Macarena', 'San Valentín', 'Fiesta de Pijamas'],
    words_en: ['Birthday', 'Christmas', 'Halloween', 'Carnival', 'Wedding', 'New Year', 'Piñata', 'Balloons', 'Confetti', 'Cake', 'Candles', 'Gifts', 'Music', 'Dance', 'Costume', 'Mask', 'Fireworks', 'Toast', 'Karaoke', 'Limbo', 'Streamers', 'Garlands', 'Surprise', 'Party Favors', 'DJ', 'Dance Floor', 'Invitations', 'Decoration', 'Photo Booth', 'Games', 'Conga', 'Macarena', 'Valentine\'s Day', 'Sleepover']
  },

  {
    id: 'viajes', icon: 'viajes_maleta.png',
    words_es: ['Avión', 'Tren', 'Barco', 'Playa', 'Montaña', 'Camping', 'Maleta', 'Pasaporte', 'Mapa', 'Brújula', 'Hotel', 'Tienda de Campaña', 'Fotografía', 'Recuerdo', 'Aeropuerto', 'Taxi', 'Autobús', 'Metro', 'Crucero', 'Safari', 'Volcán', 'Cascada', 'Desierto', 'Selva', 'Isla', 'Faro', 'Museo', 'Castillo', 'Pirámide', 'Torre Eiffel', 'Globo Aerostático', 'Mochilero', 'Brújula', 'GPS'],
    words_en: ['Airplane', 'Train', 'Ship', 'Beach', 'Mountain', 'Camping', 'Suitcase', 'Passport', 'Map', 'Compass', 'Hotel', 'Tent', 'Photography', 'Souvenir', 'Airport', 'Taxi', 'Bus', 'Subway', 'Cruise', 'Safari', 'Volcano', 'Waterfall', 'Desert', 'Jungle', 'Island', 'Lighthouse', 'Museum', 'Castle', 'Pyramid', 'Eiffel Tower', 'Hot Air Balloon', 'Backpacker', 'Compass', 'GPS']
  },

  {
    id: 'sorpresa', icon: 'sorpresa_regalo.png',
    words_es: ['Regalo', 'Caja Sorpresa', 'Mago', 'Truco', 'Escondite', 'Cumpleaños Sorpresa', 'Lotería', 'Premio', 'Tesoro', 'Cofre', 'Secreto', 'Misterio', 'Revelación', 'Adivinanza', 'Acertijo', 'Escapismo', 'Laberinto', 'Pista', 'Enigma', 'Detective', 'Lupa', 'Huella', 'Dado', 'Ruleta', 'Carta Misteriosa', 'Mensaje Secreto', 'Código', 'Candado', 'Llave Maestra', 'Habitación Secreta', 'Puerta Oculta', 'Pasadizo', 'Trampa', 'Ilusión'],
    words_en: ['Gift', 'Surprise Box', 'Magician', 'Trick', 'Hide and Seek', 'Surprise Birthday', 'Lottery', 'Prize', 'Treasure', 'Chest', 'Secret', 'Mystery', 'Reveal', 'Riddle', 'Puzzle', 'Escape Room', 'Labyrinth', 'Clue', 'Enigma', 'Detective', 'Magnifying Glass', 'Fingerprint', 'Dice', 'Roulette', 'Mystery Letter', 'Secret Message', 'Code', 'Padlock', 'Master Key', 'Secret Room', 'Hidden Door', 'Passage', 'Trap', 'Illusion']
  },

  {
    id: 'verano', icon: 'verano_sol.png',
    words_es: ['Playa', 'Sol', 'Piscina', 'Helado', 'Sandía', 'Protector Solar', 'Gafas de Sol', 'Surfear', 'Castillo de Arena', 'Flotador', 'Bikini', 'Palmera', 'Hamaca', 'Limonada', 'Abanico', 'Ventilador', 'Barbacoa', 'Sombrilla', 'Toalla', 'Olas', 'Concha Marina', 'Estrella de Mar', 'Cangrejo', 'Medusa', 'Snorkel', 'Kayak', 'Jet Ski', 'Pelota de Playa', 'Bronceado', 'Chiringuito', 'Atardecer', 'Fogata', 'Verano', 'Chapuzón'],
    words_en: ['Beach', 'Sun', 'Pool', 'Ice Cream', 'Watermelon', 'Sunscreen', 'Sunglasses', 'Surfing', 'Sand Castle', 'Floatie', 'Bikini', 'Palm Tree', 'Hammock', 'Lemonade', 'Fan', 'Electric Fan', 'BBQ', 'Umbrella', 'Towel', 'Waves', 'Seashell', 'Starfish', 'Crab', 'Jellyfish', 'Snorkel', 'Kayak', 'Jet Ski', 'Beach Ball', 'Suntan', 'Beach Bar', 'Sunset', 'Bonfire', 'Summer', 'Splash']
  },

  {
    id: 'juegos', icon: 'juegos_controller.png',
    words_es: ['Mario', 'Pac-Man', 'Tetris', 'Minecraft', 'Fortnite', 'Ajedrez', 'Damas', 'Monopoly', 'Jenga', 'Uno', 'Dado', 'Rompecabezas', 'Cartas', 'Dominó', 'Ludo', 'Twister', 'Bingo', 'Pinball', 'Futbolín', 'Pool', 'Dardos', 'Boliche', 'Videojuego', 'Consola', 'Joystick', 'Realidad Virtual', 'Arcade', 'Game Over', 'Power Up', 'Nivel', 'Boss Final', 'Laberinto', 'Trivia', 'Charadas'],
    words_en: ['Mario', 'Pac-Man', 'Tetris', 'Minecraft', 'Fortnite', 'Chess', 'Checkers', 'Monopoly', 'Jenga', 'Uno', 'Dice', 'Puzzle', 'Cards', 'Dominoes', 'Ludo', 'Twister', 'Bingo', 'Pinball', 'Foosball', 'Pool', 'Darts', 'Bowling', 'Video Game', 'Console', 'Joystick', 'Virtual Reality', 'Arcade', 'Game Over', 'Power Up', 'Level', 'Final Boss', 'Maze', 'Trivia', 'Charades']
  }
];

// ===== i18n TRANSLATIONS =====
const i18n = {
  es: {
    appTitle: 'Mímica Pro',
    categories: { animales: 'Animales', peliculas: 'Películas', heroes: 'Héroes', accion: 'Acción', deportes: 'Deportes', musica: 'Música', profesiones: 'Profesiones', objetos: 'Objetos', comida: 'Comida', fiesta: 'Fiesta', viajes: 'Viajes', sorpresa: 'Sorpresa', verano: 'Verano', juegos: 'Juegos' },
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
    resultados: 'MÍMICA PRO<br>RESULTADOS',
    puntuacion: 'PUNTUACIÓN<br>TOTAL:',
    volverJugar: 'VOLVER A JUGAR',
    menu: 'MENÚ',
    configTitle: 'Mímica Pro -<br>Configuración',
    idioma: 'Idioma / Language',
    musicaLabel: 'Música',
    vibracion: 'Vibración',
    tiempoJuego: 'Tiempo de Juego',
    segundos: 'segundos',
    guardar: 'GUARDAR',
    salirTitulo: '¿QUIERES SALIR?',
    salirDesc: '¡Oh no! Se perderá el progreso actual.',
    noSeguir: '▶ NO, SEGUIR',
    siSalir: '✕ SÍ, SALIR',
    seleccionaCat: '¡Selecciona al menos una categoría!',
    loading: 'Cargando Assets...',
  },
  en: {
    appTitle: 'Mimica Pro',
    categories: { animales: 'Animals', peliculas: 'Movies', heroes: 'Heroes', accion: 'Action', deportes: 'Sports', musica: 'Music', profesiones: 'Professions', objetos: 'Objects', comida: 'Food', fiesta: 'Party', viajes: 'Travel', sorpresa: 'Surprise', verano: 'Summer', juegos: 'Games' },
    empezar: 'START',
    config: 'Settings',
    ayuda: 'Help',
    comoJugar: 'How to Play',
    howto1Title: 'Choose a category',
    howto1Desc: 'Explore the fun themes and pick one to start playing.',
    howto2Title: 'Act it out',
    howto2Desc: "Describe the word without talking! Your team must guess in time.",
    howto3Title: 'Score points',
    howto3Desc: 'Earn points with every correct guess and celebrate victory.',
    entendido: 'GOT IT',
    pasar: 'SKIP',
    correcto: 'CORRECT',
    resultados: 'MIMICA PRO<br>RESULTS',
    puntuacion: 'TOTAL<br>SCORE:',
    volverJugar: 'PLAY AGAIN',
    menu: 'MENU',
    configTitle: 'Mimica Pro -<br>Settings',
    idioma: 'Language / Idioma',
    musicaLabel: 'Music',
    vibracion: 'Vibration',
    tiempoJuego: 'Game Time',
    segundos: 'seconds',
    guardar: 'SAVE',
    salirTitulo: 'QUIT GAME?',
    salirDesc: "Oh no! You'll lose current progress.",
    noSeguir: '▶ NO, CONTINUE',
    siSalir: '✕ YES, QUIT',
    seleccionaCat: 'Select at least one category!',
    loading: 'Loading Assets...',
  }
};
