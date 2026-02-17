const CACHE_NAME = 'mimica-pro-v2.7.3';
const ASSETS = [
    './',
    './index.html',
    './gameData.js',
    './manifest.json',
    './assets/iconos/animales_leon.png',
    './assets/iconos/peliculas_popcorn.png',
    './assets/iconos/heroes_escudo.png',
    './assets/iconos/accion_rayo.png',
    './assets/iconos/deportes_basket.png',
    './assets/iconos/musica_headphones.png',
    './assets/iconos/profesiones_steth.png',
    './assets/iconos/objetos_lampara.png',
    './assets/iconos/comida_pizza.png',
    './assets/iconos/fiesta_confetti.png',
    './assets/iconos/viajes_maleta.png',
    './assets/iconos/sorpresa_regalo.png',
    './assets/iconos/verano_sol.png',
    './assets/iconos/juegos_controller.png'
];

self.addEventListener('install', (e) => {
    e.waitUntil(
        caches.open(CACHE_NAME).then((cache) => cache.addAll(ASSETS))
    );
});

self.addEventListener('activate', (e) => {
    e.waitUntil(
        caches.keys().then((keys) => {
            return Promise.all(keys.map((k) => {
                if (k !== CACHE_NAME) return caches.delete(k);
            }));
        })
    );
});

self.addEventListener('fetch', (e) => {
    e.respondWith(
        caches.match(e.request).then((res) => res || fetch(e.request))
    );
});
