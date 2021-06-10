var btnReservar = document.getElementById("btnReservar");

btnReservar.addEventListener("click", reservar, false);

function reservar(){
    
  idLibro = this.getAttribute('name');
  fetch('/reserva/reservar/', {
    method: "POST",
    body: idLibro,
    headers: {
      "X-CSRFToken": getCookie('csrftoken'),
      "X-Requested-With": "XMLHttpRequest",
    }
  }).then(
      function(response){
        console.log(response)
        return response.json()
      }
   ).then(
      function (data) {
        console.log(data)
        btnReservar.className += ' disabled';
        btnReservar.innerHTML = 'Reservado';
        btnReservar.removeEventListener('click', reservar);
      }
   )
}