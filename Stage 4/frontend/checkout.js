Cart();

function Cart(){
    //init
    var total = 0;
    var totalTax = 0;
    var price = 0;
    var items = 0;
    var productname = "";
    var productflavor = " ";
    var carttable = "";
    if(sessionStorage.getItem('cart')) {
        //get cart data & parse to array
        var cart = JSON.parse(sessionStorage.getItem('cart'));
        //get no of items in cart 
        items = cart.length;
        //loop over cart array
        for (var i = 0; i < items; i++){
            //convert each JSON product in array back into object
            var x = JSON.parse(cart[i]);
            //get property value of price
            price = parseFloat(x.price);
            productname = x.pname;
            productflavor = x.flavors;
            //add price to total
            carttable += "<tr><td>" + productname + ": "+ productflavor+ "</td><td>$" + price.toFixed(2) + "</td></tr>";
            total += price;
        totalTax = total + (total*.05);
        }
    }
    // document.getElementById("total").innerHTML = total.toFixed(2);
    document.getElementById("total").innerHTML = totalTax.toFixed(2);
    //insert saved products to cart table
    document.getElementById("carttable").innerHTML = carttable;
    //update items in cart on website HTML
    document.getElementById("itemsquantity").innerHTML = items;
}
setupDbConnection();

document.addEventListener("DOMContentLoaded", function () {
 

  const apiRequest = fetch("/api/checkout");
  apiRequest
    .then((response) => response.json())
    .then((data) => setupemail(data.data));
 
});
