from flask import Flask
from flask import render_template
import libraries.mongodb as mongodb
from libraries import celery_factory as celery


def createApp(config, url_prefix=None):
    app = Flask(__name__)

    mongodb.setDefaultConfig(config)

    from routes import facebook

    app.config.from_object(config)

    app.register_blueprint(
        facebook.getBlueprint(config), url_prefix=url_prefix)

    @app.route('/')
    def index():
        return "It is running"

    return app


def createCeleryApp(config):
    mongodb.setDefaultConfig(config)
    celery.setCeleryConfig(config)
    app = celery.getCelery()
    from proxies import recipePusher
    return app
