setupDbConnection();

document.addEventListener("DOMContentLoaded", function () {
  let db;
  const request = indexedDB.open("RollingStoneIceCreamStage3");
  request.onerror = (event) => {
    console.error("Failed to open IndexedDb");
  };
  request.onsuccess = (event) => {
    db = event.target.result;
    setupTypes(db);
  };
});

function setupTypes(db) {
  db.transaction(["login"]).objectStore("login").getAll().onsuccess = (
    event
  ) => {
    print("Setup types.");
    const types = event.target.result;
    const loginForm = document.getElementById("loginForm");
    for (type of types) {
      const usernameInput = document.getElementById("username");
      const passwordInput = document.getElementById("password");
      print("Finish getting elements.");

      loginForm.addEventListener("submit", (event) => {
        event.preventDefault();
        const username = usernameInput.value.trim();
        const password = passwordInput.value.trim();

        fetch("defaultData.json")
          .then((response) => response.json())
          .then((users) => {
            const user = users.find(
              (u) => u.username === username && u.password === password
            );
            if (user) {
              alert(`Welcome, ${user.username}!`);
              window.location.href("management.html");
            } else {
              alert("Invalid username or password. Please try again.");
            }
          })
          .catch((error) => {
            console.error(error);
            alert(
              "An error occurred while trying to log in. Please try again later."
            );
          });
      });
    }
  };
}
