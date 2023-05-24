let a = 5;
let b = 3;

for(let i= 1; i<101; i++){
    if((i%a===0) && (i%b===0) ){
        console.log("FizzBuzz");
    }
    else if(i%a===0){
        console.log("Buzz");
    }
    else if(i%b===0){
        console.log("Fizz");
    }
    else{
        console.log(i);
    }
}