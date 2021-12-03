from pathlib import Path
from typing import Union


__all__ = ['str2path', 'path2string']


def str2path(val: Union[str, Path]) -> Path:
    if isinstance(val, Path):
        return val
    return Path(val)


def path2string(val: Union[str, Path]) -> str:
    if isinstance(val, str):
        return val
    return str(val)
