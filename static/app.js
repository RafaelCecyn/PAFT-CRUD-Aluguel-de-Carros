function createContact(){
    console.log("create");
    let modelo = document.getElementById("modelo").value;
    let marca = document.getElementById("marca").value;
    let year = document.getElementById("year").value;
    let obs = document.getElementById("obs").value;
    let valor = document.getElementById("valor").value;
    let status = document.getElementById("status").value;
    axios.post('http://127.0.0.1:5000/contacts',{modelo,marca,year,obs,valor,status})
    .then(response => {
        console.log(response);
        location.reload();
    })
    .catch(error => console.log(error));

}
function deleteContact(id){
    axios.delete(`http://127.0.0.1:5000/contacts/${id}`)
    .then(response =>{
        console.log(response);
        location.reload();
    }).catch(error => console.log(error));
}
function updateContact(id){
    const modelo = prompt("Insert the new model");
    const marca = prompt("Insert the new brand");
    const year = prompt("Insert the new year");
    const obs = prompt("Insert the new obs");
    const valor = prompt("Insert the new value");
    const status = prompt("Insert the new status");
    axios.put(`http://127.0.0.1:5000/contacts/${id}`, {modelo,marca,year,obs,valor,status})
    .then(response =>{
        console.log(response);
        location.reload();
    }).catch(error => console.log(error));
}
axios.get('http://127.0.0.1:5000/contacts')
.then(response => {
    
    let data = response.data;
    let tbody = document.getElementById("contacts-table-body");
    for(let contact of data.contacts){
        console.log(contact);
        let row = tbody.insertRow();
        let idCell = row.insertCell();
        idCell.innerHTML = contact.id;
        let modeloCell = row.insertCell();
        modeloCell.innerHTML = contact.modelo;
        let marcaCell = row.insertCell();
        marcaCell.innerHTML = contact.marca;
        let yearCell = row.insertCell();
        yearCell.innerHTML = contact.year;
        let obsCell = row.insertCell();
        obsCell.innerHTML = contact.obs;
        let valorCell = row.insertCell();
        valorCell.innerHTML = contact.valor;
        let statusCell = row.insertCell();
        statusCell.innerHTML = contact.status;
        let actionsCell = row.insertCell();
        actionsCell.innerHTML = `<button type="button" onclick="updateContact(${contact.id})">Update</button><button type="button" onclick="deleteContact(${contact.id})">Delete</button>`;
    }
})
.catch(error => console.log(error));




const url = `https://api.api-ninjas.com/v1/cars?limit=1&make=audi`  
fetch(url, {
    method: "GET",
    headers: { 'X-Api-Key': 'PklZm6jrIg8iWpS/S4ubfg==50uHGT4lWQnK92Lo'},
})
.then(response => {
    return response.json();
})
.then(data => {
    console.log(data[0].model)
    modelo.value = data[0].model
    marca.value = data[0].make
    year.value = data[0].year

}) 
.catch(error => console)


