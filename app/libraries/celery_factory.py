from celery import Celery

DEFAULT_CONFIG = None
APP = None


def setCeleryConfig(config):
    global DEFAULT_CONFIG

    DEFAULT_CONFIG = config


def getCelery(config=None, force=False):

    global APP
    global DEFAULT_CONFIG

    if not force and APP:
        return APP

    if not config and not DEFAULT_CONFIG:
        raise Exception("Celery Needs a config object for getCelery operation")

    config = DEFAULT_CONFIG or config
    APP = Celery(config.CELERYNAME)
    APP.config_from_object(config)

    return APP
