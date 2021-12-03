from functools import wraps
from importlib import import_module
from os import environ
from typing import Callable


__all__ = ['load_settings']

from attr import asdict


def load_settings(func: Callable) -> Callable:
    """
    Export class variables and properties to module namespace.
    This will export and class variable that is all upper case and doesn't
    begin with ``_``. These members will be set as attributes on the module
    ``module_name``.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        settings_module = import_module(environ.get('DJANGO_SETTINGS_MODULE'))
        settings_instance = getattr(settings_module, 'settings')
        for key, value in asdict(settings_instance).items():
            # if key.isupper() and not key.startswith('_'):
            setattr(settings_module, key, value)
        return func(*args, **kwargs)
    return wrapper
