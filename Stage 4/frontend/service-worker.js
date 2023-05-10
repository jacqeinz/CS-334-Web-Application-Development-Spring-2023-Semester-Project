const staticIceCreamShop = "dev-ice-cream-site"
const assets = [
  "/",
  "index.html",
  "images/headertest.jpg",
  "images/headersec.jpg", 
  "images/test.jpg", 
  "images/icon2.png"

]

self.addEventListener("install", installEvent => {
  installEvent.waitUntil(
    caches.open(staticIceCreamShop).then(cache => {
      cache.addAll(assets)
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
