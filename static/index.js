

// let modelo = document.getElementById("modelo").value;


async function allCars (){
    const URL = 'http://127.0.0.1:5000/contacts';
    return(
         fetch(URL, {
        method: "GET",
        // headers: { 'X-Api-Key': 'PklZm6jrIg8iWpS/S4ubfg==50uHGT4lWQnK92Lo'},
    })
    .then(response => {
        // console.log("response", response)
        return response.json();
    })
    .then(data => {
        return data.contacts;
        console.log("data", data)
    }) 
    .catch(error => console)
    )
}

async function test () {
    const selected = document.getElementById('carros').value;
    let carros = await allCars();
    let actual = (carros.filter(x => x.modelo == selected))[0];
    await fill_info(actual);
}

async function fill_info (car){
    console.log(car);
    let marca = document.getElementById("marca");
    let ano = document.getElementById("ano");
    let obs = document.getElementById("observacao");
    let diaria = document.getElementById("diaria");
    let status = document.getElementById("status");

    let title = document.getElementById("title");
    let img = document.getElementById("picture");
    const fix_title = (car.modelo).replaceAll(/\s/g,'').replaceAll("/", "").toLowerCase()
    console.log(fix_title);
    const SRC = `../static/imgs/picture_${fix_title}.jpg`
    

    marca.value = car.marca;
    ano.value = car.year;
    obs.value = car.obs;
    diaria.value = car.valor;
    status.value = car.status;

    title.innerText = (car.modelo).toUpperCase();
    img.src = SRC;
}


function ReplacingImage(){ 
 
    document.getElementById("x").src="image2.png" 
 
} 