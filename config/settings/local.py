from src.django_class_settings.base import local

from .base import Settings as BaseSettings


class Settings(BaseSettings, local.Settings):
    pass


Settings.load(__name__)
