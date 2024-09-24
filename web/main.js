// alert("Hola mundos");

var nombre = "Addison Reyes";
var altura = 170;

var concatenacion = nombre + " " + altura;

// document.write(nombre);
// document.write(altura);
// document.write(concatenacion);


if (altura >= 190) {
    datos.innerHTML += "<h1>Eres una persona ALTA</h1>";
} else {
    datos.innerHTML += "<h1>Eres una persona BAJITA</h1>";
}

// for (var i = 2002; i <= 2024; i++) {
//     datos.innerHTML += `<h2>Estamoes en el año: ${i}</h2>`
// }

function MuestraMiNombre(nombre, altura) {
    return `
    <h1>Hola doy la caja de datos</h1>
    <h2>Mi nombre es: ${nombre}</h2>
    <h3>Mido: ${altura}</h3>
    `;
}

function imprimir() {
    datos = document.getElementById("datos");
    datos.innerHTML = MuestraMiNombre(nombre, altura);
}

imprimir();

var nombres = ['Victor', 'Antonio', 'Joaquin'];
// alert(nombres[0])

document.write('<h1>Listado de nombres</h1>');
// for (var i = 0; i < nombres.length; i++) {
//     document.write(nombres[i] + '<br/>');
// }

nombres.forEach(function (nombre) {
    document.write(nombre + '<br/>');
})