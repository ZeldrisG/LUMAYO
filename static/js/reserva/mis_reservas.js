var exampleModal = document.getElementById('exampleModal');
exampleModal.addEventListener('show.bs.modal', modal, false);

function modal(event){
  if (!event) // i.e. the argument is undefined or null
      event = window.event;
  // Button that triggered the modal
  var button = event.relatedTarget;
  // Extract info from data-bs-* attributes
  var id = button.getAttribute('data-bs-whatever');
  var titulo = button.getAttribute('name');
  var modalTitle = exampleModal.querySelector('.modal-title')
  modalTitle.textContent = 'Esta seguro de cancelar la reserva: ' + titulo;
  var btnEliminarModal = document.getElementById('btnEliminarModal');
  btnEliminarModal.addEventListener('click', eliminar.bind(this, id), false);
}

function eliminar(idLibro){
  fetch('/reserva/eliminar/', {
  method: "post",
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
      console.log(data);
      alert(data['estado']);
      location.reload();
    }
 )
}

