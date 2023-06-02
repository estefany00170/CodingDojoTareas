

function nameEdit(){
    let nameUser = document.getElementById("name");
    nameUser.innerHTML ="Angi Doe";

}

function removeUser(element, action){
    let NumberRequests= document.querySelector("#ConnectionRequestNumber");
    let currentNumber = Number(NumberRequests.textContent );
    currentNumber --;
    NumberRequests.textContent = currentNumber;
    let user = element.closest(".card-list-item");
    let buttons = element.closest( ".buttons" );// Para Remover los botones de aceptar y cerrar
    buttons.remove();//Hasta aqui para remover los botones
    let userContent = user.innerHTML;
    user.remove();


if (action === "add"){
    let myConnections = document.querySelector("#myConnections");
    myConnections.innerHTML += `
    <li class="card-list-item start">
        ${userContent}
        </li>
    `;
    
    let totalConnections = document.querySelector("#totalConnections"); //aumentar el contador de Your Connections cuado se acepte un amigo
    currentNumber = Number(totalConnections.textContent);
    currentNumber ++;
    totalConnections.textContent = currentNumber;
    }
}