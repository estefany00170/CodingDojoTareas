//Ejercicio 1 Imprimir impares 1-20
let num= 0;

for(let i=1; i<21; i++){
    if(i%2===1){
        console.log(i);
    }
}

//Ejercicio 2 Disminuir múltiplos de 3
let a = 3;

for(let i=100; i>=0; i--){
    if(i%a===0){
        console.log(i);
    }

}

//Ejercicio 3 Imprime la secuencia
let i = 5.5;
while (i>-3.5) {
    i=i-1.5
    console.log(i);
}
//Ejercicio 4 Sigma
let sum=0;
for(let i=1; i<101; i++){
    sum+=i;
        console.log(sum);
}

//Ejercicio 5 Factorial
let product= 1;
for(let i=1; i<13; i++){
    product*=i;
    console.log(product);

}