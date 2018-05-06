# Django Profanity Filter

[![PyPI license](https://img.shields.io/pypi/l/Django.svg)](https://pypi.python.org/pypi/Django/) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

Django Profanity Filter is a simple Django app that introduces a range of template tags and filters and model validators that remove or censor inappropriate language. 

## Installation
1. Run `pip install NAME OF PACKAGE`
2. Add `'profanity',` to your `INSTALLED_APPS` in `settings.py`
3. Use `{% load profanity %}` in templates for tags and filters, and
`import profanity.validators` to import profanity validators.

## TODO
#### Misc
- [ ] Command line to load in your own list of words as a variable, and define validators and template filters with them
#### Template Tags

- [ ] Basic filter
- [ ] Advanced filter
    - Keyword argument for custom word filter
    
#### Validators
- [ ] Basic Censorship Validator
    
