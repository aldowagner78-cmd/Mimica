import csv

def write_csv():
    outfile = 'charadas_latam_database.csv'
    header = ['Categoría', 'Nivel', 'Español (Latino)', 'Inglés']
    
    # MASTER DATABASE CONTENT
    # Format: (Level, ES, EN)
    
    # 1. ANIMALES
    animales = [
        (1, 'León', 'Lion'), (1, 'Vaca', 'Cow'), (1, 'Perro', 'Dog'), (1, 'Gato', 'Cat'), (1, 'Elefante', 'Elephant'), (1, 'Jirafa', 'Giraffe'), (1, 'Mono', 'Monkey'), (1, 'Tigre', 'Tiger'), (1, 'Oso', 'Bear'), (1, 'Conejo', 'Rabbit'), (1, 'Ratón', 'Mouse'), (1, 'Cerdo', 'Pig'), (1, 'Oveja', 'Sheep'), (1, 'Caballo', 'Horse'), (1, 'Pato', 'Duck'), (1, 'Gallina', 'Hen'), (1, 'Águila', 'Eagle'), (1, 'Serpiente', 'Snake'), (1, 'Tiburón', 'Shark'), (1, 'Ballena', 'Whale'), (1, 'Delfín', 'Dolphin'), (1, 'Pingüino', 'Penguin'), (1, 'Sapo', 'Toad'), (1, 'Tortuga', 'Turtle'), (1, 'Araña', 'Spider'), (1, 'Mariposa', 'Butterfly'), (1, 'Abeja', 'Bee'), (1, 'Hormiga', 'Ant'), (1, 'Mosquito', 'Mosquito'), (1, 'Cangrejo', 'Crab'),
        (2, 'Ordeñar una vaca', 'Milking a cow'), (2, 'Montar a caballo', 'Riding a horse'), (2, 'Pasear al perro', 'Walking the dog'), (2, 'Nadar con delfines', 'Swimming with dolphins'), (2, 'Cazar mariposas', 'Catching butterflies'), (2, 'Alimentar cerdos', 'Feeding pigs'), (2, 'Huir de un león', 'Running from a lion'), (2, 'Bañar al gato', 'Bathing the cat'), (2, 'Esquilar oveja', 'Shearing a sheep'), (2, 'Ver aves', 'Birdwatching'),
        (3, 'Un elefante bailando ballet', 'An elephant dancing ballet'), (3, 'Un pingüino resbalando en hielo', 'A penguin slipping on ice'), (3, 'Un gato asustado por un pepino', 'A cat scared by a cucumber'), (3, 'Un perro persiguiendo su cola', 'A dog chasing its tail'), (3, 'Un mono robando una cámara', 'A monkey stealing a camera'), (3, 'Un canguro boxeando', 'A boxing kangaroo'), (3, 'Una jirafa bebiendo agua', 'A giraffe drinking water'), (3, 'Un oso rascándose la espalda', 'A bear scratching its back'), (3, 'Un flamenco perdiendo el equilibrio', 'A flamingo losing balance'), (3, 'Un hámster corriendo rápido', 'A hamster running fast')
    ]

    # 2. PELÍCULAS
    peliculas = [
        (1, 'Titanic', 'Titanic'), (1, 'Avatar', 'Avatar'), (1, 'Shrek', 'Shrek'), (1, 'Frozen', 'Frozen'), (1, 'Coco', 'Coco'), (1, 'El Rey León', 'The Lion King'), (1, 'Toy Story', 'Toy Story'), (1, 'Matrix', 'Matrix'), (1, 'Jurassik Park', 'Jurassic Park'), (1, 'Harry Potter', 'Harry Potter'), (1, 'Star Wars', 'Star Wars'), (1, 'Gladiador', 'Gladiator'), (1, 'Tiburón', 'Jaws'), (1, 'Rocky', 'Rocky'), (1, 'Barbie', 'Barbie'), (1, 'Batman', 'Batman'), (1, 'Spiderman', 'Spiderman'), (1, 'Superman', 'Superman'), (1, 'Aladdin', 'Aladdin'), (1, 'Mulan', 'Mulan'),
        (2, 'Jack y Rose en la proa', 'Jack and Rose at the bow'), (2, 'Darth Vader soy tu padre', 'Darth Vader I am your father'), (2, 'Simba levantado por Rafiki', 'Simba lifted by Rafiki'), (2, 'E.T. volando en bicicleta', 'E.T. flying on a bike'), (2, 'Forrest Gump corriendo', 'Forrest Gump running'), (2, 'Neo esquivando balas', 'Neo dodging bullets'), (2, 'Rocky subiendo escaleras', 'Rocky running up stairs'), (2, 'Spiderman lanzando telaraña', 'Spiderman shooting web'), (2, 'El Padrino acariciando gato', 'The Godfather petting cat'), (2, 'Marilyn Monroe vestido', 'Marilyn Monroe dress flying'),
        (3, 'Hulk aplastando un auto', 'Hulk smashing a car'), (3, 'Buzz Lightyear cayendo con estilo', 'Buzz Lightyear falling with style'), (3, 'Gollum hablando con el anillo', 'Gollum talking to the ring'), (3, 'Jack Sparrow corriendo borracho', 'Jack Sparrow running drunk'), (3, 'Yoda levantando la nave', 'Yoda lifting the ship'), (3, 'El T-Rex rugiendo bajo la lluvia', 'T-Rex roaring in the rain'), (3, 'Dorothy golpeando los talones', 'Dorothy clicking her heels'), (3, 'King Kong en el edificio', 'King Kong on the building'), (3, 'El Genio saliendo de la lámpara', 'Genie coming out of the lamp'), (3, 'Tarzán golpeando su pecho', 'Tarzan beating his chest')
    ]

    # 3. HÉROES
    heroes = [
        (1, 'Batman', 'Batman'), (1, 'Superman', 'Superman'), (1, 'Spiderman', 'Spiderman'), (1, 'Hulk', 'Hulk'), (1, 'Thor', 'Thor'), (1, 'Iron Man', 'Iron Man'), (1, 'Mujer Maravilla', 'Wonder Woman'), (1, 'Flash', 'Flash'), (1, 'Capitán América', 'Captain America'), (1, 'Aquaman', 'Aquaman'), (1, 'Viuda Negra', 'Black Widow'), (1, 'Pantera Negra', 'Black Panther'), (1, 'Doctor Strange', 'Doctor Strange'), (1, 'Wolverine', 'Wolverine'), (1, 'Deadpool', 'Deadpool'), (1, 'Linterna Verde', 'Green Lantern'), (1, 'Ant-Man', 'Ant-Man'), (1, 'Robin', 'Robin'), (1, 'Gatúbela', 'Catwoman'), (1, 'Joker', 'Joker'),
        (2, 'Volar como Superman', 'Flying like Superman'), (2, 'Lanzar escudo', 'Throwing shield'), (2, 'Trepar pared', 'Climbing wall'), (2, 'Disparar láser', 'Shooting laser'), (2, 'Hacerse invisible', 'Turning invisible'), (2, 'Correr super rápido', 'Running super fast'), (2, 'Nadar bajo el agua', 'Swimming underwater'), (2, 'Levantar un auto', 'Lifting a car'), (2, 'Usar el lazo mágico', 'Using magic lasso'), (2, 'Llamar al martillo', 'Calling the hammer'),
        (3, 'Hulk intentando enhebrar una aguja', 'Hulk trying to thread a needle'), (3, 'Batman perdiendo las llaves del Batimóvil', 'Batman losing Batmobile keys'), (3, 'Spiderman pegado a su propia telaraña', 'Spiderman stuck in his own web'), (3, 'Superman con miedo a las alturas', 'Superman afraid of heights'), (3, 'Flash esperando el autobús', 'Flash waiting for the bus'), (3, 'Thor tratando de cambiar un foco', 'Thor trying to change a lightbulb'), (3, 'Iron Man sin batería en el traje', 'Iron Man out of battery'), (3, 'Capitán América usando un celular moderno', 'Captain America using a smartphone'), (3, 'Aquaman ahogándose en un vaso de agua', 'Aquaman drowning in a glass of water'), (3, 'Mujer Maravilla despeinada por el viento', 'Wonder Woman hair messed by wind')
    ]

    # 4. ACCIÓN
    accion = [
        (1, 'Correr', 'Running'), (1, 'Saltar', 'Jumping'), (1, 'Bailar', 'Dancing'), (1, 'Cantar', 'Singing'), (1, 'Comer', 'Eating'), (1, 'Dormir', 'Sleeping'), (1, 'Llorar', 'Crying'), (1, 'Reír', 'Laughing'), (1, 'Nadar', 'Swimming'), (1, 'Volar', 'Flying'), (1, 'Escribir', 'Writing'), (1, 'Leer', 'Reading'), (1, 'Cocinar', 'Cooking'), (1, 'Pintar', 'Painting'), (1, 'Barrer', 'Sweeping'), (1, 'Manejar', 'Driving'), (1, 'Pescar', 'Fishing'), (1, 'Aplaudir', 'Clapping'), (1, 'Abrazar', 'Hugging'), (1, 'Besar', 'Kissing'),
        (2, 'Planchar una camisa', 'Ironing a shirt'), (2, 'Atar los cordones', 'Tying shoelaces'), (2, 'Lavarse los dientes', 'Brushing teeth'), (2, 'Cortar el pasto', 'Mowing the lawn'), (2, 'Inflar un globo', 'Inflating a balloon'), (2, 'Cambiar un pañal', 'Changing a diaper'), (2, 'Palar nieve', 'Shoveling snow'), (2, 'Martillar un clavo', 'Hammering a nail'), (2, 'Exprimir naranjas', 'Squeezing oranges'), (2, 'Abrir un frasco duro', 'Opening a stuck jar'),
        (3, 'Caminar sobre carbón caliente', 'Walking on hot coals'), (3, 'Intentar estornudar y no poder', 'Trying to sneeze and failing'), (3, 'Pisar caca de perro', 'Stepping on dog poop'), (3, 'Caminar contra un viento huracanado', 'Walking against hurricane wind'), (3, 'Tratando de matar una mosca molesta', 'Trying to kill an annoying fly'), (3, 'Ponerse jeans muy ajustados', 'Putting on very tight jeans'), (3, 'Quemar la comida y esconderla', 'Burning food and hiding it'), (3, 'Bailar tango con una escoba', 'Dancing tango with a broom'), (3, 'Desactivar una bomba con miedo', 'Defusing a bomb with fear'), (3, 'Hacer equilibrio en la cuerda floja', 'Balancing on a tightrope')
    ]

    # 5. DEPORTES
    deportes = [
        (1, 'Fútbol', 'Soccer'), (1, 'Básquet', 'Basketball'), (1, 'Tenis', 'Tennis'), (1, 'Natación', 'Swimming'), (1, 'Boxeo', 'Boxing'), (1, 'Rugby', 'Rugby'), (1, 'Golf', 'Golf'), (1, 'Vóley', 'Volleyball'), (1, 'Béisbol', 'Baseball'), (1, 'Hockey', 'Hockey'), (1, 'Esquí', 'Skiing'), (1, 'Surf', 'Surfing'), (1, 'Ciclismo', 'Cycling'), (1, 'Patinaje', 'Skating'), (1, 'Karate', 'Karate'), (1, 'Gimnasia', 'Gymnastics'), (1, 'Pesca', 'Fishing'), (1, 'Atletismo', 'Athletics'), (1, 'Sumo', 'Sumo'), (1, 'Arquería', 'Archery'),
        (2, 'Meter un gol', 'Scoring a goal'), (2, 'Hacer un home run', 'Hitting a home run'), (2, 'Nocaut en boxeo', 'Knockout in boxing'), (2, 'Saque de tenis', 'Tennis serve'), (2, 'Tirar un penal', 'Shooting a penalty'), (2, 'Caerse esquiando', 'Falling while skiing'), (2, 'Atrapar una pelota alta', 'Catching a high ball'), (2, 'Hacer pesas', 'Lifting weights'), (2, 'Remar en kayak', 'Rowing a kayak'), (2, 'Escalar una montaña', 'Climbing a mountain'),
        (3, 'Un luchador de sumo bailando ballet', 'Sumo wrestler dancing ballet'), (3, 'Un tenista rompiendo la raqueta de bronca', 'Tennis player smashing racket in anger'), (3, 'Un arquero con miedo a la pelota', 'Goalkeeper afraid of the ball'), (3, 'Un surfista perseguido por un tiburón', 'Surfer chased by a shark'), (3, 'Un boxeador noqueándose a sí mismo', 'Boxer knocking himself out'), (3, 'Un golfista festejando antes de tiempo', 'Golfer celebrating too early'), (3, 'Un ciclista perdiendo la cadena', 'Cyclist losing the chain'), (3, 'Un nadador con calambre en la pierna', 'Swimmer with leg cramp'), (3, 'Un jugador de básquet muy bajito', 'Very short basketball player'), (3, 'Un esquiador chocando con un árbol', 'Skier hitting a tree')
    ]

    # 6. MÚSICA
    musica = [
        (1, 'Guitarra', 'Guitar'), (1, 'Piano', 'Piano'), (1, 'Batería', 'Drums'), (1, 'Violín', 'Violin'), (1, 'Trompeta', 'Trumpet'), (1, 'Microfono', 'Microphone'), (1, 'Saxofón', 'Saxophone'), (1, 'Flauta', 'Flute'), (1, 'Acordeón', 'Accordion'), (1, 'Arpa', 'Harp'), (1, 'Cantante', 'Singer'), (1, 'DJ', 'DJ'), (1, 'Director', 'Conductor'), (1, 'Rock', 'Rock'), (1, 'Pop', 'Pop'), (1, 'Jazz', 'Jazz'), (1, 'Tango', 'Tango'), (1, 'Salsa', 'Salsa'), (1, 'Ópera', 'Opera'), (1, 'Rap', 'Rap'),
        (2, 'Tocar la guitarra eléctrica', 'Playing electric guitar'), (2, 'Cantar ópera', 'Singing opera'), (2, 'Dirigir una orquesta', 'Conducting an orchestra'), (2, 'Romper una guitarra', 'Smashing a guitar'), (2, 'Bailar reggaetón', 'Dancing reggaeton'), (2, 'Tocar el piano rápido', 'Playing piano fast'), (2, 'Hacer beatbox', 'Beatboxing'), (2, 'Afinar un violín', 'Tuning a violin'), (2, 'Tocar la batería fuerte', 'Playing drums loud'), (2, 'Cantar en la ducha', 'Singing in the shower'),
        (3, 'Un rockero rompiendo la guitarra y llorando', 'Rocker smashing guitar and crying'), (3, 'Un director de orquesta espantando moscas', 'Conductor swatting flies'), (3, 'Un cantante olvidándose la letra', 'Singer forgetting the lyrics'), (3, 'Un DJ que se queda dormido', 'DJ falling asleep'), (3, 'Tocar el piano con los pies', 'Playing piano with feet'), (3, 'Un violinista con mucha picazón', 'Violinist with an itch'), (3, 'Un baterista perdiendo los palillos', 'Drummer losing sticks'), (3, 'Un cantante de ópera rompiendo copas', 'Opera singer breaking glasses'), (3, 'Un rapero que se traba al hablar', 'Rapper stuttering'), (3, 'Bailarvalses con un esqueleto', 'Dancing waltz with a skeleton')
    ]

    # 7. PROFESIONES
    profesiones = [
        (1, 'Doctor', 'Doctor'), (1, 'Maestro', 'Teacher'), (1, 'Policía', 'Police'), (1, 'Bombero', 'Firefighter'), (1, 'Cocinero', 'Chef'), (1, 'Mecánico', 'Mechanic'), (1, 'Pintor', 'Painter'), (1, 'Payaso', 'Clown'), (1, 'Mago', 'Magician'), (1, 'Astronauta', 'Astronaut'), (1, 'Juez', 'Judge'), (1, 'Dentista', 'Dentist'), (1, 'Granjero', 'Farmer'), (1, 'Actor', 'Actor'), (1, 'Cantante', 'Singer'), (1, 'Soldado', 'Soldier'), (1, 'Enfermera', 'Nurse'), (1, 'Arquitecto', 'Architect'), (1, 'Fotógrafo', 'Photographer'), (1, 'Carpintero', 'Carpenter'),
        (2, 'Apagar un incendio', 'Putting out a fire'), (2, 'Operar un paciente', 'Operating on a patient'), (2, 'Dirigir el tráfico', 'Directing traffic'), (2, 'Sacar una muela', 'Pulling a tooth'), (2, 'Enseñar matemáticas', 'Teaching math'), (2, 'Cocinar una sopa', 'Cooking soup'), (2, 'Arreglar un auto', 'Fixing a car'), (2, 'Ordeñar una vaca', 'Milking a cow'), (2, 'Sacar una foto', 'Taking a photo'), (2, 'Construir una pared', 'Building a wall'),
        (3, 'Un dentista con miedo a los dientes', 'Dentist afraid of teeth'), (3, 'Un bombero con miedo al fuego', 'Firefighter afraid of fire'), (3, 'Un cirujano con hipo', 'Surgeon with hiccups'), (3, 'Un mimo atrapado en una caja real', 'Mime trapped in a real box'), (3, 'Un astronauta flotando sin control', 'Astronaut floating uncontrollably'), (3, 'Un mago fallando el truco', 'Magician failing a trick'), (3, 'Un profesor perdiendo la paciencia', 'Teacher losing patience'), (3, 'Un policía persiguiendo una tortuga', 'Police chasing a turtle'), (3, 'Un pintor manchándose todo', 'Painter getting paint everywhere'), (3, 'Un juez golpeando el martillo en su dedo', 'Judge hitting finger with gavel')
    ]

    # 8. OBJETOS
    objetos = [
        (1, 'Celular', 'Phone'), (1, 'Computadora', 'Computer'), (1, 'Silla', 'Chair'), (1, 'Mesa', 'Table'), (1, 'Cama', 'Bed'), (1, 'Lámpara', 'Lamp'), (1, 'Reloj', 'Clock'), (1, 'Espejo', 'Mirror'), (1, 'Lápiz', 'Pencil'), (1, 'Libro', 'Book'), (1, 'Tijeras', 'Scissors'), (1, 'Cuchara', 'Spoon'), (1, 'Tenedor', 'Fork'), (1, 'Cuchillo', 'Knife'), (1, 'Vaso', 'Glass'), (1, 'Botella', 'Bottle'), (1, 'Llave', 'Key'), (1, 'Mochila', 'Backpack'), (1, 'Paraguas', 'Umbrella'), (1, 'Escoba', 'Broom'),
        (2, 'Abrir un paraguas', 'Opening an umbrella'), (2, 'Escribir con lápiz', 'Writing with pencil'), (2, 'Cortar con tijeras', 'Cutting with scissors'), (2, 'Leer un libro', 'Reading a book'), (2, 'Hablar por celular', 'Talking on phone'), (2, 'Dormir en la cama', 'Sleeping in bed'), (2, 'Barrer el piso', 'Sweeping the floor'), (2, 'Mirarse al espejo', 'Looking in mirror'), (2, 'Tomar agua del vaso', 'Drinking from glass'), (2, 'Abrir una puerta con llave', 'Unlocking a door'),
        (3, 'Una lavadora caminando sola', 'Washing machine walking alone'), (3, 'Una tostadora quemando el pan', 'Toaster burning bread'), (3, 'Un paraguas dado vuelta por viento', 'Umbrella flipped by wind'), (3, 'Una aspiradora tragándose la cortina', 'Vacuum swallowing curtain'), (3, 'Un teléfono vibrando en la mesa', 'Phone vibrating on table'), (3, 'Una impresora atascada', 'Printer jamming'), (3, 'Un inodoro desbordado', 'Toilet overflowing'), (3, 'Una botella de ketchup que no sale', 'Ketchup bottle stuck'), (3, 'Un ventilador tirando papeles', 'Fan blowing papers'), (3, 'Una silla que se rompe al sentarse', 'Chair breaking when sitting')
    ]

    # 9. COMIDA
    comida = [
        (1, 'Pizza', 'Pizza'), (1, 'Hamburguesa', 'Burger'), (1, 'Helado', 'Ice Cream'), (1, 'Taco', 'Taco'), (1, 'Sushi', 'Sushi'), (1, 'Sopa', 'Soup'), (1, 'Chocolate', 'Chocolate'), (1, 'Banana', 'Banana'), (1, 'Manzana', 'Apple'), (1, 'Huevo', 'Egg'), (1, 'Pan', 'Bread'), (1, 'Queso', 'Cheese'), (1, 'Carne', 'Meat'), (1, 'Pollo', 'Chicken'), (1, 'Pescado', 'Fish'), (1, 'Fideos', 'Noodles'), (1, 'Ensalada', 'Salad'), (1, 'Torta', 'Cake'), (1, 'Jugo', 'Juice'), (1, 'Café', 'Coffee'),
        (2, 'Comer fideos', 'Eating noodles'), (2, 'Cortar carne', 'Cutting meat'), (2, 'Pelar una banana', 'Peeling a banana'), (2, 'Lamer un helado', 'Licking ice cream'), (2, 'Preparar un sándwich', 'Making a sandwich'), (2, 'Revolver la sopa', 'Stirring soup'), (2, 'Romper un huevo', 'Cracking an egg'), (2, 'Tomar café caliente', 'Drinking hot coffee'), (2, 'Poner sal a la comida', 'Salting food'), (2, 'Mascar chicle', 'Chewing gum'),
        (3, 'Intentar comer gelatina con tenedor', 'Trying to eat jelly with fork'), (3, 'Morder un limón muy ácido', 'Biting a sour lemon'), (3, 'Comer espagueti sin manos', 'Eating spaghetti no hands'), (3, 'Se te cae el helado al suelo', 'Dropping ice cream on floor'), (3, 'Tomar algo muy caliente y quemarse', 'Drinking hot drink and burning'), (3, 'Tragar una semilla de sandía', 'Swallowing watermelon seed'), (3, 'Llorar cortando cebolla', 'Crying chopping onions'), (3, 'Comer comida muy picante', 'Eating very spicy food'), (3, 'Intentar abrir un coco', 'Trying to open coconut'), (3, 'Hacer globos de chicle y que explote', 'Gum bubble popping on face')
    ]

    # 10. FIESTA
    fiesta = [
        (1, 'Globo', 'Balloon'), (1, 'Torta', 'Cake'), (1, 'Regalo', 'Gift'), (1, 'Piñata', 'Piñata'), (1, 'Vela', 'Candle'), (1, 'Disfraz', 'Costume'), (1, 'Música', 'Music'), (1, 'Baile', 'Dance'), (1, 'Confeti', 'Confetti'), (1, 'Bebida', 'Drink'), (1, 'Payaso', 'Clown'), (1, 'Invitación', 'Invitation'), (1, 'Sorpresa', 'Surprise'), (1, 'Foto', 'Photo'), (1, 'Amigos', 'Friends'),
        (2, 'Soplar las velas', 'Blowing candles'), (2, 'Abrir regalos', 'Opening gifts'), (2, 'Romper la piñata', 'Breaking piñata'), (2, 'Bailar con la abuela', 'Dancing with grandma'), (2, 'Inflar globos', 'Inflating balloons'), (2, 'Servir tarta', 'Serving cake'), (2, 'Sacar una selfie', 'Taking a selfie'), (2, 'Brindar con copas', 'Toasting cups'), (2, 'Poner música', 'Playing music'), (2, 'Jugar a las sillas', 'Playing musical chairs'),
        (3, 'Caerse encima de la torta', 'Falling on the cake'), (3, 'Un payaso perdiendo sus zapatos', 'Clown losing shoes'), (3, 'Cantar cumpleaños desafinado', 'Singing birthday off-key'), (3, 'La piñata no se rompe', 'Piñata won\'t break'), (3, 'Abrir un regalo feo y sonreír', 'Opening ugly gift smiling'), (3, 'Quedarse encerrado en el baño', 'Locked in bathroom'), (3, 'Dormirse en la fiesta', 'Falling asleep at party'), (3, 'Se vuelca la bebida en el vestido', 'Spilling drink on dress'), (3, 'Bailar la conga solo', 'Dancing conga alone'), (3, 'El DJ pone la música equivocada', 'DJ playing wrong music')
    ]

    # 11. VIAJES
    viajes = [
        (1, 'Avión', 'Plane'), (1, 'Maleta', 'Suitcase'), (1, 'Pasaporte', 'Passport'), (1, 'Mapa', 'Map'), (1, 'Playa', 'Beach'), (1, 'Cámara', 'Camera'), (1, 'Hotel', 'Hotel'), (1, 'Tren', 'Train'), (1, 'Montaña', 'Mountain'), (1, 'Auto', 'Car'), (1, 'Boleto', 'Ticket'), (1, 'Isla', 'Island'), (1, 'Turista', 'Tourist'), (1, 'Mochila', 'Backpack'), (1, 'Sol', 'Sun'),
        (2, 'Hacer la maleta', 'Packing suitcase'), (2, 'Perder el vuelo', 'Missing flight'), (2, 'Sacar fotos a todo', 'Taking photos of everything'), (2, 'Mirar el mapa', 'Looking at map'), (2, 'Nadar en el mar', 'Swimming in sea'), (2, 'Subir la montaña', 'Climbing mountain'), (2, 'Pedir un taxi', 'Hailing a taxi'), (2, 'Comprar recuerdos', 'Buying souvenirs'), (2, 'Dormir en el avión', 'Sleeping on plane'), (2, 'Buscar el hotel', 'Searching for hotel'),
        (3, 'Corriendo por el aeropuerto tarde', 'Running late in airport'), (3, 'La maleta no cierra', 'Suitcase won\'t close'), (3, 'Intentar hablar otro idioma', 'Trying to speak language'), (3, 'Quemarse con el sol en la playa', 'Getting sunburn at beach'), (3, 'Perderse en una ciudad nueva', 'Getting lost in new city'), (3, 'Comer comida muy rara', 'Eating weird food'), (3, 'El auto se descompone', 'Car breaking down'), (3, 'Un mosquito en la carpa', 'Mosquito in tent'), (3, 'Olvidar el pasaporte', 'Forgetting passport'), (3, 'Pelear con un mapa gigante', 'Fighting giant map')
    ]

    # 12. SORPRESA
    sorpresa = [
        (1, 'Regalo', 'Gift'), (1, 'Caja', 'Box'), (1, 'Susto', 'Scare'), (1, 'Fiesta', 'Party'), (1, 'Anillo', 'Ring'), (1, 'Carta', 'Letter'), (1, 'Bomba', 'Bomb'), (1, 'Huevo', 'Egg'), (1, 'Mago', 'Magician'), (1, 'Conejo', 'Rabbit'), (1, 'Lotería', 'Lottery'), (1, 'Noticia', 'News'), (1, 'Visita', 'Visit'), (1, 'Secreto', 'Secret'), (1, 'Truco', 'Trick'),
        (2, 'Esconderse detrás de la puerta', 'Hiding behind door'), (2, 'Gritar ¡Sorpresa!', 'Yelling Surprise!'), (2, 'Abrir una caja misteriosa', 'Opening mystery box'), (2, 'Ganar la lotería', 'Winning lottery'), (2, 'Encontrar dinero', 'Finding money'), (2, 'Recibir una carta', 'Getting a letter'), (2, 'Ver un fantasma', 'Seeing a ghost'), (2, 'Revelar un secreto', 'Revealing secret'), (2, 'Hacer un truco de magia', 'Doing magic trick'), (2, 'Asustar a alguien', 'Scaring someone'),
        (3, 'Descubrir que eres adoptado', 'Discovering adoption'), (3, 'Caminar y pisar un chicle', 'Stepping on gum'), (3, 'Encontrar una araña en el zapato', 'Finding spider in shoe'), (3, 'El regalo está vacío', 'Gift is empty'), (3, 'Confundir a alguien con un famoso', 'Mistaking someone for famous'), (3, 'Se te caen los pantalones', 'Pants falling down'), (3, 'Un pájaro te hace caca', 'Bird pooping on you'), (3, 'Sustode película de terror', 'Horror movie scare'), (3, 'Morder una manzana con gusano', 'Biting apple with worm'), (3, 'Romper algo valioso sin querer', 'Breaking valuable accidentally')
    ]

    # 13. VERANO
    verano = [
        (1, 'Sol', 'Sun'), (1, 'Playa', 'Beach'), (1, 'Helado', 'Ice Cream'), (1, 'Piscina', 'Pool'), (1, 'Lentes', 'Sunglasses'), (1, 'Bikini', 'Bikini'), (1, 'Arena', 'Sand'), (1, 'Ola', 'Wave'), (1, 'Calor', 'Heat'), (1, 'Ventilador', 'Fan'), (1, 'Sandia', 'Watermelon'), (1, 'Toalla', 'Towel'), (1, 'Mosquito', 'Mosquito'), (1, 'Surf', 'Surf'), (1, 'Barco', 'Boat'),
        (2, 'Tomar sol', 'Sunbathing'), (2, 'Construir castillo de arena', 'Building sandcastle'), (2, 'Tirarse a la piscina', 'Jumping in pool'), (2, 'Comer sandía', 'Eating watermelon'), (2, 'Abanicarse por calor', 'Fanning self from heat'), (2, 'Ponerse protector solar', 'Putting sunscreen'), (2, 'Nadar estilo perrito', 'Doggy paddle swimming'), (2, 'Manejar un bote', 'Driving a boat'), (2, 'Jugar paleta en la playa', 'Playing beach paddle'), (2, 'Pescar en el muelle', 'Fishing on pier'),
        (3, 'Arena caliente quemando pies', 'Hot sand burning feet'), (3, 'Un cangrejo pellizca el dedo', 'Crab pinching toe'), (3, 'Tragar agua salada', 'Swallowing salt water'), (3, 'Perder la malla en el mar', 'Losing swimsuit in sea'), (3, 'Derritiéndose de calor', 'Melting from heat'), (3, 'Un helado se derrite en la mano', 'Ice cream melting on hand'), (3, 'Intentar abrir sombrilla con viento', 'Opening umbrella in wind'), (3, 'Ser picado por medusa', 'Stung by jellyfish'), (3, 'Tirarse de panza al agua', 'Belly flop into water'), (3, 'Sacudirse la arena pegada', 'Shaking off sticky sand')
    ]

    # 14. JUEGOS
    juegos = [
        (1, 'Cartas', 'Cards'), (1, 'Dados', 'Dice'), (1, 'Ajedrez', 'Chess'), (1, 'Dominó', 'Dominoes'), (1, 'Rompecabezas', 'Puzzle'), (1, 'Videojuego', 'Video Game'), (1, 'Pelota', 'Ball'), (1, 'Escondidas', 'Hide and Seek'), (1, 'Rayuela', 'Hopscotch'), (1, 'Soga', 'Rope'), (1, 'Jenga', 'Jenga'), (1, 'Monopolio', 'Monopoly'), (1, 'Ludo', 'Ludo'), (1, 'Bingo', 'Bingo'), (1, 'Trompo', 'Top'),
        (2, 'Mezclar las cartas', 'Shuffling cards'), (2, 'Tirar los dados', 'Rolling dice'), (2, 'Mover pieza de ajedrez', 'Moving chess piece'), (2, 'Armar un rompecabezas', 'Doing a puzzle'), (2, 'Jugar a la soga', 'Jumping rope'), (2, 'Ganar una partida', 'Winning a game'), (2, 'Hacer trampa', 'Cheating'), (2, 'Jugar videojuegos', 'Playing video games'), (2, 'Esconderse bien', 'Hiding well'), (2, 'Saltar la rayuela', 'Playing hopscotch'),
        (3, 'Perder y enojarse mucho', 'Losing and raging'), (3, 'Tirar el tablero de ajedrez', 'Flipping chess board'), (3, 'La torre de Jenga se cae', 'Jenga tower falling'), (3, 'Tratando de entender las reglas', 'Trying to understand rules'), (3, 'Gritar ¡Bingo! por error', 'Yelling Bingo! by mistake'), (3, 'Hacer trampa y ser descubierto', 'Cheating and getting caught'), (3, 'Quedarse sin batería jugando', 'Battery dying while playing'), (3, 'Perder la última pieza del puzzle', 'Losing last puzzle piece'), (3, 'Jugar a las cartas con un perro', 'Playing cards with a dog'), (3, 'Chocando con la realidad virtual', 'Bumping into VR reality')
    ]

    all_data = {
        'Animales': animales,
        'Películas': peliculas,
        'Héroes': heroes,
        'Acción': accion,
        'Deportes': deportes,
        'Música': musica,
        'Profesiones': profesiones,
        'Objetos': objetos,
        'Comida': comida,
        'Fiesta': fiesta,
        'Viajes': viajes,
        'Sorpresa': sorpresa,
        'Verano': verano,
        'Juegos': juegos
    }

    with open(outfile, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for cat, items in all_data.items():
            for lvl, es, en in items:
                lvl_str = 'Baja' if lvl == 1 else 'Media' if lvl == 2 else 'Alta'
                writer.writerow([cat, lvl_str, es, en])

    print(f"Database rebuilt successfully with correct English translations in {outfile}")

if __name__ == "__main__":
    write_csv()
