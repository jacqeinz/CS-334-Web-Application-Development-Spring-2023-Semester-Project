setupDbConnection();

document.addEventListener("DOMContentLoaded", function () {

    const apiRequest = fetch("https://jacqiec.pythonanywhere.com/api/managerPortalLogin");
    apiRequest
        .then((response) => response.json())
        .then((data) => setupTypes(data.data));


    // let confirmation = confirm("Do you wish to add this to the cart?");

    // window.location.href = "SimpleSundaeFlavors.html";
});

function setupTypes(data) {
    console.log(data)
    const userDiv = document.getElementById("usershow");
    for (type of data) {
        let column = document.createElement("div");
        let containerDiv = document.createElement("div");
        column.append(containerDiv);
        let nameP = document.createElement("p");


        let ename = document.createTextNode(type.ename);
        let employeeID = document.createTextNode(type.empID);
        let password = document.createTextNode(type.password);
        containerDiv.append(nameP);
        nameP.append(ename);
        nameP.append(employeeID);
        nameP.append(password);


        userDiv.append(column);
    }
};


function deleteUser() {
    let inputid = document.getElementById("empID");
    let id = inputid.value;
    fetch("/api/deleteUsers/" + id, {
        method: "DELETE"
    })
        .then((response) => response.text())
        .then((text) => {
            console.log(text);
            window.location.href = "userManagement.html";
        });
}

function addUser() {
    let inputid = document.getElementById("newEmpID");
    let id = inputid.value;
    let inputEname = document.getElementById("ename");
    let ename = inputEname.value;
    let inputPassword = document.getElementById("password");
    let password = inputPassword.value;

    fetch("/api/addNewUser/", {
        method: "POST",
        body: JSON.stringify({
            ename: ename,
            userId: id,
            password: password
        }),
        headers: {
            "Content-type": "application/json; charset=UTF-8",
        }
    })
        .then((response) => response.text())
        .then((text) => {
            if(text == -1){
                alert("User with empID or ename already exists");
                return;
            }
            console.log(text);
            window.location.href = "userManagement.html";
        });
}

// const btns_flavors = document.querySelectorAll(".goToFlavors div");
// for (let bt of btns_flavors) {
//   bt.addEventListener("click", addToCart(e));
//}
