import os

from . import Settings as CoreSettings
from .helpers import base_dir_path

__all__ = [
    'Settings',
    'BaseDir',
]

BaseDir = base_dir_path


# noinspection PyPep8Naming
class Settings(CoreSettings):
    """
    Lambda Core base settings, don't use this directly.
    """

    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR = os.environ.get('BASE_DIR')

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    ALLOWED_HOSTS = []

    # Application definition

    _INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    ]

    @property
    def INSTALLED_APPS(self):
        return self._INSTALLED_APPS

    @INSTALLED_APPS.setter
    def INSTALLED_APPS(self, values):
        self._INSTALLED_APPS = values

    _MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

    @property
    def MIDDLEWARE(self):
        return self._MIDDLEWARE

    @MIDDLEWARE.setter
    def MIDDLEWARE(self, values):
        self._MIDDLEWARE = values

    ROOT_URLCONF = os.environ.get('ROOT_URLCONF', 'config.urls')

    _CONTEXT_PROCESSORS = [
        'django.template.context_processors.debug',
        'django.template.context_processors.request',
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
    ]

    @property
    def CONTEXT_PROCESSORS(self):
        return self._CONTEXT_PROCESSORS

    @CONTEXT_PROCESSORS.setter
    def CONTEXT_PROCESSORS(self, values):
        self._CONTEXT_PROCESSORS = values

    _TEMPLATES_DIRS = []

    @property
    def TEMPLATES_DIRS(self):
        return self._TEMPLATES_DIRS

    @TEMPLATES_DIRS.setter
    def TEMPLATES_DIRS(self, values):
        self._TEMPLATES_DIRS = values

    # noinspection PyPropertyAccess
    @property
    def TEMPLATES(self):
        return [{
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': self.TEMPLATES_DIRS,
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': self.CONTEXT_PROCESSORS,
            },
        }]

    WSGI_APPLICATION = os.environ.get('WSGI_APPLICATION', 'config.wsgi.application')

    # Database
    # https://docs.djangoproject.com/en/3.0/ref/settings/#databases

    @property
    def DATABASES(self):
        return {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(self.BASE_DIR, 'db.sqlite3'),
            }
        }

    # Password validation
    # https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]

    # Authentication
    # https://docs.djangoproject.com/en/3.0/topics/auth/customizing/

    _AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend']

    @property
    def AUTHENTICATION_BACKENDS(self):
        return self._AUTHENTICATION_BACKENDS

    @AUTHENTICATION_BACKENDS.setter
    def AUTHENTICATION_BACKENDS(self, values):
        self._AUTHENTICATION_BACKENDS = values

    # Internationalization
    # https://docs.djangoproject.com/en/3.0/topics/i18n/

    LANGUAGE_CODE = os.environ.get('LANGUAGE_CODE', 'en-US')

    TIME_ZONE = os.environ.get('TIME_ZONE', 'UTC')

    USE_I18N = True

    USE_L10N = True

    USE_TZ = True

    _LOCALE_PATHS = []

    @property
    def LOCALE_PATHS(self):
        return self._LOCALE_PATHS

    @LOCALE_PATHS.setter
    def LOCALE_PATHS(self, values):
        self._LOCALE_PATHS = values

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.0/howto/static-files/

    STATIC_URL = os.environ.get('STATIC_URL', '/static/')

    @property
    def STATIC_ROOT(self):
        return os.path.join(self.BASE_DIR, 'static/')

    _STATICFILES_DIRS = []

    @property
    def STATICFILES_DIRS(self):
        return self._STATICFILES_DIRS

    @STATICFILES_DIRS.setter
    def STATICFILES_DIRS(self, values):
        self._STATICFILES_DIRS = values

    MEDIA_URL = os.environ.get('MEDIA_URL', '/media/')

    @property
    def MEDIA_ROOT(self):
        return os.path.join(self.BASE_DIR, 'media/')

    def __init__(self, *args, **kwargs):
        if not self.BASE_DIR:
            raise Exception(f'{_("BASE_DIR must be defined...")}')