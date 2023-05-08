setupDbConnection();

document.addEventListener("DOMContentLoaded", function () {

  const apiRequest = fetch("http://jacqiec.pythonanywhere.com/api/getOrders");
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
      const productsDiv = document.getElementById("ordershow");
      for (type of types) {
        let column = document.createElement("div");
        let containerDiv = document.createElement("div");
        containerDiv.classList.add("w3-display-container w3-container");
        column.append(containerDiv);
        let nameP = document.createElement("p");
        
        
        let totalContent = document.createTextNode("$" + type.total);
      
        for (item of type.items){
          let price = type.price
          let flavors = type.flavors
          let pname = type.pname
          nameP.append(price)
          nameP.append(flavors)
          nameP.append(pname)
        }
        let email = document.createTextNode(type.email);
        containerDiv.append(nameP);
        nameP.append(nameContent);
        nameP.append(totalContent);
        nameP.append(items);
        nameP.append(email)


        productsDiv.append(column);
      }
    };
}
let inputid = document.getElementById("orderID");
let id = inputid.value;
function deleteOrder(){
  fetch("/api/deleteOrders/"+ id, {
    method: "DELETE",
   
})
  .then((response) => response.text())
  .then((text) => {
      console.log(text);
      window.location.href = "orders.html";
  });
}

// const btns_flavors = document.querySelectorAll(".goToFlavors div");
// for (let bt of btns_flavors) {
//   bt.addEventListener("click", addToCart(e));
//}
