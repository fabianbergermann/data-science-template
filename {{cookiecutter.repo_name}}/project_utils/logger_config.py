import pathlib

from loguru import logger

logging_path = pathlib.Path(__file__).absolute().parent
path = logging_path / "project_debug.log"
logger.add(path, rotation="1 week", retention="30 days", level="DEBUG")
