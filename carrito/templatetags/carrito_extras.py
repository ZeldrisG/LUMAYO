from django import template

register = template.Library()

@register.filter()
def cantidad_libros_format(cantidad=1):
    return '{} {}'.format(cantidad, 'libros' if cantidad > 1 else 'producto')


@register.filter()
def cantidad_add_format(cantidad=1):
    return '{} {}'.format(
        cantidad_libros_format(cantidad),
        'Agregados' if cantidad > 1 else 'agregado'
    )