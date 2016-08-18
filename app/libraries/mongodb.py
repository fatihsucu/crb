from pymongo import MongoClient

DEFAULT_CONFIG = None

DATABASE = None


def setDefaultConfig(config):

    global DEFAULT_CONFIG
    DEFAULT_CONFIG = config


def getDb(config=None, force=False):

    global DATABASE
    global DEFAULT_CONFIG

    if not force and DATABASE:
        return DATABASE

    if not config and not DEFAULT_CONFIG:
        raise TypeError('while invoking getDb(), config is missing and \
            default config is not set')

    config = config or DEFAULT_CONFIG

    try:
        client = MongoClient(config.MONGODB_URI)
        DATABASE = client[config.MONGODB_DATABASENAME]
    except Exception as error:
        raise error

    return DATABASE
