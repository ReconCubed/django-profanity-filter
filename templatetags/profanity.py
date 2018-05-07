from django import template
from profanity.extras import ProfanityFilter

register = template.Library()
pf = ProfanityFilter()


@register.filter()
def censor(value):
    return pf.censor(value)


@register.filter()
def is_profane(value):
    return pf.is_profane(value)
