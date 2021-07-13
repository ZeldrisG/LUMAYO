const agregarReserva = document.getElementById('addReserva')
const removerReserva = document.getElementById('removeReserva')
const cantidadReserva = document.getElementById('cantidadReserva')

agregarReserva.addEventListener('click', function() {
    cantidadReserva.value = parseInt(cantidadReserva.value) + 1;
})

removerReserva.addEventListener('click', function() {
    valor = parseInt(cantidadReserva.value);

    if(valor != 1){
        valor = valor -1;
    }

    cantidadReserva.value = valor;
})

