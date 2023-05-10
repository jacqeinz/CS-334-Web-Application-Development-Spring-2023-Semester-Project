setupDbConnection();

document.addEventListener("DOMContentLoaded", function () {


});

function checkDbID() {

  let usernameInput = document.getElementById("username");
  let passwordInput = document.getElementById("password");


  let password = passwordInput.value.trim();
  let username = usernameInput.value.trim();


  fetch("/api/managementPortalLogin/" + id, {
    method: "POST",
    body: JSON.stringify({
      username: username,
      password: password
    }),
    headers: {
      "Content-type": "application/json; charset=UTF-8",
    }
  })

    .then((response) => response.text())
    .then((text) => {
      if (text == -1) {
        alert("Username or Password is incorrect, please try again!");
        return;
      }
      console.log(text);
      sessionStorage.setItem("userId", text);
      window.location.href = "management.html";
    });
};

