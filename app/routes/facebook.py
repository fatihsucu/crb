# coding=utf-8
from flask import Blueprint
from app.libraries.helpers import jsonizeRequest

from app.controllers import botManager
from app.modules.restAPI import RestAPI
from app.modules.users import Users


def getBlueprint(config):
    app = Blueprint('facebook_webhooks', __name__)

    @app.route('/message_received', methods=['POST'])
    @jsonizeRequest
    def message_received(data):
        '''
        Facebook webhook when message received
        All bot operations starts with this endpoint
        '''
        data = data["entry"][0]["messaging"][0]
        if "message" in data:
            if "quick_reply" in data["message"]:
                text = data["message"]["quick_reply"]["payload"]
            elif "text" in data["message"]:
                text = data["message"]["text"]
            else:
                text = "image_or_unknown_data"
            rec_id = data["sender"]["id"]
        else:
            text = data["postback"]["payload"]
            rec_id = data["sender"]["id"]
        bot, isNew = botManager.getBotOfUser(rec_id)
        bot.reply(text)
        # if answer["api"]:
        #     keyword = answer["text"]
        #     elem = restApiModule.getByKeyword(keyword)
        #     elements = restApiModule.prepareNews(elem)
        #     restApiModule.send_images_facebook(rec_id, elements[0:7])
        #     return "ok"
        # restApiModule.send_text_message(rec_id, answer["text"])
        return "Ok"

    @app.route('/message_received', methods=['GET'])
    @jsonizeRequest
    def getAccount(data):
        '''
        Facebook webhook confirmation
        '''
        return data.get("hub.challenge", "None")

    @app.route('/activeGetStartedButton', methods=['GET'])
    def activateButton():
        response = RestAPI(config).set_welcome()
        return "Get Started Button Activated"

    @app.route("/deactivateGetStartedButton", methods=["GET"])
    def deactivateButton():
        response = RestAPI(config).remove_welcome_screen()
        return "Get Started Button Deactivated"

    @app.route("/notify", methods=["GET"])
    def pushNotifications():
        userModule = Users(config)
        api = RestAPI(config)
        users = userModule.get_users_for_notification()
        for user in users:
            api.send_facebook(
                user, config.QUICK_REPLY_ANOTHER_RECIPE)
            userModule.updateUserLastNotification(user)
        return "Done"

    return app
