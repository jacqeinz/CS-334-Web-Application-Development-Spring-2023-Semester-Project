const staticDevIceCream = async (resources) => {
    const cache = await caches.open("v1");
    await cache.addAll(resources);
  };
  
  self.addEventListener("install", (event) => {
    event.waitUntil(
        staticDevIceCream([
    "/",
    "index.html",
    "index.js",
    "common.js",
    "defaultData.json",
    "carousel.css",
    "carousel.js",
    "images/LOGO.JPG",
    "images/login+person+profile+user+users+icon-1320166527284195604.png",
    "images/headertest.jpg",
    "images/headersec.jpg",
    "images/test.jpg",
    "https://www.w3schools.com/w3css/default.asp", 
    "https://www.w3schools.com/w3css/4/w3.css",
    "https://fonts.googleapis.com/css?family=Roboto", 
    "https://fonts.googleapis.com/css?family=Montserrat", 
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
        ])
    );
});
self.addEventListener("install", installEvent => {
    installEvent.waitUntil(
        caches.open(staticDevIceCream).then(cache => {
            cache.addAll(resources);
        })
    )
})

self.addEventListener("fetch", fetchEvent => {
    fetchEvent.respondWith(
        caches.match(fetchEvent.request).then(res => {
            return res || fetch(fetchEvent.request)
        })
    )
})