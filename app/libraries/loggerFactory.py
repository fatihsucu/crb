import logging
from logging.config import dictConfig

DEFAULT_NAME = None


def setConfig(config, defaultName=None):
    global DEFAULT_NAME
    DEFAULT_NAME = defaultName
    dictConfig(config.LOGGING)


def get():
    return logging.getLogger(DEFAULT_NAME)


def getLogger(name=None):
    logger = logging.getLogger(name)
    return logger
