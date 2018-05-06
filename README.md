# Django Profanity Filter

[![PyPI license](https://img.shields.io/pypi/l/Django.svg)](https://pypi.python.org/pypi/Django/) [![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

Django Profanity Filter is a simple Django app that introduces a range of template tags and filters and model validators that remove or censor inappropriate language. 

## Installation
1. Install via pip
```
$ pip install NAME OF PACKAGE
```
2. Add `'profanity',` to your `INSTALLED_APPS` in `settings.py`
```python
INSTALLED_APPS = (
...
'profanity',
...
)
```

## Usage
#### Template Tags
At the top of every template you wish to use profanity filters and tags on, make sure to load the profanity tags.

```jinja2
...
{% load profanity %}
...
```
##### Censor Tag
###### Example
```jinja2
{% with string='You are a bitch!' %}
{{ string|censor }}
{% endwith %}
```
The output will be `You are a *****!`, instead of `You are a bitch!`.


#### Validators
##### Is Profane Validator
###### Example
```python
from profanity.validators import validate_is_profane

class Post(models.Model):
    post = models.TextArea(max_length=150, validators=[validate_is_profane])
```


## TODO
### Template Tags

- [x] Basic filter
- [ ] Advanced filter
    - Keyword argument for custom word filter
    
### Validators
- [x] Basic Censorship Validator
    
