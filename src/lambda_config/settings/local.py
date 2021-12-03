from typing import List

from attr import attrs, Factory

from ..core import Settings as BaseSettings

__all__ = ['settings']


@attrs(auto_attribs=True, order=True, slots=True)
class Settings(BaseSettings):
    INTERNAL_IPS: List[str] = Factory(lambda: ['127.0.0.1'])
    EMAIL_BACKEND: str = 'django.core.mail.backends.console.EmailBackend'


settings = Settings(
    DEBUG=True,
    ALLOWED_HOSTS=['*'],
)
