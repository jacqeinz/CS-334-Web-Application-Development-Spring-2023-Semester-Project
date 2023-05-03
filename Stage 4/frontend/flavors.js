setupDbConnection();

document.addEventListener("DOMContentLoaded", function () {
  const apiRequest = fetch("/api/getFlavors");
  apiRequest
    .then((response) => response.json())
    .then((data) => setupTypes(data.data));

  // let confirmation = confirm("Do you wish to add this to the cart?");

  // window.location.href = "SimpleSundaeFlavors.html";
});

function setupTypes(data) {
  console.log(data);
  const flavorsDiv = document.getElementById("flavors");
  for (type of data) {
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
    input.onclick = checkboxValidate;

    column.append(img);
    column.append(label);
    column.append(input);

    flavorsDiv.append(column);
  }
}

function checkboxValidate() {
  const checkedBoxes = document.querySelectorAll(
    'input[type="checkbox"]:checked'
  );
  if (checkedBoxes.length >= 3) {
    const uncheckedBoxes = document.querySelectorAll(
      'input[type="checkbox"]:not(:checked)'
    );
    for (box of uncheckedBoxes) {
      box.disabled = true;
    }
  } else {
    const disabledBoxes = document.querySelectorAll(
      'input[type="checkbox"]:disabled'
    );
    for (box of disabledBoxes) {
      box.disabled = false;
    }
  }
}

//get count of flavors, limit amount of flavors, pass to cart
function addToCart() {
  const queryString = new URLSearchParams(window.location.search);
  let type, name, price;

  if (!queryString.has("type") || !queryString.has("name")) {
    //YELL AT USER
    console.log("queryStringError");
    console.log(queryString.get("type"));
    console.log(queryString.get("id"));
    console.log(queryString.get("name"));
    console.log(queryString.get("price"));
    return;
  }
  type = queryString.get("type");
  id = queryString.get("id");
  price = queryString.get("price");
  name = queryString.get("name");

  const checkedFlavors = document.querySelectorAll(
    'input[type="checkbox"]:checked'
  );
  let flavorString = "";
  if (checkedFlavors < 1) {
    //Yell at user
    return;
  }
  for (i = 0; i < checkedFlavors.length; i++) {
    flavorString += checkedFlavors[i].id;
    if (i < checkedFlavors.length - 1) {
      flavorString += ",";
    }
  }

  window.location.href =
    "shoppingcart.html?type=" +
    type +
    "&price=" +
    price +
    "&name=" +
    name +
    "&flavors=" +
    flavorString;
}
