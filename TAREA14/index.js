//1. Siempre hambriento
function alwaysHungry(arr) {
    var hambriento = 0;
    for(var i=0; i<arr.length; i++){
        if(arr[i] === "comida"){
            console.log("delicioso");
            hambriento++;
        }
    }
    if(hambriento === 0){
        console.log("tengo hambre")
    }
}
alwaysHungry([3.14, "comida", "pastel", true, "comida"]);
// esto debería mostrar "delicioso, "delicioso"
alwaysHungry([4, 1, 5, 7, 2]);
// esto debería mostrar "Tengo hambre"

//2. Filtro paso alto .Dado un arreglo y un valor cutoff, devuelve un nuevo arreglo que contenga solo los valores mayores a cutoff.
function highPass(arr, cutoff) {
    var filteredArr = [];
    for(var i =0; i<arr.length; i++){
        if(arr[i]>cutoff){
            filteredArr.push(arr[i]);
        }
    }
    return filteredArr;
}
var result = highPass([6, 8, 3, 10, -2, 5, 9], 5);
console.log(result); // esperamos de vuelta [6, 8, 10, 9]

//3. Mejor que el promedio. Dado un arreglo de números, devuelve un recuento de cuántos de los números son mayores que el promedio.
function betterThanAverage(arr) {
    var sum = 0;
    for( var i=0; i<arr.length; i++){
        sum= sum+arr[i];
    }
    var avg= sum/ arr.length;
    var count = 0
    
    for(var i=0; i<arr.length; i++){
        if(arr[i] > avg){
            count++
        }
    }
    return count;
}
var result = betterThanAverage([6, 8, 3, 10, -2, 5, 9]);
console.log(result); 

//4. Arreglo invertido. Escribe una función que invierta los valores de un arreglo y los devuelva.
function reverse(arr) {
    var left = 0;
    var right = arr.length - 1;
    while(left < right) {
        var temp = arr[left];
        arr[left] = arr[right];
        arr[right] = temp;
        left++;
        right--;
    }
    return arr;
}
var result = reverse(["a", "b", "c", "d", "e"]);
console.log(result);

//5
function fibonacciArray(n) {
    var fibArr = [0, 1];
    for(let i = 2; i< n; i++){
        fibArr.push(fibArr[i -1] + fibArr[i-2]);
    }
    return fibArr;
}
var result = fibonacciArray(10);
console.log(result); // esperamos de vuelta[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

