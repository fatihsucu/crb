import sys
import os


sys.path.insert(
    0,
    os.path.join(os.path.abspath(os.path.dirname(__file__)) + '/../'))


import configs
conf = configs.get()
from app.libraries import loggerFactory
from app.app import createApp
loggerFactory.setConfig(conf, defaultName='')
logger = loggerFactory.get()
logger.warning("======================")
logger.warning("======================")
logger.warning("======================")
logger.warning("Starting Facebook Bot ")
logger.warning("======================")
logger.warning("======================")
logger.warning("======================")
application = createApp(conf)

if __name__ == "__main__":
    application.run("localhost", port=80)
