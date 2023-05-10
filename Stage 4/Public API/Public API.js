async function getData() {
    const response = await fetch('https://jacqiec.pythonanywhere.com/api/getSales');
    const data = await response.json();
    return data.data;
  }
  
  async function main() {
    const data = await getData();
    console.log(data)
    const ordersDiv = document.getElementById("ordershow");
    for (type of data) {
      let column = document.createElement("div");
      let containerDiv = document.createElement("div");
      column.append(containerDiv);
      let nameP = document.createElement("p");
      // let totalContent = document.createTextNode("$" + type.total);
      let item_list = []
      for (item of type.items) {
        let price = item.price
        let flavors = item.flavors
        let pname = item.pname
        item_list += " "+price+" " + flavors +" "+ pname+","
      }
      // let email = document.createTextNode(type.email);
      containerDiv.append(nameP);
      // nameP.append(totalContent);
      nameP.append(item_list);
      // nameP.append(email)
  
  
      ordersDiv.append(column);
    }
  }
  
  main();
  