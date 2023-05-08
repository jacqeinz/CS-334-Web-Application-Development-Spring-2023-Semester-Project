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
      const ordersDiv = document.getElementById("ordershow");
      for (type of types) {
        let column = document.createElement("div");
        let containerDiv = document.createElement("div");
        containerDiv.classList.add(" w3-container");
        column.append(containerDiv);
        let nameP = document.createElement("p");
        let totalContent = document.createTextNode("$" + type.total);
        let item_list = []
        for (item of type.items){
          let price = item.price
          let flavors = item.flavors
          let pname = item.pname
          item_list += price + flavors + pname
        }
        let email = document.createTextNode(type.email);
        containerDiv.append(nameP);
        nameP.append(totalContent);
        nameP.append(item_list);
        nameP.append(email)


        ordersDiv.append(column);
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
