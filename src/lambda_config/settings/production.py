import os
from typing import Tuple, Optional

from attr import attrs, Factory

from ..core import Settings as BaseSettings

__all__ = ['settings', 'Settings']


@attrs(auto_attribs=True, order=True, slots=True)
class Settings(BaseSettings):
    # SSL Configuration
    # https://docs.djangoproject.com/en/3.0/topics/security/

    SECURE_SSL_REDIRECT: bool = True
    SECURE_HSTS_PRELOAD: bool = True
    SECURE_HSTS_SECONDS: int = 3600
    SECURE_HSTS_INCLUDE_SUBDOMAINS: bool = True
    SECURE_CONTENT_TYPE_NOSNIFF: bool = True
    SECURE_BROWSER_XSS_FILTER: bool = True
    SECURE_PROXY_SSL_HEADER: Optional[Tuple[str, str]] = Factory(lambda: ('HTTP_X_FORWARDED_PROTO', 'https'))

    SESSION_COOKIE_SECURE: bool = True

    CSRF_COOKIE_SECURE: bool = True

    X_FRAME_OPTIONS: str = 'DENY'

    DATABASES: dict = Factory(lambda: {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.environ.get('DB_NAME'),
            'USER': os.environ.get('DB_USER'),
            'PASSWORD': os.environ.get('DB_PASSWORD'),
            'HOST': os.environ.get('DB_HOST', 'localhost'),
            'PORT': os.environ.get('DB_PORT', 5432),
        }
    })


settings = Settings()
