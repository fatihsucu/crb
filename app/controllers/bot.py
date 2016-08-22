# -*- coding: utf8 -*-
import json

from app.modules import nlp
from app.modules import restAPI
from app.modules import users
from app.modules import reports
from app.libraries import mongodb
from app.libraries.helpers import stringFixer
from app.libraries import loggerFactory

import arrow
import pymongo


class Bot(object):
    """docstring for Bot"""

    def __init__(self, config, user_id):
        super(Bot, self).__init__()
        """Init icerisindeki cogu degisken test sirasinda isteyebilecekleri
        featureler sebebiyle birakildi."""
        self.config = config
        self.logger = loggerFactory.get()
        self.database = mongodb.getDb(self.config)
        self.storage = self.database["bots"]
        self.nlpModule = nlp
        self.lastActivity = None
        self.user_id = user_id
        self._type = None
        self.mainIngredient = None
        self.appetizerIng = None
        self.time = None
        self.region = None
        self.appetizerType = None
        self.params = "" # RWS API'a istek yapan parametreler
        self.readyseteatparams = "" # ReadySetEat'e gonderen  url'i hazilayan parametreler
        self.dessert = None
        self.breakfastIngredient = None
        self.breakfastTime = None
        self.sideDish = None
        self.username = None
        self.data = None
        self.index = 0
        self.lastMessage = None
        self.lastTopic = None
        self.sumTitle = None
        self.lastAnswerData = None # Bot'un son verdigi cevabin saklandigi yer
        self.reports = reports.Reports(self.config) # Botun anlasilmayanlar raporladigi modul
        self.api = restAPI.RestAPI(self.config) # Botun disariya istek yaptigi modul
        self.usersModule = users.Users(self.config)
        if self.isNew():
            self.logger.warning("new bot initialized")
            self.logger.warning("User info and welcome message will send")
            self.startSession()
            self.init_user()

    def startSession(self):
        """ Raporlayabilmek icin kac bot acildigini hesaplayabilmek icin
         her bot acildiginda veritababina kaydediyoruz. """
        self.storage.insert(self.__json__())

    def isNew(self):
        """BotManager'in instance indexlemesi nedeniyle servis yeniden basladiginda
        botun yeni acildigi ya da eski bir botun canlnadigi bilgisi icin bu metod yazildi"""
        bot = self.storage.find_one({"user": self.user_id})
        if not bot:
            return True
        return False

    def updateLastActiviy(self):
        self.lastActivity = arrow.utcnow()

    def close(self):
        permanent_bot = self.storage.find_one({
            "user_id": self.user_id})
        data = self.__json__()
        if "_id" in permanent_bot:
            data["_id"] = permanent_bot["_id"]
        self.storage.save(data)

    def __json__(self):
        return {
            "user": self.user_id
        }

    def reply(self, message):
        """Bot senaryolarinin uygulandigi ve kontrol edilebilecek yer. Butun islem reply metodu icerisinde
        gerceklesiyor."""
        self.logger.info("message came as {}".format(message))
        message = message.lower()
        if message in ["start over", "get started", "hello", "hi", "say hello"]:
            self.params = ""
            self.readyseteatparams = ""
            # self.api.send_text_facebook(
            #     self.user_id,
            #     'What type of recipe would you like to make? You can type "start over" at any time'
            # )
            # return self.api.send_facebook(self.user_id, self.config.QUESTION_MAIN)
            self.send_welcome_messages()
            return self.api.send_facebook(self.user_id, self.config.QUICK_REPLY_MAIN)
        if message in ["more", "show more"] and self.data:
            self.index += 5
            m_data = self.config.DEFAULT_TEMPLATE.copy()
            m_data["message"]["attachment"]["payload"]["elements"] = self.data[self.index:self.index + 3]
            return self.api.send_facebook(self.user_id, m_data)
        if message == "ask-tomorrow-payload":
            self.usersModule.makeNotificationDaily(self.user_id)
            return self.api.send_text_facebook(self.user_id, "This notification has been set up.")
        if message == "ask-week-payload":
            self.usersModule.makeNotificationWeekly(self.user_id)
            return self.api.send_text_facebook(self.user_id, "This notification has been set up.")
        if message == "activate notifications":
            self.usersModule.makeNotificationDaily(self.user_id)
            return self.api.send_text_facebook(self.user_id, "Notification has been activated.")
        if message in ["do-nothing", "payload_unsubscribe"]:
            if message == "payload_unsubscribe":
                self.usersModule.deactivateNotification(self.user_id)
                return self.api.send_text_facebook(
                    self.user_id,
                    'Notification has been deactivated. You can type "start over" anytime.')
            else:
                return self.api.send_text_facebook(
                    self.user_id,
                    'You can type "start over" when you are looking for new recipes.')

        try:
            title, choice = message.split("_")
        except:
            title = None
            choice = message

        if title == "category":
            self.params = ""
            self._type = choice
            if choice == "dinner":
                self.params += "&category=89"
                self.readyseteatparams += "&category=89"
                # self.api.send_text_facebook(self.user_id, "Select a main ingredient:")
                # return self.api.send_facebook(self.user_id, self.config.DINNER_INGREDIENTS)
                return self.api.send_facebook(self.user_id, self.config.DINNER_GUICK_REPLY)
            elif choice == "dessert":
                self.params += "&category=88"
                self.readyseteatparams += "&category=88"
                # self.api.send_text_facebook(self.user_id, "What kind of dessert would you like to make?")
                # return self.api.send_facebook(self.user_id, self.config.DESSERTS)
                return self.api.send_facebook(self.user_id, self.config.DESSERTS_QUICK_REPLY)
            elif choice == "breakfast":
                self.params += "&category=87"
                self.readyseteatparams += "&category=87"
                # self.api.send_text_facebook(self.user_id, "What kind of breakfast do you want?")
                # return self.api.send_facebook(self.user_id, self.config.BREAKFAST_QUESTION)
                return self.api.send_facebook(self.user_id, self.config.BREAKFAST_QUICK_REPLY)
            elif choice == "appetizer":
                self.params += "&category=85"
                self.readyseteatparams += "&category=85"
                # self.api.send_text_facebook(self.user_id, "What kind of appetizer or snack sounds good?")
                # return self.api.send_facebook(self.user_id, self.config.APPETIZER_QUESTION)
                return self.api.send_facebook(self.user_id, self.config.APPETIZER_QUICK_REPLY)
            elif choice == "side dish":
                self.params += "&category=95"
                self.readyseteatparams += "&category=95"
                # self.api.send_text_facebook(self.user_id, "Select a main ingredient")
                # return self.api.send_facebook(self.user_id, self.config.SIDE_DISH_QUESTION)
                return self.api.send_facebook(self.user_id, self.config.SIDE_DISH_QUICK_REPLY)
            else:
                return self.api.send_text_facebook(self.user_id,
                                                   "I don't know answer that belongs to {} yet".format(message))

        if title == "main-ingredient":
            self.mainIngredient = choice
            if choice == "chicken":
                self.params += "&mainingredient=76"
                self.readyseteatparams += "&mainingredient=76"
            elif choice == "beef":
                self.params += "&mainingredient=70"
                self.readyseteatparams += "&mainingredient=70"
            elif choice == "pork":
                self.params += "&mainingredient=249"
                self.readyseteatparams += "&mainingredient=249"
            elif choice == "seafood":
                self.params += "&mainingredient=73"
                self.readyseteatparams += "&mainingredient=73"
            elif choice == "pasta":
                self.params += "&mainingredient=272"
                self.readyseteatparams += "&mainingredient=272"
            elif choice == "vegetarian":
                self.params += "&lifestyle=299"
                self.readyseteatparams += "&lifestyle=299"
            return self.api.send_facebook(self.user_id, self.config.TIME_QUICK_REPLY)
        if title == "bre-time":
            self.breakfastTime = choice
            if choice == "15":
                self.params += "&totaltime=15"
                self.readyseteatparams += "&totaltime=15"
            elif choice == "30":
                self.params += "&totaltime=30"
                self.readyseteatparams += "&totaltime=30"
            elif choice == "45":
                pass
            recipes = self.api.getRecipes(self.params)
            if not recipes:
                return self.send_no_results()
            viewMoreUrl = self.api.prepareViewMoreUrl(self.readyseteatparams)
            elems = self.api.prepareRecipes(recipes, viewMoreUrl)
            self.data = elems
            m_data = self.config.DEFAULT_TEMPLATE.copy()
            m_data["message"]["attachment"]["payload"]["elements"] = self.data[self.index:self.index + 3]
            r = self.api.send_facebook(self.user_id, m_data)
            self.logger.warning(r)
            return
        if title == "time":
            self.time = choice
            self.params += "&totaltime={}".format(choice)
            self.readyseteatparams += "&totaltime={}".format(choice)
            # self.api.send_text_facebook(self.user_id, "What sounds Good?")
            # return self.api.send_facebook(self.user_id, self.config.REGION_DINNER_QUESTION)
            return self.api.send_facebook(self.user_id, self.config.REGION_QUICK_REPLY)

        if title == "region":
            self.region = choice
            if choice == "asian":
                self.params += "&cuisine=44"
                self.readyseteatparams += "&cuisine=44"
            elif choice == "italian":
                self.params += "&cuisine=46"
                self.readyseteatparams += "&cuisine=46"
            elif choice == "mediterranean":
                self.params += "&cuisine=367"
                self.readyseteatparams += "&cuisine=367"
            elif choice == "mexican":
                self.params += "&cuisine=45"
                self.readyseteatparams += "&cuisine=45"
            elif choice == "american":
                self.params += "&suppresstraits=44,35,355,46,367,45,356,261"

            recipes = self.api.getRecipes(self.params)
            if not recipes:
                return self.send_no_results()
            viewMoreUrl = self.api.prepareViewMoreUrl(self.readyseteatparams)
            elems = self.api.prepareRecipes(recipes, viewMoreUrl)
            self.data = elems
            m_data = self.config.DEFAULT_TEMPLATE.copy()
            m_data["message"]["attachment"]["payload"]["elements"] = self.data[self.index:self.index + 3]
            r = self.api.send_facebook(self.user_id, m_data)
            self.logger.warning(r)
            return

        if title == "dessert":
            self.dessert = choice
            if choice == "cookies":
                self.params += "&trait=48,10,20,110&suppresstraits=22,24&keywords=cookies"
                self.readyseteatparams += "&trait=48,10,20,110&keywords=cookies"
            elif choice == "cakes":
                self.params += "&suppresstraits=24&keywords=cake"
                self.readyseteatparams += "&keywords=cake"
            elif choice == "pies":
                self.params = "sortby=season,rating&order=desc,desc&negativeingredientkeyword=pieces&keywords=pie&suppresstraits=24&category=88"
                self.readyseteatparams = "&negativeingredientkeyword=pieces&keywords=pie&category=88"
            elif choice == "healthier":
                self.params += "&goodforyou=257&goodforyou=258&goodforyou=260"
                self.readyseteatparams += "&goodforyou=257&goodforyou=258&goodforyou=260"
            elif choice == "seasonal":
                self.params = "sortby=season,newest,rating,publisheddate&order=desc,desc,desc,desc&category=88&season=330"
                self.readyseteatparams = "&category=88&season=330"
            elif choice == "quick":
                self.params = "&totaltime=30"
                self.readyseteatparams = "&totaltime=30"

            recipes = self.api.getRecipes(self.params)
            if not recipes:
                return self.send_no_results()
            viewMoreUrl = self.api.prepareViewMoreUrl(self.readyseteatparams)
            elems = self.api.prepareRecipes(recipes, viewMoreUrl)
            self.data = elems
            m_data = self.config.DEFAULT_TEMPLATE.copy()
            m_data["message"]["attachment"]["payload"]["elements"] = self.data[self.index:self.index + 3]
            r = self.api.send_facebook(self.user_id, m_data)
            self.logger.warning(r)
            return

        if title == "breakfast":
            self.breakfastIngredient = choice
            if choice == "egg":
                self.params += "&mainingredient=72"
                self.readyseteatparams += "&mainingredient=72"
                self.params += "&trait=9"
                self.readyseteatparams += "&trait=9"
            elif choice == "casserole":
                self.params += "&keywords=casserole"
                self.readyseteatparams += "&keywords=casserole"
            elif choice == "healthier":
                self.params += "&goodforyou=260&goodforyou=258"
                self.readyseteatparams += "&goodforyou=260&goodforyou=258"
            elif choice == "sweet":
                self.params += "&trait=22"
                self.readyseteatparams += "&trait=22"
                # will add something sweet
                pass
            return self.api.send_facebook(self.user_id, self.config.BREAKFAST_TIME_QUICK_REPLY)

        if title == "appetizer":
            self.appetizerIng = choice
            if choice == "cheesy" or choice == "meaty":
                if choice == "cheesy":
                    self.params += "&keywords=cheese"
                    self.readyseteatparams += "&keywords=cheese"
                elif choice == "meaty":
                    self.params += "&mainingredient=70&mainingredient=76&mainingredient=249"
                    self.readyseteatparams += "&mainingredient=70&mainingredient=76&mainingredient=249"
                recipes = self.api.getRecipes(self.params)
                if not recipes:
                    return self.send_no_results()
                viewMoreUrl = self.api.prepareViewMoreUrl(self.readyseteatparams)
                elems = self.api.prepareRecipes(recipes, viewMoreUrl)
                self.data = elems
                m_data = self.config.DEFAULT_TEMPLATE.copy()
                m_data["message"]["attachment"]["payload"]["elements"] = self.data[self.index:self.index + 3]
                r = self.api.send_facebook(self.user_id, m_data)
                self.logger.warning(r)
                return
            elif choice == "veggies" or choice == "healthier":
                if choice == "veggies":
                    self.params += "&mainingredient=77&mainingredient=310"
                    self.readyseteatparams += "&mainingredient=77&mainingredient=310"
                elif choice == "heathier":
                    self.params += "&goodforyou=260"
                    self.readyseteatparams += "&goodforyou=260"
                return self.api.send_facebook(self.user_id, self.config.HOT_OR_COLD_QUICK_REPLY)

        if title == "hot-cold":
            self.appetizerType = choice
            if choice == "hot":
                self.params += "&suppresstraits=252"
            elif choice == "cold":
                self.params += "&cookingmethod=252"
                self.readyseteatparams += "&cookingmethod=252"

            recipes = self.api.getRecipes(self.params)
            if not recipes:
                return self.send_no_results()
            viewMoreUrl = self.api.prepareViewMoreUrl(self.readyseteatparams)
            elems = self.api.prepareRecipes(recipes, viewMoreUrl)
            self.data = elems
            m_data = self.config.DEFAULT_TEMPLATE.copy()
            m_data["message"]["attachment"]["payload"]["elements"] = self.data[self.index:self.index + 3]
            r = self.api.send_facebook(self.user_id, m_data)
            self.logger.warning(r)
            return

        if title == "side-dish":
            self.sideDish = choice
            if choice == "potato":
                self.params += "&mainingredient=298"
                self.readyseteatparams += "&mainingredient=298"
            elif choice == "vegetable":
                self.params += "&mainingredient=77"
                self.readyseteatparams += "&mainingredient=77"
            elif choice == "rice":
                self.params += "&mainingredient=272"
                self.readyseteatparams += "&mainingredient=272"
            elif choice == "pasta":
                self.params += "&mainingredient=75"
                self.readyseteatparams += "&mainingredient=75"
            elif choice == "salad":
                self.params = "sortby=season,newest,rating,publisheddate&order=desc,desc,desc,desc&category=95&mainingredient=77"
                self.readyseteatparams = "&category=95&mainingredient=77&trait=92"
            elif choice == "beans":
                self.params += "&mainingredient=310"
                self.readyseteatparams += "&mainingredient=310"

            recipes = self.api.getRecipes(self.params)
            if not recipes:
                return self.send_no_results()
            viewMoreUrl = self.api.prepareViewMoreUrl(self.readyseteatparams)
            elems = self.api.prepareRecipes(recipes, viewMoreUrl)
            self.data = elems
            m_data = self.config.DEFAULT_TEMPLATE.copy()
            m_data["message"]["attachment"]["payload"]["elements"] = self.data[self.index:self.index + 3]
            r = self.api.send_facebook(self.user_id, m_data)
            self.logger.warning(r)
            return
        isParamInMessage = self.fetch_parameters(message)
        if isParamInMessage:
            recipes = self.api.getRecipes(self.params)
            if not recipes:
                return self.send_no_results()
            viewMoreUrl = self.api.prepareViewMoreUrl(self.readyseteatparams)
            elems = self.api.prepareRecipes(recipes, viewMoreUrl)
            self.data = elems
            m_data = self.config.DEFAULT_TEMPLATE.copy()
            m_data["message"]["attachment"]["payload"]["elements"] = self.data[self.index:self.index + 3]
            r = self.api.send_facebook(self.user_id, m_data)
            self.logger.warning(r)
            return
        return self.api.send_text_facebook(self.user_id, "You can write ‘start over’ to go to the first step")

    def send_welcome_messages(self):
        r = self.api.send_text_facebook(self.user_id, "Welcome to ReadySetEat bot.")
        r2 = self.api.send_text_facebook(self.user_id, "You can type 'start over' anytime.")
        self.logger.warning("facebook response if {}".format(r))

    def send_no_results(self):
        self.api.send_text_facebook(
            self.user_id, "We’re sorry, there are no results, please select another option")

    def fetch_parameters(self, message):
        self.params = ""
        self.readyseteatparams = ""
        kwds = message.split()
        for kwd in kwds:
            self.params += "&keywords={}".format(kwd)
            self.readyseteatparams += "&keywords={}".format(kwd)
        return kwds

    def init_user(self):
        user_json = self.api.getUser(self.user_id)
        user_json["fb_id"] = self.user_id
        self.username = user_json.get("first_name", "")
        if not self.usersModule.get(self.user_id):
            self.usersModule.insert(user_json)
            self.usersModule.makeNotificationDaily(self.user_id)
