document.getElementById("flavors").innerHTML = writeInitialFlavors();
//FLAVOR ITEM: get initial content after EDIT button is clicked
function editFlavorItem(element){
    selectedElement = element.parentElement.parentElement.parentElement;
    console.log(selectedElement);
    Initname = selectedElement.childNodes[3];
    Initimage = selectedElement.childNodes[1].childNodes[1];
    showFlavorEditTab();
}
//REGULAR ITEM: get initial content after EDIT button is clicked
function editItem(element){
    selectedElement = element.parentElement.parentElement.parentElement;
    Initname='';Initimage='';Initprice='';Initdesc='';

    Initname = selectedElement.childNodes[3];
    Initprice = selectedElement.childNodes[3].childNodes[2];
    Initdesc = selectedElement.childNodes[5];
    console.log("initdesc", Initdesc);
    Initimage = selectedElement.childNodes[1].childNodes[1];
    showEditTab();
}

//FLAVOR TAB: shows the editing tab for flavors, populates it with information from the initial html
function showFlavorEditTab(){
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
    document.getElementById('edit_tab').style.display='block'
    tab = document.getElementById('edit_tab');
  
    tabimage = tab.childNodes[1].childNodes[1].childNodes[5];
    namefield = tab.childNodes[1].childNodes[1].childNodes[9];
    pricefield = tab.childNodes[1].childNodes[1].childNodes[11];
    descfield = tab.childNodes[1].childNodes[1].childNodes[13];
    
    tabimage.innerHTML = Initimage.outerHTML;
    namefield.innerHTML = `<input class = "w3-input w3-border" type="text" placeholder="` + Initname.innerHTML +`"` + ` value="` + Initname.innerHTML + `"id="editName"></input>`;
    console.log("descfield: ", descfield);
    pricefield.innerHTML = `<input class="w3-input w3-border" type="text" placeholder="`+ Initprice.innerHTML+`"` + ` value="` + Initprice.innerHTML + `"id="editPrice"></input>`;
    descfield.innerHTML = `<input class="w3-input w3-border" type="text" placeholder="`+ Initdesc.innerHTML+`"` + ` value="` + Initdesc.innerHTML + `"id="editDesc"></input>`;
}

//Function runs on Save Item being clicked
//updates the initial name and image for flavor items
function updateFlavorItem(){
    Initname.innerHTML = document.getElementById("editName").value;
    Initimage.outerHTML = tabimage.innerHTML;
    document.getElementById('edit_tab').style.display='none';
}
  
//EDIT TAB: If the user selects a new image, update the edit tab to show it
function changeImage(){
    filename = editImg.files[0].name;
    console.log(filename);
    tabimage.innerHTML = '<img src="images/' + filename + '" style="width:100%">';
    console.log("image changed"); 
}
//NEW ITEM TAB: function to upload an image for new item creation
function uploadImage(){
    filename = uploadImg.files[0].name;
    console.log(filename);
    imageSlot = document.getElementById("newImage").parentElement;
    imageSlot.innerHTML = '<img src="images/' + filename + '" id="newImage" style="width:100%">';
}
  
//Completely gets rid of selected element when DELETE button is clicked.
function deleteItem(){
    if (confirm("Are you sure you want to delete this item?") == true) {
      console.log("Item deletion");
      selectedElement.innerHTML = ' ';
      selectedElement.outerHTML = ' ';
      document.getElementById('edit_tab').style.display='none';
    } else {
      console.log("Item not deleted");
    }
}

//creates a new item in any category
function createNewItem(){
    itemname = document.getElementById("nameEdit").value;
    itemprice = document.getElementById("priceEdit").value;
    itemdesc = document.getElementById("descEdit").value;
    itemimg = imageSlot.innerHTML;
    itemcategory = document.getElementById("category").value;
    section = document.getElementById(itemcategory);
    console.log(itemcategory);
    console.log(section);

    if (itemcategory != "flavors"){
        buttonhtml = `<button class="w3-button w3-black" onclick="editItem(this)">Edit</button>`;
        section.innerHTML += `<div class="w3-col l3 s6">
                            <div class="w3-container">
                            <div class="w3-display-container">` + itemimg + `
                                <div class="w3-display-middle w3-display-hover">`
                                + buttonhtml + 
                                `</div>
                            </div>`+ itemname + `</div>
                        </div>`
    }else{
        buttonhtml = `<button class="w3-button w3-black" onclick="editFlavorItem(this)">Edit</button>`;
        section.innerHTML += `<div class="w3-col l3 s6">
                            <div class="w3-container">
                            <div class="w3-display-container">` + itemimg + `
                                <div class="w3-display-middle w3-display-hover">`
                                + buttonhtml + 
                                `</div>
                            </div>`
                            +  itemname +
                            `</div>
                        </div>`
    }
    
    
    
}







//Function to load in initial flavor content: Unfinished // should read fromo JSON
function writeInitialFlavors(){
    let myFlavors = ` <div class="w3-col l3 s6">
        <div class="w3-container">
          <div class="w3-display-container">
            <img src="images/tiramisu.JPG" style="width:100%">
            <div class="w3-display-middle w3-display-hover">
              <button class="w3-button w3-black" onclick="editFlavorItem(this)">Edit</button>
            </div>
          </div>
          <p>Tiramisu</p>
        </div>
        <div class="w3-container">
          <div class="w3-display-container">
            <img src="images/cookiedough.JPG"style="width:100%" >
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
            <img src="images/chocolatechip.JPG"style="width:100%" >
            <div class="w3-display-middle w3-display-hover">
              <button class="w3-button w3-black" onclick="editFlavorItem(this)">Edit</button>
            </div>
          </div>
          <p>Chocolate Chip</p>
        </div>
        <div class="w3-container">
          <div class="w3-display-container">
            <img src="images/espresso.JPG"style="width:100%" >
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
            <img src="images/vanillabean.JPG"style="width:100%" >
            <div class="w3-display-middle w3-display-hover">
              <button class="w3-button w3-black" onclick="editFlavorItem(this)">Edit</button>
            </div>
          </div>
          <p>Vanilla Bean</p>
        </div>
        <div class="w3-container">
          <div class="w3-display-container">
            <img src="images/chocolatefudge.JPG"style="width:100%" >
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
            <img src="images/strawberry.JPG"style="width:100%" >
            <div class="w3-display-middle w3-display-hover">
              <button class="w3-button w3-black" onclick="editFlavorItem(this)">Edit</button>
            </div>
          </div>
          <p>Strawberry</p>
        </div>
        <div class="w3-container">
          <div class="w3-display-container">
            <img src="images/pecanpraline.JPG"style="width:100%" >
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
            <img src="images/raspberrycheescake.JPG"style="width:100%" >
            <div class="w3-display-middle w3-display-hover">
              <button class="w3-button w3-black" onclick="editFlavorItem(this)">Edit</button>
            </div>
          </div>
          <p>Raspberry Cheesecake</p>
        </div>`
    return myFlavors;
}
