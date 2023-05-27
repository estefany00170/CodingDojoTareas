function pizzaOven(tipoCorteza, tipoSalsa, quesos, extras){
    var pizza= {};
    pizza.tipoCorteza = tipoCorteza;
    pizza.tipoSalsa = tipoSalsa;
    pizza.quesos = quesos;
    pizza.extras = extras;
    return pizza;
}

var pz1 = pizzaOven("estilo chicago", "tradicional", "mozarella", ["pepperoni","salchicha"]);
console.log(pz1);

var pz2 = pizzaOven("lanzada a mano", "marinara",["mozzarella", "feta"], ["champiñones", "aceitunas", "cebolla"] )

var tipoCortezas = [
"Napolitana",
"Nueva York",
"Chicago Deep Dish",
"Siciliana",
"Sin gluten",
"Coliflor"
];

var tipoSalsas = [
"Salsa de tomate",
"Salsa blanca",
"Salsa cheddar",
"Salsa barbacoa",
"Salsa de albahaca",
"Salsa de ajo"
];

var quesos = [
"Mozzarella",
"Cheddar",
"Parmesano",
"Provolone",
"Gorgonzola",
"Feta"
]

var extras = [
"Pepperoni",
"Champiñones",
"Pimiento verde",
"Maiz",
"tocino",
"piña"
]

function randomRange(max, min) {
    return Math.floor(Math.random() * max - min) + min;
}

function randomPick(arr) {
    var i = Math.floor(arr.length * Math.random());
    return arr[i];
}

function randomPizza() {
    var pizza = {};
    pizza.tipoCortezas = randomPick(tipoCortezas);
    pizza.tipoSalsas = randomPick(tipoSalsas);
    pizza.quesos = [];
    pizza.extras = [];
    for(var i=0; i<randomRange(5, 1); i++) {
        pizza.quesos.push(randomPick(quesos));
    }
    for(var i=0; i<randomRange(4, 0); i++) {
        pizza.extras.push(randomPick(extras));
    }
    return pizza;
}

console.log(randomPizza());