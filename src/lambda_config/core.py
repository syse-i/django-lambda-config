import os
from pathlib import Path, PosixPath
from typing import List
from attr import attrs, attrib, Factory, validators

__all__ = ['Settings']


@attrs(auto_attribs=True, order=True, slots=True)
class Settings:
    """
    Lambda Core base settings, don't use this directly.
    """

    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR: Path = attrib(
        default=Path(os.environ.get('BASE_DIR', os.getcwd())),
        validator=validators.instance_of(PosixPath)
    )  # converter=path2string

    # Quick-start development settings - unsuitable for production
    SECRET_KEY: str = os.environ.get('SECRET_KEY')  # validators.instance_of(str)

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG: bool = os.environ.get('DEBUG', False)  # lambda v: strtobool(v) if isinstance(v, str) else bool(v)

    ALLOWED_HOSTS: List[str] = Factory(list)

    INSTALLED_APPS: List[str] = Factory(
        lambda: [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
        ]
    )

    MIDDLEWARE: List[str] = Factory(
        lambda: [
            'django.middleware.security.SecurityMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',
        ]
    )

    ROOT_URLCONF: str = os.environ.get('ROOT_URLCONF', 'config.urls')

    TEMPLATES: List[dict] = Factory(
        lambda self: [{
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [self.BASE_DIR / 'templates/'],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        }],
        takes_self=True
    )

    WSGI_APPLICATION: str = os.environ.get('WSGI_APPLICATION', 'config.wsgi.application')

    # Database
    # https://docs.djangoproject.com/en/3.2/ref/settings/#databases

    DATABASES: dict = Factory(
        lambda self: {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': self.BASE_DIR / 'db.sqlite3',
            }
        },
        takes_self=True
    )

    # Password validation
    # https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

    AUTH_PASSWORD_VALIDATORS: list = Factory(lambda: [
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
    ])

    # Authentication
    # https://docs.djangoproject.com/en/3.2/topics/auth/customizing/

    AUTHENTICATION_BACKENDS: List[str] = Factory(lambda: ['django.contrib.auth.backends.ModelBackend'])

    # Internationalization and localization
    # https://docs.djangoproject.com/en/3.2/topics/i18n/

    LANGUAGE_CODE: str = os.environ.get('LANGUAGE_CODE', 'en-US')

    TIME_ZONE: str = os.environ.get('TIME_ZONE', 'UTC')

    USE_I18N: bool = True

    USE_L10N: bool = True

    USE_TZ: bool = True

    LOCALE_PATHS: List[Path] = Factory(list)

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/3.2/howto/static-files/

    STATIC_URL: str = os.environ.get('STATIC_URL', '/static/')

    STATIC_ROOT: Path = Factory(
        lambda self: self.BASE_DIR / 'static/',
        takes_self=True
    )  # converter=path2string  # Requires: BASE_DIR

    STATICFILES_DIRS: List[Path] = attrib(factory=list)  # converter=path2string

    # Media files

    MEDIA_URL: str = attrib(default=os.environ.get('MEDIA_URL', '/media/'))

    MEDIA_ROOT: Path = Factory(
        lambda self: self.BASE_DIR / 'media/',
        takes_self=True
    )  # converter=path2string  # Requires: BASE_DIR


