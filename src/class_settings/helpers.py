from pathlib import Path

# Django 3.8
# BASE_DIR = Path(__file__).resolve().parent.parent

__all__ = [
    'parent_path',
    'base_dir_path',
]


def parent_path(file_path, depth, n=0):
    return parent_path(file_path.parent, depth, n + 1) if n < depth else file_path.parent


def base_dir_path(*args, depth=2):
    return str(parent_path(Path(*args).resolve(), depth))
