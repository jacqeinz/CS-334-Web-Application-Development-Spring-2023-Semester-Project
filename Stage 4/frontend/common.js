if ('serviceWorker' in navigator) {
 window.addEventListener('load', function(){
  navigator.serviceWorker.register('service-worker.js')
  .then(res => console.log("service worked registered"))
  .catch(err => console.log("service worker not registered", err))
 });

}
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