
var numlikes = document.querySelectorAll(".numero");


function likeaunme(index){
    for(let i=0; i<numlikes.length; i++){
        if(i=== index){
        var num = numlikes[i];
        let elementonumero = parseInt(num.textContent);
        let newValue = elementonumero + 1;
        num.textContent = newValue;
    }
}
}
