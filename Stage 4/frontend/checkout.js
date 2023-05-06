setupDbConnection();
let cart = [];

document.addEventListener("DOMContentLoaded", function () {
  Cart();
});
const send_button = document.createElementById("place_order");

function Cart() {
  if (sessionStorage.getItem("cart")) {
    //get cart data & parse to array
    cart = JSON.parse(sessionStorage.getItem("cart"));
    let totalTax = 0;
    let price = 0;
    let items = 0;
    let productName = "";
    let productFlavor = " ";
    let cartTable = "";
    //get no of items in cart
    items = cart.length;
    //loop over cart array
    for (let i = 0; i < items; i++) {
      //convert each JSON product in array back into object
      let x = JSON.parse(cart[i]);
      //get property value of price
      price = parseFloat(x.price);
      productName = x.pname;
      productFlavor = x.flavors;
      //add price to total
      cartTable +=
        "<tr><td>" +
        productName +
        ": " +
        productFlavor +
        "</td><td>$" +
        price.toFixed(2) +
        "</td></tr>";
      total += price;
      totalTax = total + total * 0.05;
      // document.getElementById("total").innerHTML = total.toFixed(2);
      document.getElementById("total").innerHTML = totalTax.toFixed(2);
      //insert saved products to cart table
      document.getElementById("carttable").innerHTML = cartTable;
      //update items in cart on website HTML
      document.getElementById("itemsquantity").innerHTML = items;
    }
  }
}

function onCheckout() {
  for (i in cart) {
    stringCart = JSON.stringify(cart);
    console.log("cart", stringCart);
  }
  let email = document.getElementById("email");
  let userEmail = email.value;
  console.log("userEmail", email);
  let total = sessionStorage.getItem("totalTax");
  console.log("total", total);

  fetch("/api/check_out_confirmation", {
    method: "POST",
    body: JSON.stringify({
      "total": total,
      "cart": cart,
      "userEmail": userEmail,
    }),
    headers: {
      "Content-type": "application/json; charset=UTF-8",
    },
  })
    .then((response) => response.json())
    .then((json) => console.log(json));
}
