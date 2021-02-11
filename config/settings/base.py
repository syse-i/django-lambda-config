from src.django_class_settings import base


class Settings(base.Settings):
    BASE_DIR = base.BaseDir(__file__)

    @property
    def INSTALLED_APPS(self):
        return super().INSTALLED_APPS + [
            'django_extensions',
        ]
