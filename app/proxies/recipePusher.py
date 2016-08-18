import configs


from app.libraries.celery_factory import getCelery
from app.libraries import loggerFactory

import requests

config = configs.get()
app = getCelery(config)
logger = loggerFactory.get()

@app.task
def push_notifications():
    """ Notifikasyonlar flask app'in kullanidigi instancelari kullanabilsin diye
    request araciligiyla gonderiliyor"""
    logger.warning("Notifications are sending.")
    requests.get(config.HOSTNAME + "/notify")
    return