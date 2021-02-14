from . import Settings as BaseSettings

__all__ = ['Settings']


class Settings(BaseSettings):
    DEBUG = True

    ALLOWED_HOSTS = ['*']

    INTERNAL_IPS = ['127.0.0.1']

    EMAIL_BACKEND = 'rtd_config.core.mail.backends.console.EmailBackend'

