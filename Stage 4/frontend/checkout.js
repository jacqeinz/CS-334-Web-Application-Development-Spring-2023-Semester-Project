setupDbConnection();

document.addEventListener("DOMContentLoaded", function () {

 

  const apiRequest = fetch("/api/checkout");
  apiRequest
    .then((response) => response.json())
    .then((data) => setupemail(data.data));
 
});