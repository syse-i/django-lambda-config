#!/usr/bin/env python
"""Since we are trying to distribute Django applications as Python Packages,
it is important that some commands (such `migrate`) are available from within
the installation of the package without the need of copying the source code.

Because of that ``pyscaffoldext-django`` moves the generated ``manage.py`` file
to become the package's ``__main__.py`` file. This way all the commands that
could be run before as ``python3 manage.py <COMMAND>`` can now be run as
``python3 -m lambda_config <COMMAND>``, in a straight forward fashion just after
a ``pip3 install``.

This file is a executable stub that simply calls ``__main__.py:main()`` for
the sake of backward compatibility of the developer's workflow.
"""
import os
import sys

from lambda_config import load_settings


@load_settings
def main():
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lambda_config.settings.local')

    # This makes the package usable even without being installed with pip
    # (redundant in the case the developer uses `python setup.py develop`)
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))

    main()

