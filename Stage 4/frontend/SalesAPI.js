async function getData() {
    const response = await fetch('https://jacqiec.pythonanywhere.com/api/getOrders');
    const data = await response.json();
    return data;
  }
  
  async function main() {
    const data = await getData();
    console.log(JSON.stringify(data))
  }
  
  main();
  