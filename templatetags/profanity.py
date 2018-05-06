from django import template

register = template.Library()

@register.filter()
def noprofanity(value):
    return None
    # TODO
    # Read through value word by word,
    # replace any profanity with