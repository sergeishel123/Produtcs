from django import template

register = template.Library()
Dictionary = {'usd':'$',
              'rub':'RUB',}
@register.filter(name = 'currenty')
def name(value,currency = 'rub'):
    return f'{value} {Dictionary[currency]}'
