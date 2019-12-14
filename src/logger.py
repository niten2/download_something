import logging
import os

from src.settings import LOG_PATH

logger = logging.getLogger("simple")

fileHandler = logging.FileHandler(LOG_PATH)
consoleHandler = logging.StreamHandler()

logger.addHandler(fileHandler)
logger.addHandler(consoleHandler)

# logging.basicConfig(
# 	filename=LOG_PATH,
# 	format='%(name)s - %(levelname)s - %(message)s'
# )

# import logging
# logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
# rootLogger = logging.getLogger()



# fileHandler.setFormatter(logFormatter)

# consoleHandler.setFormatter(logFormatter)

# rootLogger.addHandler(fileHandler)
# rootLogger.addHandler(consoleHandler)
