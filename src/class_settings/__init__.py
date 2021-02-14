import sys

if sys.version_info[:2] >= (3, 8):
    # TODO: Import directly (no need for conditional) when `python_requires = >= 3.8`
    from importlib.metadata import PackageNotFoundError, version  # pragma: no cover
else:
    # noinspection PyUnresolvedReferences
    from importlib_metadata import PackageNotFoundError, version  # pragma: no cover

try:
    # Change here if project is renamed and does not equal the package name
    dist_name = __name__
    __version__ = version(dist_name)
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError


"""Class based settings for complex settings inheritance."""

import inspect
import sys


class Settings:
    """Class-based settings wrapper."""

    @classmethod
    def load(cls, module_name):
        """
        Export class variables and properties to module namespace.

        This will export and class variable that is all upper case and doesn't
        begin with ``_``. These members will be set as attributes on the module
        ``module_name``.
        """
        self = cls()
        module = sys.modules[module_name]
        for (member, value) in inspect.getmembers(self):
            if member.isupper() and not member.startswith('_'):
                if isinstance(value, property):
                    # noinspection PyArgumentList
                    value = value.fget(self)
                setattr(module, member, value)
