from django import template
from profanity.extras import ProfanityFilter

register = template.Library()
pf = ProfanityFilter()


@register.filter()
def censor(value):
    return pf.censor(value)
