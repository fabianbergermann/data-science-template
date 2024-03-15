import pathlib
import time
from functools import wraps
from typing import Union

from project_utils.logger_config import logger


def get_project_root() -> pathlib.Path:
    root_path = pathlib.Path(__file__).absolute().parent.parent
    return root_path


def timeit(func):
    @wraps(func)
    def timed(*args, **kw):
        ts = time.time()
        result = func(*(args or []), **(kw or {}))
        te = time.time()
        logger.info(f"--- function {func.__name__} took {te - ts:.3} seconds ---")
        return result

    return timed


def mkdir_if_not_exits(path) -> Union[str, pathlib.Path]:
    """make parent directories of not existant yet and return the path"""
    p = pathlib.Path(path)
    if not p.suffix == "":
        p = p.parent
    p.mkdir(parents=True, exist_ok=True)
    return path
