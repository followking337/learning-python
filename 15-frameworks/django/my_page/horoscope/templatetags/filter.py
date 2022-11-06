from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()  # при помощи этой переменной идет регистрация фильтров


@register.filter(name='split')  # if we don´t put name= the filter name will be the name of func
@stringfilter  # argument value in func will be guaranteed string type
def split(value, key=' '):
    return value.split(key)
