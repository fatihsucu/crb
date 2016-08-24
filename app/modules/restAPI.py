# -*- coding: utf8 -*-
import requests
import json
import sys

from app.libraries import loggerFactory

reload(sys)
sys.setdefaultencoding("utf-8")


class RestAPI(object):
    """docstring for RestAPI"""
    def __init__(self, config):
        super(RestAPI, self).__init__()
        self.config = config
        self.logger = loggerFactory.get()
        self.facebook_answer_url = self.config.FB_SEND_URL(self.config.FB_PAGE_ACCESS_TOKEN)
        self.headers = {"content-type": "application/json"}
        self.facebook_answer_data = self.config.FACEBOOK_MESSAGGING_TEMPLATE
        self.text_data = self.config.TEXT_MESSAGE
        self.set_welcome_url = self.config.WELCOME_SCREEN_API
        self.user_profile_url = self.config.USER_PROFILE_API

    def send_text_facebook(self, recipient_id, answer):
        self.facebook_answer_data["recipient"]["id"] = recipient_id
        answer_data = self.text_data.copy()
        answer_data["text"] = answer
        self.facebook_answer_data["message"] = answer_data
        response = requests.post(
            self.facebook_answer_url, 
            data=json.dumps(self.facebook_answer_data),
            headers=self.headers)
        return response.json()

    def set_welcome(self):
        data = {
              "setting_type":"call_to_actions",
              "thread_state":"new_thread",
              "call_to_actions":[
                {
                   "payload": "Get Started"
                }
              ]
            }
        response = requests.post(
                self.set_welcome_url,
                data=json.dumps(data),
                headers=self.headers)
        return response.json()

    def remove_welcome_screen(self):
        data = {
            "setting_type": "call_to_actions",
            "thread_state": "new_thread"
        }
        response = requests.delete(
            self.set_welcome_url,
            data=json.dumps(data),
            headers=self.headers
        )
        return response.json()

    def getUser(self, user_id):
        url = self.user_profile_url(user_id, self.config.FB_PAGE_ACCESS_TOKEN)
        response = requests.get(url)
        return response.json()

    def prepareRecipes(self, recipes, viewMoreUrl):
        elems = []
        for r in recipes:
            try:
                elem = {}
                elem["title"] = r["name"]
                elem["buttons"] = [{
                    "type": "web_url",
                    "url": self.config.REPICE_PATH + r["url"] + "?&utm_source=rse&utm_medium=facebook%20bot&utm_campaign=recipe%20tool",
                    "title": "Show Recipe"
                },
                {
                    "type": "web_url",
                    "url": viewMoreUrl + "&utm_source=rse&utm_medium=facebook%20bot&utm_campaign=recipe%20tool",
                    "title": "View More"
                }
                ]
                elem["image_url"] = self.config.IMAGE_PATH + r["imageName"]
                elem["subtitle"] = r["description"]
                elems.append(elem)
            except:
                continue
        return elems

    def send_facebook(self, user_id, message_data):
        message_data["recipient"]["id"] = user_id
        r = requests.post(
            self.facebook_answer_url, data=json.dumps(message_data), headers=self.headers)
        return r.json()

    def getRecipes(self, params):
        if params.startswith("sort"):
            url = self.config.PURE_RECIPE_API_URL + params
        else:
            url = self.config.RECIPE_API_URL + params
        r = requests.get(url)
        self.logger.error(url)
        results = r.json()["results"]["recipes"]
        return results

    def prepareViewMoreUrl(self, params):
        url = self.config.VIEW_MORE_URL + "?" + params
        url = url.lstrip("&")
        self.logger.warning("View More Url {}".format(url))
        return url