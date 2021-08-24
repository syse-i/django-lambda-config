"""
DOCSTRING
"""
import os
import inspect
from sys import modules as sys_modules
from itertools import chain
from pathlib import Path
from dataclasses import dataclass, fields, Field, field, MISSING
from typing import List, Callable, Union, Optional

__all__ = []


def set_path(base_dir, d):
    """
    DOCSTRING
    """
    return str(d if isinstance(d, Path) else Path(base_dir, d))


def parent_path(file_path, depth, n=0) -> Path:
    """
    DOCSTRING
    """
    return parent_path(file_path.parent, depth, n + 1) if n < depth else file_path.parent


def liststr_setter(value: Union[List[str], Callable[[List[str]], List[str]]], default: List[str]) -> List[str]:
    """
    DOCSTRING
    """
    if callable(value):
        return value(default)
    if isinstance(value, list):
        return list(chain(default, value))
    if value is None:
        return default
    return value


def basedir_setter(*args, depth=2, default=None) -> Path:
    """
    DOCSTRING
    """
    return parent_path(Path(*args).resolve(), depth=depth)


def template_dirs_setter(base_dir, dirs):
    """
    DOCSTRING
    """
    return list(map(set_path, (base_dir, dirs)))


def template_options_setter(value: dict, defaults: dict) -> dict:
    """
    DOCSTRING
    """
    options = defaults.copy()
    options.update(value)
    options['context_processors'] = list(chain(
        defaults.get('context_processors', []),
        value.get('context_processors', []),
    ))
    return defaults


# @dataclass
# class Template:
#     """
#     DOCSTRING
#     """
#     BACKEND: str
#     DIRS: List[str] = field(metadata={'setter': template_dirs_setter})
#     APP_DIRS: bool = True
#     OPTIONS: dict = field(default_factory=lambda: {
#         'context_processors': [
#             'django.template.context_processors.debug',
#             'django.template.context_processors.request',
#             'django.contrib.auth.context_processors.auth',
#             'django.contrib.messages.context_processors.messages',
#         ]
#     }, metadata={'setter': template_options_setter})
#
#     def set_dirs(self, base_dir):
#         # noinspection PyUnresolvedReferences
#         _field = self.__dataclass_fields__['DIRS']
#         dirs = getattr(self, 'DIRS')
#         func = _field.metadata['setter']  # <-- template_dirs_setter
#         setattr(self, 'DIRS', func(base_dir, dirs))
#
#     def set_options(self):
#         # noinspection PyUnresolvedReferences
#         _field = self.__dataclass_fields__['OPTIONS']
#         if _field.default is not MISSING:
#             defaults = _field.default
#         elif callable(_field.default_factory):
#             defaults = _field.default_factory()
#         else:
#             raise Exception('undefined OPTIONS')
#         value = getattr(self, 'OPTIONS')
#         func = _field.metadata['setter']
#         setattr(self, 'OPTIONS', func(value, defaults))
#
#     def __post_init__(self):
#         self.set_options()


# @dataclass
# class Database:
#     """
#     DOCSTRING
#     """
#     ENGINE: 'django.db.backends.postgresql',
#     NAME: 'mydatabase',
#     USER: 'mydatabaseuser',
#     PASSWORD: 'mypassword',
#     HOST: '127.0.0.1',
#     PORT: '5432',
#
#     def set_dirs(self, base_dir):
#         # noinspection PyUnresolvedReferences
#         _field = self.__dataclass_fields__['DIRS']
#         dirs = getattr(self, 'DIRS')
#         func = _field.metadata['setter']  # <-- template_dirs_setter
#         setattr(self, 'DIRS', func(base_dir, dirs))
#
#     def set_options(self):
#         # noinspection PyUnresolvedReferences
#         _field = self.__dataclass_fields__['OPTIONS']
#         if _field.default is not MISSING:
#             defaults = _field.default
#         elif callable(_field.default_factory):
#             defaults = _field.default_factory()
#         else:
#             raise Exception('undefined OPTIONS')
#         value = getattr(self, 'OPTIONS')
#         func = _field.metadata['setter']
#         setattr(self, 'OPTIONS', func(value, defaults))


@dataclass
class Settings:
    """
    Class based settings for complex settings inheritance.
    """

    # Build paths inside the project like this: os.path.join(BASE_DIR, ...)
    BASE_DIR: Path = field(metadata={'setter': basedir_setter})

    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY: str = os.environ.get('SECRET_KEY')

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG: bool = os.environ.get('DEBUG', True)

    ALLOWED_HOSTS: List[str] = field(default_factory=list, metadata={'setter': liststr_setter})

    INSTALLED_APPS: List[str] = field(default_factory=list, metadata={
        'setter': liststr_setter,
    })

    MIDDLEWARE: List[str] = field(default_factory=list, metadata={'setter': liststr_setter})

    ROOT_URLCONF: str = os.environ.get('ROOT_URLCONF', 'config.urls')

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

    # TEMPLATES: List[Template] = field(default_factory=lambda: [
    #     Template('django.template.backends.django.DjangoTemplates')
    # ])

    WSGI_APPLICATION: str = os.environ.get('WSGI_APPLICATION', 'config.wsgi.application')

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

    AUTH_PASSWORD_VALIDATORS: List[str] = field(default_factory=list, metadata={'setter': liststr_setter})

    # Authentication
    # https://docs.djangoproject.com/en/3.0/topics/auth/customizing/

    AUTHENTICATION_BACKENDS: List[str] = field(default_factory=list, metadata={'setter': liststr_setter})

    # Internationalization
    # https://docs.djangoproject.com/en/3.0/topics/i18n/

    LANGUAGE_CODE: str = os.environ.get('LANGUAGE_CODE', 'en-US')

    TIME_ZONE: str = os.environ.get('TIME_ZONE', 'UTC')

    USE_I18N: bool = True

    USE_L10N: bool = True

    USE_TZ: bool = True

    LOCALE_PATHS: List[Path] = field(default_factory=list)

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.0/howto/static-files/

    STATIC_URL: str = os.environ.get('STATIC_URL', '/static/')

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

    MEDIA_URL: str = os.environ.get('MEDIA_URL', '/media/')

    MEDIA_ROOT: str = ''

    # @property
    # def MEDIA_ROOT(self):
    #     return os.path.join(self.BASE_DIR, 'media/')

    class Meta:
        """
        DOCSTRING
        """

        # APPS definition
        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
        ]

        MIDDLEWARE = [
            'django.middleware.security.SecurityMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',
        ]

        AUTHENTICATION_BACKENDS = [
            'django.contrib.auth.backends.ModelBackend',
        ]

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

        ALLOWED_HOSTS = []

    ###########################################################################
    #                                                                         #
    ###########################################################################

    def __post_init__(self):
        for _field in fields(self):
            setter_func = _field.metadata.get('setter')
            if callable(setter_func):
                value = getattr(self, _field.name)
                setattr(self, _field.name, setter_func(value(getattr(self.Meta, _field.name))))

            # if _field.name == 'TEMPLATES':
            #     attr_val = getattr(self, 'TEMPLATES')
            #     for t in attr_val:
            #         t.set_dirs(self.BASE_DIR)

    ###########################################################################
    #                                                                         #
    ###########################################################################

    def load(self, module_name: str = "__main__") -> None:
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


# noinspection PyUnresolvedReferences
def main():
    x = Settings(
        __file__,
        INSTALLED_APPS=lambda x: list(chain(x, ['foo'])),
        # TEMPLATES=[
        #     Template(
        #         'django.template.backends.django.DjangoTemplates',
        #         DIRS=['templates/']
        #     )
        # ]
    )
    x.load()
    print(x)

    # @dataclass
    # class X:
    #     FOO: List = field(default_factory=lambda *args: list(chain([1, 2, 3], *args)))
    #
    #     def __post_init__(self):
    #         for _field in fields(self):
    #             current = getattr(self, _field.name, [])
    #             setattr(self, _field.name, _field.default_factory(current))
    #
    # x = X([4, 5, 6])
    # print(x.FOO)

    # print(x.TEMPLATES)
    # print(BASE_DIR)
    # t = Template(DIRS=['templates', Path('/Users/dsv/')])
    # t.set_dirs(x.BASE_DIR)
    # print(t.OPTIONS, t.DIRS)


if __name__ == "__main__":
    main()
    # x.load()
    # noinspection PyUnresolvedReferences
    # print(x, INSTALLED_APPS)
