// ===== GAME DATA - MÍMICA PRO =====
// Categorias con sub-niveles de dificultad: 1 (Fácil), 2 (Medio), 3 (Difícil)

const CATEGORIES = [
  {
    id: 'animales', icon: 'animales_leon.png',
    words_es: {
      1: ['León', 'Elefante', 'Jirafa', 'Gato', 'Perro', 'Vaca', 'Pato', 'Mono', 'Serpiente', 'Tiburón', 'Conejo', 'Oso', 'Cerdo', 'Pez', 'Araña', 'Lobo', 'Rana', 'Búho', 'Cebra', 'Ratón', 'Gallina', 'Pollo', 'Mariposa', 'Abeja', 'Oveja', 'Caballo', 'Gorila', 'Tigre', 'Tortuga', 'Caracol'],
      2: ['Mono comiendo banana', 'Perro persiguiendo su cola', 'Gato maullando', 'Pez fuera del agua', 'Pájaro volando', 'Delfín saltando', 'Canguro boxeando', 'Serpiente enroscándose', 'Elefante usando la trompa', 'Gallina poniendo un huevo', 'Tiburón atacando', 'Oso invernando', 'Gorila golpeándose el pecho', 'Cangrejo caminando de lado', 'Pájaro carpintero picoteando', 'Camaleón cambiando de color', 'Hipopótamo abriendo la boca', 'Araña tejiendo tela', 'Cerdo revolcándose en lodo', 'Vaca siendo ordeñada'],
      3: ['Un pingüino bailando claqué en el hielo', 'Una mariposa saliendo de su capullo', 'Un pulpo tratando de abrir un frasco', 'Un murciélago durmiendo de cabeza', 'Un pavo real abriendo sus plumas', 'Un camello cruzando el desierto con sed', 'Una ardilla escondiendo una nuez', 'Un rinoceronte embistiendo un árbol', 'Una foca aplaudiendo por pescado', 'Un oso hormiguero usando su lengua larga', 'Una luciérnaga brillando en la noche', 'Un perezoso bajando un árbol muy lento', 'Un avestruz escondiendo la cabeza', 'Un koala abrazado a un eucalipto', 'Un ornitorrinco nadando en un río']
    },
    words_en: {
      1: ['Lion', 'Elephant', 'Giraffe', 'Cat', 'Dog', 'Cow', 'Duck', 'Monkey', 'Snake', 'Shark', 'Rabbit', 'Bear', 'Pig', 'Fish', 'Spider', 'Wolf', 'Frog', 'Owl', 'Zebra', 'Mouse', 'Hen', 'Chicken', 'Butterfly', 'Bee', 'Sheep', 'Horse', 'Gorilla', 'Tiger', 'Turtle', 'Snail'],
      2: ['Monkey eating banana', 'Dog chasing its tail', 'Cat meowing', 'Fish out of water', 'Bird flying', 'Dolphin jumping', 'Kangaroo boxing', 'Snake coiling up', 'Elephant using its trunk', 'Chicken laying an egg', 'Shark attacking', 'Bear hibernating', 'Gorilla thumping chest', 'Crab walking sideways', 'Woodpecker pecking', 'Chameleon changing color', 'Hippo opening its mouth', 'Spider weaving a web', 'Pig rolling in mud', 'Cow being milked'],
      3: ['A penguin tap dancing on ice', 'A butterfly emerging from a cocoon', 'An octopus trying to open a jar', 'A bat sleeping upside down', 'A peacock opening its feathers', 'A camel crossing the desert and thirsty', 'A squirrel hiding a nut', 'A rhino ramming a tree', 'A seal clapping for fish', 'An anteater using its long tongue', 'A firefly glowing in the night', 'A sloth climbing down a tree very slowly', 'An ostrich hiding its head', 'A koala hugging a eucalyptus tree', 'A platypus swimming in a river']
    }
  },

  {
    id: 'peliculas', icon: 'peliculas_popcorn.png',
    words_es: {
      1: ['Titanic', 'Batman', 'Frozen', 'Shrek', 'Harry Potter', 'Avatar', 'Rocky', 'Spider-Man', 'Pinocho', 'Aladdin', 'Cars', 'Coco', 'Nemo', 'Tarzán', 'Mulan', 'Soul', 'Cenicienta', 'Joker', 'Iron Man', 'Thor', 'Hulk', 'Dumbo', 'Bambi', 'Peter Pan', 'Superman'],
      2: ['Jurassic Park', 'Indiana Jones', 'Star Wars', 'El Rey León', 'Toy Story', 'Misión Imposible', 'Piratas del Caribe', 'La Casa de Papel', 'Stranger Things', 'Matilda', 'Home Alone', 'El Padrino', 'El Mago de Oz', 'Juego de Tronos', 'Gladiador', 'Terminator', 'Matrix', 'Mad Max', 'Jumanji', 'Ghostbusters'],
      3: ['Jack Sparrow manejando el Perla Negra', 'Harry Potter volando en su escoba', 'Simba siendo presentado en la roca', 'Spider-Man lanzando telarañas por la ciudad', 'Elsa construyendo su castillo de hielo', 'Rocky Balboa subiendo las escaleras corriendo', 'King Kong escalando un edificio gigante', 'Indiana Jones escapando de una roca gigante', 'Iron Man aterrizando de forma heroica', 'E.T. señalando hacia el cielo con el dedo', 'Katniss Everdeen lanzando una flecha', 'Forrest Gump corriendo sin parar', 'Michael Jackson bailando Thriller', 'Un Minion buscando una banana', 'Ego de Ratatouille probando la comida']
    },
    words_en: {
      1: ['Titanic', 'Batman', 'Frozen', 'Shrek', 'Harry Potter', 'Avatar', 'Rocky', 'Spider-Man', 'Pinocchio', 'Aladdin', 'Cars', 'Coco', 'Nemo', 'Tarzan', 'Mulan', 'Soul', 'Cinderella', 'Joker', 'Iron Man', 'Thor', 'Hulk', 'Dumbo', 'Bambi', 'Peter Pan', 'Superman'],
      2: ['Jurassic Park', 'Indiana Jones', 'Star Wars', 'The Lion King', 'Toy Story', 'Mission Impossible', 'Pirates of the Caribbean', 'Money Heist', 'Stranger Things', 'Matilda', 'Home Alone', 'The Godfather', 'Wizard of Oz', 'Game of Thrones', 'Gladiator', 'Terminator', 'Matrix', 'Mad Max', 'Jumanji', 'Ghostbusters'],
      3: ['Jack Sparrow steering the Black Pearl', 'Harry Potter flying on his broomstick', 'Simba being presented on the rock', 'Spider-Man swinging webs through the city', 'Elsa building her ice castle', 'Rocky Balboa running up the museum steps', 'King Kong climbing a giant skyscraper', 'Indiana Jones escaping a giant rolling boulder', 'Iron Man performing a hero landing', 'E.T. pointing to the sky with his finger', 'Katniss Everdeen shooting an arrow', 'Forrest Gump running across the country', 'Michael Jackson doing the Thriller dance', 'A Minion searching for a banana', 'Ego from Ratatouille tasting food']
    }
  },

  {
    id: 'heroes', icon: 'heroes_escudo.png',
    words_es: {
      1: ['Superman', 'Batman', 'Spider-Man', 'Iron Man', 'Thor', 'Hulk', 'Flash', 'Aquaman', 'Wolverine', 'Deadpool', 'Robin Hood', 'Joker', 'Catwoman', 'Loki', 'Groot', 'Venom', 'Thanos', 'Robin', 'Black Widow', 'Hawkeye'],
      2: ['Mujer Maravilla', 'Capitán América', 'Doctor Strange', 'Pantera Negra', 'Linterna Verde', 'Ant-Man', 'Bruja Escarlata', 'Héroe salvando un bebé', 'Superhéroe volando', 'Hulk golpeando el suelo', 'Thor llamando a su martillo', 'Spider-Man trepando una pared', 'Batman usando su bati-gancho', 'Capitán América lanzando su escudo', 'Flash corriendo a la velocidad de la luz'],
      3: ['Iron Man armando su armadura por partes', 'Thanos chasqueando los dedos con el guantelete', 'La Mujer Maravilla usando su lazo de la verdad', 'Doctor Strange haciendo círculos mágicos con las manos', 'Wolverine sacando sus garras de metal lentamente', 'El Hombre Hormiga haciéndose diminuto y gigante', 'Magneto moviendo un puente de metal con la mente', 'Groot diciendo "Yo soy Groot" con gestos', 'Spider-Man balanceándose entre dos edificios', 'Aquaman hablando con los peces bajo el mar']
    },
    words_en: {
      1: ['Superman', 'Batman', 'Spider-Man', 'Iron Man', 'Thor', 'Hulk', 'Flash', 'Aquaman', 'Wolverine', 'Deadpool', 'Robin Hood', 'Joker', 'Catwoman', 'Loki', 'Groot', 'Venom', 'Thanos', 'Robin', 'Black Widow', 'Hawkeye'],
      2: ['Wonder Woman', 'Captain America', 'Doctor Strange', 'Black Panther', 'Green Lantern', 'Ant-Man', 'Scarlet Witch', 'Hero saving a baby', 'Superhero flying', 'Hulk smashing the ground', 'Thor calling his hammer', 'Spider-Man climbing a wall', 'Batman using his bat-grapple', 'Captain America throwing his shield', 'Flash running at light speed'],
      3: ['Iron Man assembling his suit piece by piece', 'Thanos snapping his fingers with the gauntlet', 'Wonder Woman using her lasso of truth', 'Doctor Strange making magical circles with hands', 'Wolverine extending his claws slowly', 'Ant-Man becoming tiny and then giant', 'Magneto moving a metal bridge with his mind', 'Groot saying "I am Groot" with gestures', 'Spider-Man swinging between two buildings', 'Aquaman talking to fish underwater']
    }
  },

  {
    id: 'accion', icon: 'accion_rayo.png',
    words_es: {
      1: ['Correr', 'Saltar', 'Nadar', 'Bailar', 'Cocinar', 'Dormir', 'Volar', 'Conducir', 'Cantar', 'Llorar', 'Reír', 'Bostezar', 'Pintar', 'Pescar', 'Barrer', 'Coser', 'Comer', 'Beber', 'Gritar', 'Silbar'],
      2: ['Tomar sopa caliente', 'Caminata lunar', 'Matar moscas', 'Cambiar un foco', 'Inflar un globo', 'Abrir un paraguas', 'Cepillarse los dientes', 'Atarse los cordones', 'Tocar la puerta', 'Saltar la soga', 'Patinar sobre hielo', 'Subir una montaña', 'Boxear con un saco', 'Jugar al boliche', 'Montar a caballo'],
      3: ['Enhebrar una aguja muy pequeña', 'Bailar breakdance en el suelo', 'Hacer parkour sobre cajas invisibles', 'Intentar atrapar una mosca con las manos', 'Hacer un striptease cómico', 'Cruzar la calle sobre una cuerda floja', 'Luchar contra un viento muy fuerte', 'Tratar de encender una fogata con piedras', 'Hacer malabares con tres pelotas', 'Surfear una ola gigante', 'Escribir una carta de amor con pluma']
    },
    words_en: {
      1: ['Run', 'Jump', 'Swim', 'Dance', 'Cook', 'Sleep', 'Fly', 'Drive', 'Sing', 'Cry', 'Laugh', 'Yawn', 'Paint', 'Fish', 'Sweep', 'Sew', 'Eat', 'Drink', 'Scream', 'Whistle'],
      2: ['Eating hot soup', 'Moonwalk', 'Killing flies', 'Changing a lightbulb', 'Inflating a balloon', 'Opening an umbrella', 'Brushing teeth', 'Tying shoelaces', 'Knocking on the door', 'Jumping rope', 'Ice skating', 'Climbing a mountain', 'Punching a sandbag', 'Bowling', 'Riding a horse'],
      3: ['Threading a very small needle', 'Breakdancing on the floor', 'Doing parkour over invisible boxes', 'Trying to catch a fly with hands', 'Doing a funny striptease', 'Crossing the street on a tightrope', 'Fighting against very strong wind', 'Trying to start a fire with stones', 'Juggling with three balls', 'Surfing a giant wave', 'Writing a love letter with a quill']
    }
  },

  {
    id: 'deportes', icon: 'deportes_basket.png',
    words_es: {
      1: ['Fútbol', 'Basketball', 'Tenis', 'Natación', 'Boxeo', 'Golf', 'Béisbol', 'Esquí', 'Ciclismo', 'Rugby', 'Karate', 'Voleibol', 'Hockey', 'Surf', 'Lucha'],
      2: ['Meter un gol', 'Encestar una pelota', 'Nadar estilo mariposa', 'Hacer un home run', 'Levantamiento de pesas', 'Lanzamiento de jabalina', 'Jinete de caballos', 'Tiro con arco', 'Patinaje artístico', 'Salto de altura', 'Esgrima', 'Remar en canoa', 'Atajar un penal', 'Lanzar un disco', 'Hacer una plancha'],
      3: ['Un portero de fútbol haciendo una atajada heroica', 'Un gimnasta haciendo una rutina de suelo', 'Un beisbolista corriendo las bases después de un home run', 'Un surfista cayendo de una tabla en una gran ola', 'Un levantador de pesas fallando en el último segundo', 'Un boxeador siendo noqueado en cámara lenta', 'Un jugador de baloncesto fallando un mate', 'Un arquero concentrándose antes de soltar la flecha', 'Un ciclista subiendo una colina muy empinada', 'Un luchador de sumo preparándose para el combate']
    },
    words_en: {
      1: ['Soccer', 'Basketball', 'Tennis', 'Swimming', 'Boxing', 'Golf', 'Baseball', 'Skiing', 'Cycling', 'Rugby', 'Karate', 'Volleyball', 'Hockey', 'Surfing', 'Wrestling'],
      2: ['Scoring a goal', 'Dunking a ball', 'Butterfly swimming style', 'Hitting a home run', 'Weightlifting', 'Javelin throw', 'Horseback riding', 'Archery', 'Figure skating', 'High jump', 'Fencing', 'Canoe rowing', 'Saving a penalty kick', 'Throwing a discus', 'Doing a plank'],
      3: ['A soccer goalkeeper making a heroic save', 'A gymnast performing a floor routine', 'A baseball player running bases after a home run', 'A surfer falling off a board on a big wave', 'A weightlifter failing at the last second', 'A boxer being knocked out in slow motion', 'A basketball player missing a dunk', 'An archer focusing before releasing the arrow', 'A cyclist climbing a very steep hill', 'A sumo wrestler preparing for combat']
    }
  },

  {
    id: 'musica', icon: 'musica_headphones.png',
    words_es: {
      1: ['Guitarra', 'Piano', 'Batería', 'Violín', 'Cantante', 'Director', 'DJ', 'Trompeta', 'Arpa', 'Bajo', 'Flauta', 'Acordeón', 'Tambor', 'Micrófono', 'Rockstar'],
      2: ['Tocar la guitarra eléctrica', 'Cantar bajo la lluvia', 'Hacer beatbox', 'Dirigir una orquesta', 'Bailar breakdance', 'Tocar el triángulo', 'Tocar los platillos fuerte', 'Hacer un solo de piano', 'Cantar opera', 'Bailar tango', 'Bailar flamenco', 'Tocar la batería con mucha energía'],
      3: ['Un guitarrista rompiendo su guitarra en el escenario', 'Un cantante perdiendo la voz en medio de un concierto', 'Un director de orquesta que se le cae la batuta', 'Un DJ que se le raya el disco en plena fiesta', 'Un pianista que toca con los ojos vendados', 'Bailar la Macarena en grupo', 'Tocar una gaita escocesa caminando', 'Hacer una competencia de "Air Guitar"', 'Un violonchelista afinando su instrumento con dificultad', 'Un cantante de metal haciendo una voz muy grave']
    },
    words_en: {
      1: ['Guitar', 'Piano', 'Drums', 'Violin', 'Singer', 'Conductor', 'DJ', 'Trumpet', 'Harp', 'Bass', 'Flute', 'Accordion', 'Drum', 'Microphone', 'Rockstar'],
      2: ['Playing electric guitar', 'Singing in the rain', 'Doing beatbox', 'Conducting an orchestra', 'Breakdancing', 'Playing the triangle', 'Playing cymbals loudly', 'Performing a piano solo', 'Singing opera', 'Dancing tango', 'Dancing flamenco', 'Playing drums with lots of energy'],
      3: ['A guitarist smashing their guitar on stage', 'A singer losing their voice mid-concert', 'An orchestra conductor dropping their baton', 'A DJ with a scratched record during a party', 'A pianist playing blindfolded', 'Dancing the Macarena in a group', 'Playing a Scottish bagpipe while walking', 'Having an "Air Guitar" competition', 'A cellist tuning their instrument with difficulty', 'A metal singer making a very deep growl']
    }
  },

  {
    id: 'profesiones', icon: 'profesiones_steth.png',
    words_es: {
      1: ['Doctor', 'Bombero', 'Policía', 'Chef', 'Maestro', 'Pintor', 'Payaso', 'Mago', 'Jugador de basket', 'Carpintero', 'Pirata', 'Ninja', 'Soldado', 'Cartero', 'Jardinero'],
      2: ['Astronauta flotando', 'Piloto manejando avión', 'Veterinario curando perro', 'Detective privado con lupa', 'Mecánico arreglando motor', 'Fotógrafo de modelos', 'Carnicero cortando carne', 'Peluquero cortando pelo', 'Espía escondido', 'Científico loco haciendo mezclas'],
      3: ['Un domador de leones en el circo', 'Un limpiador de ventanas en un rascacielos', 'Un arqueólogo encontrando un hueso de dinosaurio', 'Un sastre tratando de enhebrar una aguja', 'Un granjero ordeñando una vaca rebelde', 'Un director de cine gritando "¡CORTE!"', 'Un mimo atrapado en una caja invisible', 'Un guardia de la reina que no se puede mover', 'Un buscador de oro encontrando una pepita', 'Un tatuador haciendo un dibujo difícil']
    },
    words_en: {
      1: ['Doctor', 'Firefighter', 'Police', 'Chef', 'Teacher', 'Painter', 'Clown', 'Magician', 'Basketball player', 'Carpenter', 'Pirate', 'Ninja', 'Soldier', 'Mailman', 'Gardener'],
      2: ['Astronaut floating', 'Pilot flying a plane', 'Veterinarian healing a dog', 'Private detective with magnifying glass', 'Mechanic fixing an engine', 'Fashion photographer', 'Butcher cutting meat', 'Barber cutting hair', 'Spy hiding', 'Mad scientist mixing chemicals'],
      3: ['A lion tamer in the circus', 'A window cleaner on a skyscraper', 'An archaeologist finding a dinosaur bone', 'A tailor trying to thread a needle', 'A farmer milking a stubborn cow', 'A movie director shouting "CUT!"', 'A mime trapped in an invisible box', 'A Queen\'s guard who cannot move', 'A gold miner finding a nugget', 'A tattoo artist making a difficult design']
    }
  },

  {
    id: 'objetos', icon: 'objetos_lampara.png',
    words_es: {
      1: ['Teléfono', 'Silla', 'Paraguas', 'Espejo', 'Reloj', 'Cuchara', 'Martillo', 'Tijeras', 'Cámara', 'Pelota', 'Libro', 'Sombrero', 'Bicicleta', 'Lámpara', 'Cama'],
      2: ['Computadora lenta', 'Mochila pesada', 'Zapatos apretados', 'Control remoto sin pilas', 'Linterna que se apaga', 'Maleta difícil de cerrar', 'Almohada muy suave', 'Tenedor doblado', 'Botella de champagne explotando', 'Globo que se vuela'],
      3: ['Una máquina de escribir antigua trabada', 'Un escudo protegiendo de flechas', 'Un hacha de leñador cortando un tronco', 'Un bastón de anciano que se rompe', 'Un lente de aumento quemando un papel', 'Un control de juegos vibrando mucho', 'Una corona que se cae de la cabeza', 'Una espada que no sale de la piedra', 'Un candado que no tiene llave', 'Un cepillo de dientes eléctrico vibrando']
    },
    words_en: {
      1: ['Phone', 'Chair', 'Umbrella', 'Mirror', 'Clock', 'Spoon', 'Hammer', 'Scissors', 'Camera', 'Ball', 'Book', 'Hat', 'Bicycle', 'Lamp', 'Bed'],
      2: ['Slow computer', 'Heavy backpack', 'Tight shoes', 'Remote control out of batteries', 'Flashlight turning off', 'Suitcase hard to close', 'Very soft pillow', 'Bent fork', 'Exploding champagne bottle', 'Balloon flying away'],
      3: ['An old stuck typewriter', 'A shield protecting from arrows', 'A lumberjack axe cutting a trunk', 'An old man\'s cane that breaks', 'A magnifying glass burning a paper', 'A game controller vibrating a lot', 'A crown falling off a head', 'A sword that won\'t come out of the stone', 'A padlock without a key', 'An electric toothbrush vibrating']
    }
  },

  {
    id: 'comida', icon: 'comida_pizza.png',
    words_es: {
      1: ['Pizza', 'Helado', 'Manzana', 'Banana', 'Huevo', 'Pan', 'Sopa', 'Carne', 'Pollo', 'Queso', 'Pastel', 'Sushi', 'Taco', 'Chocolate', 'Arroz'],
      2: ['Comer espagueti', 'Beber batido con sorbete', 'Pelar una banana', 'Batir huevos con tenedor', 'Tomar sopa muy caliente', 'Comer una hamburguesa gigante', 'Cortar un pastel de cumpleaños', 'Hacer un asado a la parrilla', 'Freír papas fritas', 'Chupar una piruleta'],
      3: ['Pelar una cebolla y empezar a llorar', 'Comer un limón muy ácido', 'Limpiar el piso después de tirar la comida', 'Intentar abrir un frasco de mermelada muy duro', 'Comer palomitas de maíz en el cine con miedo', 'Alguien que se quema la lengua con café', 'Tratar de comer con palillos chinos por primera vez', 'Alimentar a un bebé que no quiere comer', 'Hacer una pizza lanzando la masa al aire', 'Servir una mesa de restaurante con muchos platos']
    },
    words_en: {
      1: ['Pizza', 'Ice Cream', 'Apple', 'Banana', 'Egg', 'Bread', 'Soup', 'Meat', 'Chicken', 'Cheese', 'Cake', 'Sushi', 'Taco', 'Chocolate', 'Rice'],
      2: ['Eating spaghetti', 'Drinking a milkshake with a straw', 'Peeling a banana', 'Whisking eggs with a fork', 'Eating very hot soup', 'Eating a giant hamburger', 'Cutting a birthday cake', 'Doing a BBQ on the grill', 'Frying french fries', 'Licking a lollipop'],
      3: ['Peeling an onion and starting to cry', 'Eating a very sour lemon', 'Cleaning the floor after spilling food', 'Trying to open a very tight jam jar', 'Eating popcorn at the cinema while scared', 'Someone burning their tongue with coffee', 'Trying to eat with chopsticks for the first time', 'Feeding a baby who doesn\'t want to eat', 'Making a pizza by tossing dough in the air', 'Serving a restaurant table with many plates']
    }
  },

  {
    id: 'fiesta', icon: 'fiesta_confetti.png',
    words_es: {
      1: ['Fiesta', 'Pastel', 'Regalo', 'Baile', 'Globo', 'Música', 'Vela', 'Disfraz', 'Máscara', 'Confeti', 'Boda', 'Navidad', 'Piñata', 'Brindis', 'Juego'],
      2: ['Soplar las velas', 'Romper la piñata', 'Abrir un regalo sorpresa', 'Hacer un brindis con amigos', 'Bailar el vals', 'Cantar en el karaoke', 'Lanzar confeti al aire', 'Ponerse una máscara de monstruo', 'Bailar la conga en fila', 'Inflar globos para la fiesta'],
      3: ['Alguien tratando de no llorar en una boda', 'Un DJ que pierde el ritmo de la música', 'Bailar la Macarena de forma divertida', 'Saltar bajo el limbo muy bajo', 'Alguien que se marea después de dar vueltas por la piñata', 'Hacer un discurso de agradecimiento y olvidarse las palabras', 'Intentar atrapar el ramo de flores en una boda', 'Un niño que se asusta con los fuegos artificiales', 'Ponerse un disfraz muy incómodo que pica', 'Dos personas brindando y chocando copas']
    },
    words_en: {
      1: ['Party', 'Cake', 'Gift', 'Dance', 'Balloon', 'Music', 'Candle', 'Costume', 'Mask', 'Confetti', 'Wedding', 'Christmas', 'Piñata', 'Toast', 'Game'],
      2: ['Blowing out candles', 'Breaking the piñata', 'Opening a surprise gift', 'Making a toast with friends', 'Dancing the waltz', 'Singing karaoke', 'Throwing confetti in the air', 'Putting on a monster mask', 'Dancing the conga in a line', 'Inflating balloons for the party'],
      3: ['Someone trying not to cry at a wedding', 'A DJ who loses the beat of the music', 'Dancing the Macarena in a funny way', 'Going under a very low limbo stick', 'Someone getting dizzy after spinning for the piñata', 'Giving a thank-you speech and forgetting the words', 'Trying to catch the flower bouquet at a wedding', 'A child getting scared of fireworks', 'Putting on a very uncomfortable, itchy costume', 'Two people toasting and clinking glasses']
    }
  },

  {
    id: 'viajes', icon: 'viajes_maleta.png',
    words_es: {
      1: ['Avión', 'Tren', 'Barco', 'Playa', 'Maleta', 'Mapa', 'Hotel', 'Taxi', 'Metro', 'Isla', 'Montaña', 'Camping', 'Faro', 'Selva', 'Pasaporte'],
      2: ['Volar en avión con miedo', 'Remar en una canoa', 'Caminar sobre la arena caliente', 'Sacar muchas fotos del paisaje', 'Armar una carpa de camping', 'Mirar por la ventana del tren', 'Dormir en un autobús profundamente', 'Subir una montaña con mochila', 'Perderse usando un mapa', 'Pedir un taxi apurado'],
      3: ['Un turista que no entiende el idioma local', 'Un pasajero que pierde su maleta en la cinta', 'Alguien tratando de pasar por seguridad sin pitar', 'Un capitán de barco en medio de una tormenta', 'Un profesional que busca agua', 'Subir a un globo aerostático que se mueve mucho', 'Alguien que se olvida el pasaporte en casa', 'Tratar de comer comida exótica muy picante', 'Un guía de safari señalando un león invisible', 'Alguien tratando de escalar el Everest con mucho frío']
    },
    words_en: {
      1: ['Airplane', 'Train', 'Ship', 'Beach', 'Suitcase', 'Map', 'Hotel', 'Taxi', 'Subway', 'Island', 'Mountain', 'Camping', 'Lighthouse', 'Jungle', 'Passport'],
      2: ['Flying on a plane with fear', 'Rowing a canoe', 'Walking on hot sand', 'Taking many photos of the landscape', 'Setting up a camping tent', 'Looking out of the train window', 'Sleeping soundly on a bus', 'Climbing a mountain with a backpack', 'Getting lost using a map', 'Ordering a taxi in a hurry'],
      3: ['A tourist who doesn\'t understand the local language', 'A passenger losing their suitcase on the belt', 'Someone trying to go through security without beeping', 'A ship captain in the middle of a storm', 'An exhausted backpacker looking for water', 'Going up in a hot air balloon that moves a lot', 'Someone forgetting their passport at home', 'Trying to eat very spicy exotic food', 'A safari guide pointing at an invisible lion', 'Someone trying to climb Everest in extreme cold']
    }
  },

  {
    id: 'sorpresa', icon: 'sorpresa_regalo.png',
    words_es: {
      1: ['Mago', 'Regalo', 'Tesoro', 'Secreto', 'Truco', 'Premio', 'Lupa', 'Cofre', 'Llave', 'Carta', 'Dado', 'Ruleta', 'Puerta', 'Trampa', 'Adivinanza'],
      2: ['Sacar un conejo de la galera', 'Encontrar un tesoro escondido', 'Seguir huellas de detective', 'Descifrar un código secreto', 'Abrir una caja fuerte', 'Desaparecer una moneda', 'Entrar en una habitación secreta', 'Caer en una trampa cómica', 'Hacer un truco de cartas', 'Recibir una noticia inesperada'],
      3: ['Un mago que el truco le sale mal', 'Un detective que encuentra una pista falsa', 'Un escapista tratando de soltarse de cadenas', 'Alguien que descubre un pasadizo detrás de un librero', 'Una persona que gana la lotería y no lo puede creer', 'Un ninja que aparece y desaparece rápidamente', 'Un explorador que activa una trampa en un templo', 'Un hipnotizador tratando de dormir a alguien', 'Un niño abriendo un regalo que no le gusta nada', 'Alguien que recibe una fiesta sorpresa y se asusta']
    },
    words_en: {
      1: ['Magician', 'Gift', 'Treasure', 'Secret', 'Trick', 'Prize', 'Magnifying glass', 'Chest', 'Key', 'Letter', 'Dice', 'Roulette', 'Door', 'Trap', 'Riddle'],
      2: ['Pulling a rabbit out of a hat', 'Finding a hidden treasure', 'Following detective footprints', 'Decoding a secret code', 'Opening a safe', 'Making a coin disappear', 'Entering a secret room', 'Falling into a funny trap', 'Doing a card trick', 'Receiving unexpected news'],
      3: ['A magician whose trick goes wrong', 'A detective who finds a false clue', 'An escapist trying to break free from chains', 'Someone discovering a passage behind a bookshelf', 'A person who wins the lottery and can\'t believe it', 'A ninja appearing and disappearing quickly', 'An explorer triggering a trap in a temple', 'A hypnotist trying to put someone to sleep', 'A child opening a gift they don\'t like at all', 'Someone getting a surprise party and being scared']
    }
  },

  {
    id: 'verano', icon: 'verano_sol.png',
    words_es: {
      1: ['Sol', 'Playa', 'Piscina', 'Olas', 'Helado', 'Sandía', 'Palmera', 'Cangrejo', 'Surf', 'Toalla', 'Gafas', 'Hamaca', 'Abanico', 'Bikini', 'Verano'],
      2: ['Ponerse protector solar', 'Espantar mosquitos', 'Hacer un castillo de arena', 'Saltar una ola grande', 'Mecerse en una hamaca', 'Bucear con snorkel', 'Beber limonada fría', 'Usar un ventilador roto', 'Jugar con una pelota de playa', 'Tomar sol y quemarse la espalda'],
      3: ['Un surfista que se cae de la tabla con gracia', 'Un niño que se quema los pies caminando en la arena', 'Alguien que no puede cerrar su sombrilla por el viento', 'Un socorrista atento con sus binoculares', 'Alguien tratando de comer un helado que se derrite rápido', 'Un turista luchando con un flotador gigante en la piscina', 'Un cangrejo que te pellizca el dedo del pie', 'Alguien que pierde sus gafas de sol en el mar', 'Hacer una barbacoa y que salga mucho humo', 'Dormir una siesta con un mosquito zumbando cerca']
    },
    words_en: {
      1: ['Sun', 'Beach', 'Pool', 'Waves', 'Ice Cream', 'Watermelon', 'Palm tree', 'Crab', 'Surfing', 'Towel', 'Sunglasses', 'Hammock', 'Fan', 'Bikini', 'Summer'],
      2: ['Putting on sunscreen', 'Shooing mosquitoes away', 'Building a sandcastle', 'Jumping a big wave', 'Swinging in a hammock', 'Snorkeling underwater', 'Drinking cold lemonade', 'Using a broken electric fan', 'Playing with a beach ball', 'Sunbathing and burning your back'],
      3: ['A surfer falling gracefully off their board', 'A child burning their feet walking on the sand', 'Someone unable to close their umbrella due to the wind', 'A focused lifeguard with binoculars', 'Someone trying to eat ice cream that melts fast', 'A tourist struggling with a giant pool floatie', 'A crab pinching your toe', 'Someone losing their sunglasses in the sea', 'Doing a BBQ and having too much smoke', 'Taking a nap with a mosquito buzzing nearby']
    }
  },

  {
    id: 'juegos', icon: 'juegos_controller.png',
    words_es: {
      1: ['Mario', 'Pac-Man', 'Tetris', 'Minecraft', 'Fortnite', 'Ajedrez', 'Monopoly', 'Dado', 'Cartas', 'Dominó', 'Bingo', 'Jenga', 'Joystick', 'Nivel', 'Consola'],
      2: ['Saltar como Mario Bros', 'Jugar al Twister', 'Lanzar dardos al blanco', 'Derribar pinos de boliche', 'Mezclar un mazo de cartas', 'Hacer una torre de Jenga alta', 'Ponerse un casco de Realidad Virtual', 'Hacer un baile de la victoria de Fortnite', 'Perder en el Monopoly y enojarse', 'Jugar al piedra, papel o tijera'],
      3: ['Un jugador que se queda sin batería en el control', 'Alguien jugando un juego de terror con mucho miedo', 'Un Boss final recibiendo muchos golpes', 'Un jugador de ajedrez pensando intensamente', 'Alguien que se enreda jugando al Twister', 'Un niño que gana un peluche en la máquina de garras', 'Hacer el ruido y movimiento de un Pinball', 'Un rompecabezas de mil piezas que le falta una', 'Un jugador de casino gritando ¡BINGO!', 'Alguien atrapado dentro de un videojuego de arcade']
    },
    words_en: {
      1: ['Mario', 'Pac-Man', 'Tetris', 'Minecraft', 'Fortnite', 'Chess', 'Monopoly', 'Dice', 'Cards', 'Dominoes', 'Bingo', 'Jenga', 'Joystick', 'Level', 'Console'],
      2: ['Jumping like Mario Bros', 'Playing Twister', 'Throwing darts at a target', 'Knocking down bowling pins', 'Shuffling a deck of cards', 'Building a tall Jenga tower', 'Putting on a Virtual Reality headset', 'Doing a Fortnite victory dance', 'Losing at Monopoly and getting angry', 'Playing rock, paper, scissors'],
      3: ['A gamer whose controller runs out of battery', 'Someone playing a horror game with lots of fear', 'A final Boss receiving many hits', 'A chess player thinking intensely', 'Someone getting tangled playing Twister', 'A child winning a plushie in the claw machine', 'Making the sound and motion of a Pinball machine', 'A thousand-piece puzzle missing one piece', 'A casino player shouting BINGO!', 'Someone trapped inside an arcade video game']
    }
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
    puntuacion: 'PUNTUACIÓN<br>OBTENIDA:',
    puntuacionGanadora: 'PUNTUACIÓN<br>GANADORA:',
    volverJugar: 'VOLVER A JUGAR',
    menu: 'MENÚ',
    configTitle: 'Mímica Pro -<br>Configuración',
    idioma: 'Idioma / Language',
    musicaLabel: 'Música',
    vibracion: 'Vibración',
    tiempoJuego: 'Tiempo de Juego',
    dificultad: 'Dificultad',
    diff_facil: 'Fácil',
    diff_medio: 'Medio',
    diff_dificil: 'Difícil',
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
    puntuacion: 'OBTAINED<br>SCORE:',
    puntuacionGanadora: 'WINNING<br>SCORE:',
    volverJugar: 'PLAY AGAIN',
    menu: 'MENU',
    configTitle: 'Mimica Pro -<br>Settings',
    idioma: 'Language / Idioma',
    musicaLabel: 'Music',
    vibracion: 'Vibration',
    tiempoJuego: 'Game Time',
    dificultad: 'Difficulty',
    diff_facil: 'Easy',
    diff_medio: 'Medium',
    diff_dificil: 'Hard',
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
