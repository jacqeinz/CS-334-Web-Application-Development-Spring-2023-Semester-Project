//Write initial flavor content
document.getElementById("flavors").innerHTML = writeInitialFlavors();
//define initial variable values
let editType = 'regular';
let newItems = [];

//FLAVOR ITEM: get initial content after EDIT button is clicked
function editFlavorItem(element){
    selectedElement = element.parentElement.parentElement.parentElement;
    Initname = selectedElement.childNodes[3];
    Initimage = selectedElement.childNodes[1].childNodes[1];
    showFlavorEditTab();
}
//REGULAR ITEM: get initial content after EDIT button is clicked
function editItem(element){
    selectedElement = element.parentElement.parentElement.parentElement;
    Initname='';Initimage='';Initprice='';Initdesc='';
    
    Initname = selectedElement.childNodes[3];
    actualName = Initname.innerHTML;
    actualName = actualName.split('<br>');
    actualName = actualName[0];

    Initprice = selectedElement.childNodes[3].childNodes[2];
    Initdesc = selectedElement.childNodes[5];
    Initimage = selectedElement.childNodes[1].childNodes[1];
    showEditTab();
}

//FLAVOR TAB: shows the editing tab for flavors, populates it with information from the initial html
function showFlavorEditTab(){
    editType='flavor';
    document.getElementById('edit_tab').style.display='block'
    tab = document.getElementById('edit_tab');
  
    tabimage = tab.childNodes[1].childNodes[1].childNodes[5];
    namefield = tab.childNodes[1].childNodes[1].childNodes[9];
    pricefield = tab.childNodes[1].childNodes[1].childNodes[11];
    descfield = tab.childNodes[1].childNodes[1].childNodes[13];
    
    tabimage.innerHTML = Initimage.outerHTML;
    namefield.innerHTML = `<input class = "w3-input w3-border" type="text" placeholder="` + Initname.innerHTML +`"` + ` value="` + Initname.innerHTML + `"id="editName"></input>`;
    pricefield.innerHTML = 'Additional fields are unavailable for flavor items'
    descfield.innerHTML = '';
}
//REGULAR TAB: shows the editing tab for regular items with descriptions and prices
function showEditTab(){
    editType='regular';
    document.getElementById('edit_tab').style.display='block'
    tab = document.getElementById('edit_tab');
  
    tabimage = tab.childNodes[1].childNodes[1].childNodes[5];
    namefield = tab.childNodes[1].childNodes[1].childNodes[9];
    pricefield = tab.childNodes[1].childNodes[1].childNodes[11];
    descfield = tab.childNodes[1].childNodes[1].childNodes[13];
    
    tabimage.innerHTML = Initimage.outerHTML;
    namefield.innerHTML = `<input class = "w3-input w3-border" type="text" placeholder="` + actualName +`"` + ` value="` + actualName + `"id="editName"></input>`;
    pricefield.innerHTML = `<input class="w3-input w3-border" type="text" placeholder="`+ Initprice.innerHTML+`"` + ` value="` + Initprice.innerHTML + `"id="editPrice"></input>`;
    descfield.innerHTML = `<input class="w3-input w3-border" type="text" placeholder="`+ Initdesc.innerHTML+`"` + ` value="` + Initdesc.innerHTML + `"id="editDesc"></input>`;
}

//Function runs on Save Item being clicked
//updates the initial name, image, price, and description for items
function updateItem(){
  if (editType = 'flavor'){
    Initname.innerHTML = document.getElementById("editName").value;
    Initimage.outerHTML = tabimage.innerHTML;
    /*write new information into json*/
    document.getElementById('edit_tab').style.display='none';
  }
  if (editType = 'regular'){
    newName = document.getElementById("editName").value;
    Initname.outerHTML = `<p>`+ newName + `<br><b>`+document.getElementById("editPrice").value+`</b>`+`</p>`;
    Initdesc.innerHTML = document.getElementById("editDesc").value;
    Initimage = tabimage.innerHTML;
    /*write new information into json*/
    document.getElementById('edit_tab').style.display='none';
  }
    
}
  
//EDIT TAB: If the user selects a new image, update the edit tab to show it
function changeImage(){
    filename = editImg.files[0].name;
    tabimage.innerHTML = '<img src="images/' + filename + '" style="width:100%">';
}

//NEW ITEM TAB: function to upload an image for new item creation
function uploadImage(){
    filename = uploadImg.files[0].name;
    imageSlot = document.getElementById("newImage").parentElement;
    imageSlot.innerHTML = '<img src="images/' + filename + '" id="newImage" style="width:100%">';
}
  
//Completely gets rid of selected element when DELETE button is clicked.
function deleteItem(){
    //ask user for confirmation to delete
    if (confirm("Are you sure you want to delete this item?") == true) {
      /*remove initial data from json*/
      selectedElement.innerHTML = ' ';
      selectedElement.outerHTML = ' ';
      document.getElementById('edit_tab').style.display='none';
    } 
}

//creates a new item in any category
function createNewItem(){
    itemname = document.getElementById("nameEdit").value;
    itemprice = document.getElementById("priceEdit").value;
    itemdesc = document.getElementById("descEdit").value;
    itemimg = '<img src="images/' + filename + '" style="width:100%">';
    itemcategory = document.getElementById("category").value;
    section = document.getElementById(itemcategory);
    newLItem = Object.create(newItem);

    if (itemcategory != "flavors"){
        buttonhtml = `<button class="w3-button w3-black" onclick="editItem(this)">Edit</button>`;
        //create attributes for new item object
        newLItem.name = itemname; 
        newLItem.price = itemprice; 
        newLItem.desc = itemdesc; 
        newLItem.image = itemimg;
        newLItem.button = buttonhtml;
        //push object to array of objects
        newItems.push(JSON.toString(newLItem));
        //update the management html code
        section.innerHTML += `<div class="w3-col l3 s6">
                            <div class="w3-container">
                            <div class="w3-display-container">` + itemimg + `
                                <div class="w3-display-middle w3-display-hover">`
                                + buttonhtml + 
                                `</div>
                            </div>
                            <p>`+ itemname + `<br><b>` + itemprice + `</b></p>
                            <figcaption>`
                            + itemdesc + `</figcaption>
                            </div>
                        </div>`
    }else{
        buttonhtml = `<button class="w3-button w3-black" onclick="editFlavorItem(this)">Edit</button>`;
        //create attributes for new item object
        newLItem.name = itemname; 
        newLItem.image = itemimg;
        newLItem.button = buttonhtml;
        //pushes object to array
        newItems.push(JSON.toString(newLItem));
        //update management html
        section.innerHTML += `<div class="w3-col l3 s6">
                            <div class="w3-container">
                            <div class="w3-display-container">` + itemimg + `
                                <div class="w3-display-middle w3-display-hover">`
                                + buttonhtml + 
                                `</div>
                            </div>
                            <p>`+ itemname + `</p>
                            </div>
                        </div>`
    };
    document.getElementById('newitem').style.display='none';
    
}

/*code to delete items within database*/

/*code to write new items into database*/

/*code to modify existing item within database*/


//object to store new items
const newItem = {
  name: " ",
  price: " ",
  desc: " ",
  image: " ", 
  button: " "
}

//Function to load in initial flavor content: Unfinished // should read from JSON
function writeInitialFlavors(){
    let myFlavors = ` <div class="w3-col l3 s6">
        <div class="w3-container">
          <div class="w3-display-container">
            <img src="/static/images/tiramisu.JPG" style="width:100%">
            <div class="w3-display-middle w3-display-hover">
              <button class="w3-button w3-black" onclick="editFlavorItem(this)">Edit</button>
            </div>
          </div>
          <p>Tiramisu</p>
        </div>
        <div class="w3-container">
          <div class="w3-display-container">
            <img src="/static/images/cookiedough.JPG"style="width:100%" >
            <div class="w3-display-middle w3-display-hover">
              <button class="w3-button w3-black" onclick="editFlavorItem(this)">Edit</button>
            </div>
          </div>
          <p>Cookie Dough</p>
        </div>
      </div>
      <div class="w3-col l3 s6">
        <div class="w3-container">
          <div class="w3-display-container">
            <img src="/static/images/chocolatechip.JPG"style="width:100%" >
            <div class="w3-display-middle w3-display-hover">
              <button class="w3-button w3-black" onclick="editFlavorItem(this)">Edit</button>
            </div>
          </div>
          <p>Chocolate Chip</p>
        </div>
        <div class="w3-container">
          <div class="w3-display-container">
            <img src="/static/images/espresso.JPG"style="width:100%" >
            <div class="w3-display-middle w3-display-hover">
              <button class="w3-button w3-black" onclick="editFlavorItem(this)">Edit</button>
            </div>
          </div>
          <p>Espresso</p>
        </div>
      </div>
      <div class="w3-col l3 s6">
        <div class="w3-container">
          <div class="w3-display-container">
            <img src="/static/images/vanillabean.JPG"style="width:100%" >
            <div class="w3-display-middle w3-display-hover">
              <button class="w3-button w3-black" onclick="editFlavorItem(this)">Edit</button>
            </div>
          </div>
          <p>Vanilla Bean</p>
        </div>
        <div class="w3-container">
          <div class="w3-display-container">
            <img src="/static/images/chocolatefudge.JPG"style="width:100%" >
            <div class="w3-display-middle w3-display-hover">
              <button class="w3-button w3-black" onclick="editFlavorItem(this)">Edit</button>
            </div>
          </div>
          <p>Chocolate Fudge</p>
        </div>
      </div>
      <div class="w3-col l3 s6">
        <div class="w3-container">
          <div class="w3-display-container">
            <img src="/static/images/strawberry.JPG"style="width:100%" >
            <div class="w3-display-middle w3-display-hover">
              <button class="w3-button w3-black" onclick="editFlavorItem(this)">Edit</button>
            </div>
          </div>
          <p>Strawberry</p>
        </div>
        <div class="w3-container">
          <div class="w3-display-container">
            <img src="/static/images/pecanpraline.JPG"style="width:100%" >
            <div class="w3-display-middle w3-display-hover">
              <button class="w3-button w3-black" onclick="editFlavorItem(this)">Edit</button>
            </div>
          </div>
          <p>Pecan Praline</p>
        </div>
      </div>
      <div class="w3-col l3 s6">
        <div class="w3-container">
          <div class="w3-display-container">
            <img src="/static/images/raspberrycheescake.JPG"style="width:100%" >
            <div class="w3-display-middle w3-display-hover">
              <button class="w3-button w3-black" onclick="editFlavorItem(this)">Edit</button>
            </div>
          </div>
          <p>Raspberry Cheesecake</p>
        </div>`
    return myFlavors;
}
