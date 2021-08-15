"""
DOCSTRING
"""

import inspect
from sys import modules as sys_modules
from pathlib import Path
from dataclasses import dataclass, field
from typing import List, Callable, Union, Optional

# noinspection PyPackageRequirements
from decouple import config

__all__ = ['Settings']

ListStr = List[str]
OptionalListAttr = Union[ListStr, Callable[[ListStr], ListStr], None]


def parse_liststr_attr(attr: OptionalListAttr, default: ListStr) -> ListStr:
    """
    DOCSTRING
    """
    if callable(attr):
        return attr(default)
    if isinstance(attr, list):
        return default + attr
    if attr is None:
        return default
    return attr


def parent_path(file_path, depth, n=0):
    """
    DOCSTRING
    """
    return parent_path(file_path.parent, depth, n + 1) if n < depth else file_path.parent


def base_dir_path(*args, depth=2):
    """
    DOCSTRING
    """
    return str(parent_path(Path(*args).resolve(), depth))


# APPS definition
__INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

__MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

__AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

__AUTH_PASSWORD_VALIDATORS = [
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

__ALLOWED_HOSTS = []

PARSE_DEFAULT_ATTRS = [
    ('INSTALLED_APPS', parse_liststr_attr, __INSTALLED_APPS),
    ('MIDDLEWARE', parse_liststr_attr, __MIDDLEWARE),
    ('AUTHENTICATION_BACKENDS', parse_liststr_attr, __AUTHENTICATION_BACKENDS),
    ('AUTH_PASSWORD_VALIDATORS', parse_liststr_attr, __AUTH_PASSWORD_VALIDATORS),
    ('ALLOWED_HOSTS', parse_liststr_attr, __ALLOWED_HOSTS),
]


# @dataclass
# class Template:
#     """
#     DOCSTRING
#     """
#     BACKEND: str = 'django.template.backends.django.DjangoTemplates'
#     DIRS: List[str] = field(default_factory=list)
#     APP_DIRS: bool = True
#     OPTIONS: Union[dict, Callable[[dict], dict], None] = None
#
#     @staticmethod
#     def get_default_options():
#         """
#         DOCSTRING
#         """
#         return {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ]
#         }
#
#     def __post_init__(self):
#         default_options = self.get_default_options()
#         if callable(self.OPTIONS):
#             options = self.OPTIONS(default_options)
#         elif isinstance(self.OPTIONS, dict):
#             options = default_options
#             options.update(self.OPTIONS)
#         else:
#             options = None
#         self.OPTIONS = default_options if options is None else options
#
#
# ListTemplate = List[Template]
# OptionalListTemplate = Union[ListTemplate, Callable[[ListTemplate], ListTemplate], None]


# ('CONTEXT_PROCESSORS', parse_liststr_attr, __CONTEXT_PROCESSORS),

# {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(self.BASE_DIR, 'db.sqlite3'),
#     }
# }

# @dataclass
# class DATABASE:
#     tag_name: str
#     ENGINE: str
#     NAME: Path
#
#     def __post_init__(self):
#         pass


@dataclass
class Settings:
    """
    Class based settings for complex settings inheritance.
    """

    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR: str

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY: str = config('SECRET_KEY')

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG: bool = config('DEBUG', default=True)

    ALLOWED_HOSTS: OptionalListAttr = None

    INSTALLED_APPS: OptionalListAttr = None

    MIDDLEWARE: OptionalListAttr = None

    ROOT_URLCONF: str = config('ROOT_URLCONF', default='config.urls')

    # noinspection PyPropertyAccess
    # @property
    # def TEMPLATES(self):
    #     return [{
    #         'BACKEND': 'django.template.backends.django.DjangoTemplates',
    #         'DIRS': self.TEMPLATES_DIRS,
    #         'APP_DIRS': True,
    #         'OPTIONS': {
    #             'context_processors': self.CONTEXT_PROCESSORS,
    #         },
    #     }]

    TEMPLATES: List[dict] = field(default_factory=lambda: [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        }
    ])

    WSGI_APPLICATION: str = config('WSGI_APPLICATION', default='config.wsgi.application')

    # Database
    # https://docs.djangoproject.com/en/3.0/ref/settings/#databases

    DATABASES: dict = field(default_factory=lambda: {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'db.sqlite3',
            # 'NAME': os.path.join(self.BASE_DIR, 'db.sqlite3'),
        }
    })

    # Password validation
    # https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

    AUTH_PASSWORD_VALIDATORS: OptionalListAttr = None

    # Authentication
    # https://docs.djangoproject.com/en/3.0/topics/auth/customizing/

    AUTHENTICATION_BACKENDS: OptionalListAttr = None

    # Internationalization
    # https://docs.djangoproject.com/en/3.0/topics/i18n/

    LANGUAGE_CODE: str = config('LANGUAGE_CODE', default='en-US')

    TIME_ZONE: str = config('TIME_ZONE', default='UTC')

    USE_I18N: bool = True

    USE_L10N: bool = True

    USE_TZ: bool = True

    LOCALE_PATHS: List[Path] = field(default_factory=list)

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.0/howto/static-files/

    STATIC_URL: str = config('STATIC_URL', default='/static/')

    STATIC_ROOT: str = ''

    # @property
    # def STATIC_ROOT(self):
    #     return os.path.join(self.BASE_DIR, 'static/')

    STATICFILES_DIRS: List[Path] = field(default_factory=list)

    # @property
    # def STATICFILES_DIRS(self):
    #     return self._STATICFILES_DIRS
    #
    # @STATICFILES_DIRS.setter
    # def STATICFILES_DIRS(self, values):
    #     self._STATICFILES_DIRS = values

    MEDIA_URL: str = config('MEDIA_URL', default='/media/')

    MEDIA_ROOT: str = ''

    # @property
    # def MEDIA_ROOT(self):
    #     return os.path.join(self.BASE_DIR, 'media/')

    ###########################################################################
    #                                                                         #
    ###########################################################################

    def __post_init__(self):
        for attr_name, parser, default in PARSE_DEFAULT_ATTRS:
            attr = getattr(self, attr_name)
            setattr(self, attr_name, parser(attr, default))

    ###########################################################################
    #                                                                         #
    ###########################################################################

    def load(self, module_name):
        """
        Export class variables and properties to module namespace.

        This will export and class variable that is all upper case and doesn't
        begin with ``_``. These members will be set as attributes on the module
        ``module_name``.
        """
        module = sys_modules[module_name]
        for (member, value) in inspect.getmembers(self):
            if member.isupper() and not member.startswith('_'):
                if isinstance(value, property):
                    # noinspection PyArgumentList
                    value = value.fget(self)
                setattr(module, member, value)


if __name__ == "__main__":
    x = Settings(__file__)
    x.load(__name__)
    # noinspection PyUnresolvedReferences
    print(x, INSTALLED_APPS)
