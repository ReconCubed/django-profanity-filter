from .extras import ProfanityFilter
from django.core.exceptions import ValidationError

pf = ProfanityFilter()


def validate_is_profane(value):
    if pf.is_profane(value) is True:
        raise ValidationError('Please remove any profanity/swear words.')
