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
  db.transaction(["orders"]).objectStore("orders").getAll().onsuccess =
    (event) => {
      const types = event.target.result;
      const productsDiv = document.getElementById("products");
      for (type of types) {
        let column = document.createElement("div");
        if (type.hasFlavors) {
          column.classList.add("w3-col", "l3", "s6", "goToFlavors");
          column.setAttribute("onclick", "goToFlavors('" + type.id + "');");
        } else {
          column.classList.add("w3-col", "l3", "s6", "goToCart");
          column.setAttribute("onclick", "addToCart('" + type.id + "');");
        }

        let containerDiv = document.createElement("div");
        containerDiv.classList.add("w3-container");
        column.append(containerDiv);

        let imgDiv = document.createElement("div");
        imgDiv.classList.add("w3-display-container");
        containerDiv.append(imgDiv);

        let img = document.createElement("img");
        img.id = type.id + "_img";
        img.width = "200";
        img.src = type.imgSrc;
        imgDiv.append(img);

        let nameP = document.createElement("p");
        let nameContent = document.createTextNode(type.name)
        let priceContent = document.createTextNode("$" + type.price);
        containerDiv.append(nameP);
        nameP.append(nameContent);
        priceB.append(priceContent);


        productsDiv.append(column);
      }
    };
}

// const btns_flavors = document.querySelectorAll(".goToFlavors div");
// for (let bt of btns_flavors) {
//   bt.addEventListener("click", addToCart(e));
// }

function goToFlavors(type) {
  console.log(type);
  window.location.href = "flavors.html?type=cones&id="+type;
}

function addToCart(type) {

  console.log(type);
}
