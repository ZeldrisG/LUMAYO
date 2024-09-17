const agregar = document.getElementById('add')
const remover = document.getElementById('remove')
const cantidad = document.getElementById('cantidad')

agregar.addEventListener('click', function() {
    cantidad.value = parseInt(cantidad.value) + 1;
})

remover.addEventListener('click', function() {
    valor = parseInt(cantidad.value);

    if(valor != 1){
        valor = valor -1;
    }

    cantidad.value = valor;
})

