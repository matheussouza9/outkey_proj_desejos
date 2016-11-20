from django import template
from django.contrib import messages

register = template.Library()

# retorna a class do bootstrap para colorir a mensagem de acordo com seu tipo
@register.filter(name='message_type')
def message_type(msg):
    if msg.level == messages.ERROR:
        return "alert-danger"
    elif msg.level == messages.INFO:
        return "alert-info"
    elif msg.level == messages.SUCCESS:
        return "alert-success"
    elif msg.level == messages.WARNING:
        return "alert-warning"
    else:
        return ""