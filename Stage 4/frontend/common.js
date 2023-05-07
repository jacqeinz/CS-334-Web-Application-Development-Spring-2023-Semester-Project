if (typeof navigator.serviceWorker !== 'undefined') {
  navigator.serviceWorker.register('service-worker.js')
}
const CACHE_NAME = 'cool-cache';

// Add whichever assets you want to pre-cache here:
const PRECACHE_ASSETS = [
  '/',
  '/index.html'
]

// Listener for the install event - pre-caches our assets list on service worker install.
self.addEventListener('install', event => {
  event.waitUntil((async () => {
    const cache = await caches.open(CACHE_NAME);
    cache.addAll(PRECACHE_ASSETS);
  })());
});
self.addEventListener('activate', event => {
  event.waitUntil(clients.claim());
});
self.addEventListener('fetch', event => {
  event.respondWith(async () => {
    const cache = await caches.open(CACHE_NAME);

    // match the request to our cache
    const cachedResponse = await cache.match(event.request);

    // check if we got a valid response
    if (cachedResponse !== undefined) {
      // Cache hit, return the resource
      return cachedResponse;
    } else {
      // Otherwise, go to the network
      return fetch(event.request)
    };
  });
});

async function setupDbConnection() {
  let json = await fetch("defaultData.json").then((response) =>
    response.json()
  );
  let db;
  const request = indexedDB.open("RollingStoneIceCreamStage3", 2);
  request.onerror = (event) => {
    console.error("Failed to open IndexedDb");
  };
  request.onupgradeneeded = (event) => {
    db = event.target.result;

    let createStore;

    for (store of json.stores) {
      console.log(store);
      createStore = db.createObjectStore(store.name, {
        keyPath: "id",
      });
      createStore.createIndex("id", "id", { unique: true });
    }
    createStore.transaction.oncomplete = (event) => {
      for (store of json.stores) {
        const rwObjectStore = db
          .transaction(store.name, "readwrite")
          .objectStore(store.name);
        console.log(store.data);
        for (item of store.data) {
          console.log(item);
          rwObjectStore.add(item);
        }
      }
    };

    const objectStore = db.createObjectStore("cart", { keyPath: "id", autoIncrement: true });
    objectStore.createIndex("id", "id", { unique: true });
  };
  request.onsuccess = (event) => {
    db = event.target.result;
  };
}