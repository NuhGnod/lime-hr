from django import template
from django.utils import formats
import datetime

register = template.Library()


@register.filter
def convert_str_date(value):
    if value in (None, ''):
        return ''
    return str(datetime.strptime(value, '%Y-%m-%d').date())