from django import template

register = template.Library()

# retorna a class do bootstrap para colorir a mensagem de acordo com seu tipo
@register.filter(name='account_type')
def account_type(usuario):
    if usuario.is_superuser:
        return "Admin"
    else:
        return "Basic"