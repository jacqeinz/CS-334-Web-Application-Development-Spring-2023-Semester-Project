setupDbConnection();

document.addEventListener("DOMContentLoaded", function () {

  const apiRequest = fetch("/api/getOrders");
  apiRequest
    .then((response) => response.json())
    .then((data) => setupTypes(data.data));
 

  // let confirmation = confirm("Do you wish to add this to the cart?");

  // window.location.href = "SimpleSundaeFlavors.html";
});

function setupTypes(db) {
  db.transaction(["Orders"]).objectStore("Orders").getAll().onsuccess =
    (event) => {
      const types = event.target.result;
      const productsDiv = document.getElementById("orders");
      for (type of types) {
        let column = document.createElement("div");
        

        let containerDiv = document.createElement("div");
        containerDiv.classList.add("w3-container");
        column.append(containerDiv);


        let nameP = document.createElement("p");
        let nameContent = document.createTextNode(type.pname)
        let priceContent = document.createTextNode("$" + type.price);
        let items = document.createTextNode(type.items);
        containerDiv.append(nameP);
        nameP.append(nameContent);
        priceB.append(priceContent);
        priceB.append(items);


        productsDiv.append(column);
      }
    };
}

// const btns_flavors = document.querySelectorAll(".goToFlavors div");
// for (let bt of btns_flavors) {
//   bt.addEventListener("click", addToCart(e));
// }
