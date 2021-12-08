from functools import wraps
from typing import List

from attr import attrs, Factory

from ..core import Settings as BaseSettings

__all__ = ['settings']


# def settings_attrs(cls):
#     @wraps(cls)
#     def wrapper():
#         @attrs(auto_attribs=True, order=True, slots=True)
#         class Settings(cls):
#             pass
#         return Settings
#     return wrapper


@attrs(auto_attribs=True, order=True, slots=True)
class LocalSettings(BaseSettings):
    INTERNAL_IPS: List[str] = Factory(lambda: ['127.0.0.1'])
    EMAIL_BACKEND: str = 'django.core.mail.backends.console.EmailBackend'


settings = LocalSettings(
    DEBUG=True,
    ALLOWED_HOSTS=['*'],
)
