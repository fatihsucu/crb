import sys
import os


sys.path.insert(
    0,
    os.path.join(os.path.abspath(os.path.dirname(__file__)) + '/../'))


import configs
conf = configs.get()

from app.libraries import loggerFactory
loggerFactory.setConfig(conf)

logger = loggerFactory.get()

logger.warning(" APACHE APP WILL START ")
from app.app import createApp
application = createApp(conf)

