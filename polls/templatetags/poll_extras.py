from django import template
from jalali_date import date2jalali

register = template.Library()

@register.filter(name='jalali_date')
def jalali_date(value):
    return date2jalali(value)

