// Tipos de Datos en JavaScript
/*
La sintaxis en lo que es comentarios
es muy similar a la de Java
realmente diriamente que es identica
*/

var nombre = "Lautaro"; // Type String
console.log(nombre);
nombre = 7;
console.log(nombre);

var numero = 3000; // Type Number
console.log(numero);

var objeto = { // Type Object
    nombre : "Lautaro",
    apellido : "Ponzina",
    telefono : "2994706477"
}

console.log(objeto);

// Tipo de dato boolean
var bandera = true;
console.log(bandera);

// Tipo de dato funcion
function miFuncion(){}
console.log(miFuncion);

// Tipo de dato symbol
var simbolo = Symbol("Mi simbolo");
console.log(simbolo);

// Tipo de dato clase
class Persona{
    constructor(nombre,apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}

console.log(Persona);