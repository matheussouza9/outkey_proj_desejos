from django import template

register = template.Library()

# retorna a class do bootstrap para colorir a mensagem de acordo com seu tipo
@register.filter(name='admin_meus_desejos')
def admin_meus_desejos(usuario, desejo):
    if usuario.is_superuser and desejo.dono == usuario:
        return "table-info"
    else:
        return ""