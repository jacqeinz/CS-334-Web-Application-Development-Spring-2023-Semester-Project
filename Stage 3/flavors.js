setupDbConnection();

document.addEventListener("DOMContentLoaded", function () {
  let db;
  const request = indexedDB.open("RollingStoneIceCreamStage3");
  request.onerror = (event) => {
    console.error("Failed to open IndexedDb");
  };
  request.onsuccess = (event) => {
    db = event.target.result;
    setupTypes(db);
  };

  // let confirmation = confirm("Do you wish to add this to the cart?");

  // window.location.href = "SimpleSundaeFlavors.html";
});

function setupTypes(db) {
  db.transaction(["flavors"]).objectStore("flavors").getAll().onsuccess = (
    event
  ) => {
    const types = event.target.result;
    const productsDiv = document.getElementById("flavors");
    for (type of types) {
      let column = document.createElement("div");
      column.classList.add("w3-col", "l3", "s6");

      let img = document.createElement("img");
      img.id = type.id + "_img";
      img.width = "200";
      img.src = type.imgSrc;

      let label = document.createElement("label");
      label.class = "w3-container";
      label.setAttribute("for", type.id);
      let nameContent = document.createTextNode(type.name);
      label.append(nameContent);
      let input = document.createElement("input");
      input.type = "checkbox";
      input.id = type.id;

      column.append(img);
      column.append(label);
      column.append(input);

      productsDiv.append(column);
    }
  };
}

//get count of flavors, limit amount of flavors, pass to cart

function goToFlavors(type) {
  console.log(type);
  window.location.href = "flavors.html?type=flavors&id=" + type;
}

function addToCart(type) {
  console.log(type);
}
