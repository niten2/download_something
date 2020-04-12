import logging
from src.settings import LOG_PATH

logger = logging.getLogger("simple")

fileHandler = logging.FileHandler(LOG_PATH)
consoleHandler = logging.StreamHandler()

logger.addHandler(fileHandler)
logger.addHandler(consoleHandler)
