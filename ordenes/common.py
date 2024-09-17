from enum import Enum

class OrdenEstado(Enum):
    CREADO = 'CREADO'
    PAGADO = 'PAGADO'
    COMPLETADO = 'COMPLETADO'
    CANCELADO = 'CANCELADO'

opciones = [ (tag, tag.value) for tag in OrdenEstado ]