// async function setUp()
// if 
const queryString = window.location.search;
// console.log(queryString)
const urlParams = new URLSearchParams(queryString)
const type = urlParams.get('type')
console.log(type);
const id = urlParams.get('id')
console.log(id);
const flavors = urlParams.get('flavors')
console.log(flavors)
const priceb = urlParams.get('price')
console.log(priceb)
// get the string following the ?
var query = window.location.search.substring(1)

// is there anything there ?
if(query.length) {
   // are the new history methods available ?
   if(window.history != undefined && window.history.pushState != undefined) {
        // if pushstate exists, add a new state to the history, this changes the url without reloading the page

        window.history.pushState({}, document.title, window.location.pathname);
   }
}

addToCart()
// /* get cart total from session on load */
updateCartTotal();
// /* button event listeners */
document.getElementById("emptycart").addEventListener("click", emptyCart);
/* ADD TO CART functions */
function addToCart() {
    //init
    // var sibs = [];
    var getprice;
    var getproductName;
    var cart = [];
    var stringCart;
    //create product object
    var product = {
        type : type,
        flavors :flavors,
        price : priceb
    };
    console.log(product)
    //convert product data to JSON for storage
    var stringProduct = JSON.stringify(product);
    /*send product data to session storage */
    
    if(!sessionStorage.getItem('cart')){
        //append product JSON object to cart array
        cart.push(stringProduct);
        //cart to JSON
        stringCart = JSON.stringify(cart);
        //create session storage cart item
        sessionStorage.setItem('cart', stringCart);
        addedToCart(type, flavors);
        
        updateCartTotal();
    }
    else {
        //get existing cart data from storage and convert back into array
       cart = JSON.parse(sessionStorage.getItem('cart'));
        //append new product JSON object
        cart.push(stringProduct);
        //cart back to JSON
        stringCart = JSON.stringify(cart);
        //overwrite cart data in sessionstorage 
        sessionStorage.setItem('cart', stringCart);
        addedToCart(type, flavors);
        updateCartTotal();
    }
}
/* Calculate Cart Total */
function updateCartTotal(){
    //init
    var total = 0;
    var price = 0;
    var items = 0;
    var productname = "";
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
            price = parseFloat(x.price.split('$')[1]);
            console.log(price)
            productname = x.type;
            //add price to total
            carttable += "<tr><td>" + type + ": "+ flavors+ "</td><td>$" + price.toFixed(2) + "</td></tr>";
            total += price;
        }
    }
    //update total on website HTML
    document.getElementById("total").innerHTML = total.toFixed(2);
    //insert saved products to cart table
    document.getElementById("carttable").innerHTML = carttable;
    //update items in cart on website HTML
    document.getElementById("itemsquantity").innerHTML = items;
    
}
//user feedback on successful add
function addedToCart(pname,pflavor) {
  var message = pname+": "+pflavor + " was added to the cart";
  var alerts = document.getElementById("alerts");
  alerts.innerHTML = message;
  if(!alerts.classList.contains("message")){
     alerts.classList.add("message");
     
  }
}
/* User Manually empty cart */
function emptyCart() {
    //remove cart session storage object & refresh cart totals
    if(sessionStorage.getItem('cart')){
        sessionStorage.removeItem('cart');
        updateCartTotal();
      //clear message and remove class style
      var alerts = document.getElementById("alerts");
      alerts.innerHTML = "";
      if(alerts.classList.contains("message")){
          alerts.classList.remove("message");
      }
    }
}