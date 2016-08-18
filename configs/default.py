# -*- coding: utf8 -*-
from datetime import timedelta


class Config(object):
    HOSTNAME = "https://fbmessenger.botego.net/conagra"
    MONGODB_URI = "localhost"
    MONGODB_DATABASENAME = "conagra_dev"
    FB_PAGE_ACCESS_TOKEN = "EAAY0T88gIjQBAKaYzE97ajqeMUy9eC1s11mtVLBVV2ZAjZBDXMukShpxdL89Dde5GsBcB7tjsd4pqtsS7LCkZAlKc37S1kbjsMMfZCP7krYu5EVXZCQmIEpy65DDhxr9xCT1rZC2685zfN3vZC6d7Av82kr43CWfsQZBtotCcTUjBQZDZD"
    FB_SEND_URL = "https://graph.facebook.com/v2.6/me/messages?access_token={}".format
    CELERYNAME = "conagra"
    TEXT_MESSAGE = {"text": "<MESSAGE>"}
    FACEBOOK_MESSAGGING_TEMPLATE = {"recipient": {"id": "<FACEBOOK_ID>"}, "message": {}}
    PAGE_ID = "812316508869493"
    WELCOME_SCREEN_API = "https://graph.facebook.com/v2.6/{}/thread_settings?access_token={}".format(PAGE_ID,
                                                                                                     FB_PAGE_ACCESS_TOKEN)
    USER_PROFILE_API = "https://graph.facebook.com/v2.6/{}?fields=first_name,last_name,profile_pic,locale,timezone,gender&access_token={}".format

    BROKER_URL = 'amqp://localhost/'
    CELERY_RESULT_BACKEND = "mongodb://localhost/"
    CELERY_MONGODB_BACKEND_SETTINGS = {
        'database': 'conagrafood',
        'taskmeta_collection': 'tasks',
    }
    CELERY_TIMEZONE = 'UTC'
    BROKER_TRANSPORT_OPTIONS = {
        'visibility_timeout': 196000,
        'fanout_patterns': True
    }

    CELERY_DEFAULT_QUEUE = 'conagra'
    CELERY_DEFAULT_ROUTING_KEY = 'conagra'
    CELERY_TASK_RESULT_EXPIRES = 60 * 36
    CELERY_DEFAULT_EXCHANGE = 'conagra'
    CELERYD_CONCURRENCY = 2
    CELERYD_PREFETCH_MULTIPLIER = 2
    CELERYD_TASK_SOFT_TIME_LIMIT = 60 * 4
    CELERYD_TASK_TIME_LIMIT = 60 * 5
    CELERYBEAT_SCHEDULE = {
        'daily_notifications': {
            'task': 'app.proxies.recipePusher.push_notifications',
            'schedule': timedelta(minutes=1),
            'args': []
        }

    }

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'verbose': {
                'format': '%(asctime)s - %(levelname)s - %(module)s: ' +
                          '%(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S'
            },
            'colored': {
                '()': 'colorlog.ColoredFormatter',
                'format': '%(log_color)s%(asctime)s - %(levelname)s' +
                          ' - %(module)s: %(message)s',
                'datefmt': '%Y-%m-%d %H:%M:%S'
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'handlers': {
            'null': {
                'class': 'logging.NullHandler',
            },
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'colored'
            },
            'file': {
                'class': 'logging.handlers.WatchedFileHandler',
                'filename': '/var/log/conagra/api.log',
                'formatter': 'colored',
                'encoding': 'utf-8',
                'delay': True
            },
        },
        'loggers': {
            '': {
                'handlers': ['file', 'console'],
                'propagate': True,
                'level': 'INFO'
            }
        }
    }

    # Conagra Questions
    # Fist Question
    QUESTION_MAIN = {
        "recipient": {
            "id": "<USER_ID>"
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": "Dinner",
                            "image_url": "http://www.personalitytutor.com/files/2012/04/Dinner-Table-Setting.jpg",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Dinner",
                                    "payload": "category_dinner"
                                }
                            ]
                        },
                        {
                            "title": "Dessert",
                            "image_url": "http://www.readyseteat.com/assets/images/collections/allcollections/dessert-collection-featured-1.jpg",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Dessert",
                                    "payload": "category_dessert"
                                }
                            ]
                        },
                        {
                            "title": "Breakfast/Brunch",
                            "image_url": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQIqHFLKGz9E_n_nAXaBk-Zwt13wRIINphg0ek9H-n_cSovcXDRoA",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Breakfast/Brunch",
                                    "payload": "category_breakfast"
                                }
                            ]
                        },
                        {
                            "title": "Appetizer/Snack",
                            "image_url": "http://www.sobeys.com/wp-content/uploads/2015/04/hero-sensations-compliments-shrimp-appetizers.jpg",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Appetizer/Snack",
                                    "payload": "category_appetizer"
                                }
                            ]
                        },
                        {
                            "title": "Side Dish",
                            "image_url": "http://img1.cookinglight.timeinc.net/sites/default/files/styles/500xvariable/public/image/2008/05/0805p122-beans_tatoes-x.jpg?itok=ZjA9MbML",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Side Dish",
                                    "payload": "category_side dish"
                                }
                            ]
                        }
                    ]
                }
            }
        }
    }

    DINNER_INGREDIENTS = {
        "recipient": {
            "id": "<USER_ID>"
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": "Chicken",
                            "image_url": "http://consumerrecipe.conagrafoods.com/uploadedImages/img_8032_8831.jpg",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Chicken",
                                    "payload": "main-ingredient_chicken"
                                }
                            ]
                        },
                        {
                            "title": "Beef",
                            "image_url": "http://consumerrecipe.conagrafoods.com/uploadedImages/img_8169_9249.jpg",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Beef",
                                    "payload": "main-ingredient_beef"
                                }
                            ]
                        },
                        {
                            "title": "Pork",
                            "image_url": "http://consumerrecipe.conagrafoods.com/uploadedImages/img_5529_2424.jpg",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Pork",
                                    "payload": "main-ingredient_pork"
                                }
                            ]
                        },
                        {
                            "title": "Seafood/Fish",
                            "image_url": "http://consumerrecipe.conagrafoods.com/uploadedImages/img_5579_2464.jpg",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Seafood/Fish",
                                    "payload": "main-ingredient_seafood"
                                }
                            ]
                        },
                        {
                            "title": "Pasta/Rice",
                            "image_url": "http://consumerrecipe.conagrafoods.com/uploadedImages/img_7400_7185.jpg",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Pasta/Rice",
                                    "payload": "main-ingredient_pasta"
                                }
                            ]
                        },
                        {
                            "title": "Vegetarian",
                            "image_url": "http://consumerrecipe.conagrafoods.com/uploadedImages/img_8118_9175.jpg",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Vegetarian",
                                    "payload": "main-ingredient_vegetarian"
                                }
                            ]
                        }
                    ]
                }
            }
        }
    }

    TIME_QUESTION = {
        "recipient": {
            "id": "<USER_ID>"
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "button",
                    "text": "How much time do you have?",
                    "buttons": [
                        {
                            "type": "postback",
                            "title": "30 Minutes",
                            "payload": "time_30"
                        },
                        {
                            "type": "postback",
                            "title": "45 Minutes",
                            "payload": "time_45"
                        },
                        {
                            "type": "postback",
                            "title": "60 Minutes",
                            "payload": "time_60"
                        }
                    ]
                }
            }
        }
    }

    REGION_DINNER_QUESTION = {
        "recipient": {
            "id": "USER_ID"
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": "Asian",
                            "image_url": "http://www.globalintercultural.org/images/sw3.jpg",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Asian",
                                    "payload": "region_asian"
                                }
                            ]
                        },
                        {
                            "title": "Italian",
                            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a3/Eq_it-na_pizza-margherita_sep2005_sml.jpg/800px-Eq_it-na_pizza-margherita_sep2005_sml.jpg",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Italian",
                                    "payload": "region_italian"
                                }
                            ]
                        },
                        {
                            "title": "Mediterranean",
                            "image_url": "http://cateringbymario.ca/wp-content/uploads/sites/7/2013/12/MEDITERRANEAN-FOOD-Catering-1024x681.jpg",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Mediterranean",
                                    "payload": "region_mediterranean"
                                }
                            ]
                        },
                        {
                            "title": "Mexican",
                            "image_url": "http://elchilango1.com/custom/3.jpg",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Mexican",
                                    "payload": "region_mexican"
                                }
                            ]
                        },
                        {
                            "title": "American",
                            "image_url": "http://ghk.h-cdn.co/assets/cm/15/11/54ffec52236b6-cheeseburger-lgn.jpg",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "American",
                                    "payload": "region_american"
                                }
                            ]
                        }
                    ]
                }
            }
        }
    }

    DESSERTS = {
        "recipient": {
            "id": "USER_ID"
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": "Cookies",
                            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Chocolate_Chip_Cookies_-_kimberlykv.jpg/220px-Chocolate_Chip_Cookies_-_kimberlykv.jpg",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Cookies",
                                    "payload": "dessert_cookies"
                                }
                            ]
                        },
                        {
                            "title": "Cakes",
                            "image_url": "http://www.cakedunia.com/wp-content/uploads/2015/12/cake2-500x368.jpg",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Cakes",
                                    "payload": "dessert_cakes"
                                }
                            ]
                        },
                        {
                            "title": "Pies",
                            "image_url": "http://www.voakespies.co.uk/wp/wp-content/uploads/2013/05/Voakes-Pies-2008-042-300x200.jpg",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Pies",
                                    "payload": "dessert_pies"
                                }
                            ]
                        },
                        {
                            "title": "Healthier",
                            "image_url": "http://consumerrecipe.conagrafoods.com/uploadedImages/img_3523_1159.jpg",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Healthier",
                                    "payload": "dessert_healthier"
                                }
                            ]
                        },
                        {
                            "title": "Quick",
                            "image_url": "http://consumerrecipe.conagrafoods.com/uploadedImages/img_6069_3928.jpg",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Quick",
                                    "payload": "dessert_quick"
                                }
                            ]
                        },
                        {
                            "title": "Seasonal",
                            "image_url": "http://honestcooking.com/wp-content/uploads/2012/07/coko-maline.jpg",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Seasonal",
                                    "payload": "dessert_seasonal"
                                }
                            ]
                        }
                    ]
                }
            }
        }
    }
    BREAKFAST_QUESTION = {
        "recipient": {
            "id": "USER_ID"
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": "Eggs",
                            "image_url": "http://consumerrecipe.conagrafoods.com/uploadedImages/img_3584_1254.jpg",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Eggs",
                                    "payload": "breakfast_eggs"
                                }
                            ]
                        },
                        {
                            "title": "Casserole",
                            "image_url": "http://consumerrecipe.conagrafoods.com/uploadedImages/img_3638_7390.jpg",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Casserole",
                                    "payload": "breakfast_casserole"
                                }
                            ]
                        },
                        {
                            "title": "Healthier",
                            "image_url": "http://consumerrecipe.conagrafoods.com/uploadedImages/img_7849_8323.jpg",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Healthier",
                                    "payload": "breakfast_healthier"
                                }
                            ]
                        },
                        {
                            "title": "Something Sweet",
                            "image_url": "http://consumerrecipe.conagrafoods.com/uploadedImages/img_7723_7992.jpg",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Something Sweet",
                                    "payload": "breakfast_sweet"
                                }
                            ]
                        }
                    ]
                }
            }
        }
    }
    BREAKFAST_TIME = {
        "recipient": {
            "id": "<USER_ID>"
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "button",
                    "text": "How much time do you have?",
                    "buttons": [
                        {
                            "type": "postback",
                            "title": "15 Minutes",
                            "payload": "bre-time_15"
                        },
                        {
                            "type": "postback",
                            "title": "30 Minutes",
                            "payload": "bre-time_30"
                        },
                        {
                            "type": "postback",
                            "title": "45 Minutes Or More",
                            "payload": "bre-time_45"
                        }
                    ]
                }
            }
        }
    }

    APPETIZER_QUESTION = {
        "recipient": {
            "id": "USER_ID"
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": "Cheesy",
                            "image_url": "http://www.desktopcookbook.com/images-recipe/129665.jpg",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Cheesy",
                                    "payload": "appetizer_cheesy"
                                }
                            ]
                        },
                        {
                            "title": "Meaty",
                            "image_url": "http://beyondwonderful.com/images/recipes/appetizers_wraps_prosciutto_karen_225x450.jpg",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Meaty",
                                    "payload": "appetizer_meaty"
                                }
                            ]
                        },
                        {
                            "title": "Veggies",
                            "image_url": "http://cdn.trendhunterstatic.com/thumbs/vegetarian-appetizers.jpeg",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Veggies",
                                    "payload": "appetizer_veggies"
                                }
                            ]
                        },
                        {
                            "title": "Healthier",
                            "image_url": "http://consumerrecipe.conagrafoods.com/uploadedImages/img_5206_2127.jpg",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Healthier",
                                    "payload": "appetizer_healthier"
                                }
                            ]
                        }
                    ]
                }
            }
        }
    }

    APPETIZER_HOT_COLD = {
        "recipient": {
            "id": "<USER_ID>"
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "button",
                    "text": "Hot Or Cold?",
                    "buttons": [
                        {
                            "type": "postback",
                            "title": "Hot",
                            "payload": "hot-cold_hot"
                        },
                        {
                            "type": "postback",
                            "title": "Cold",
                            "payload": "hot-cold_cold"
                        }
                    ]
                }
            }
        }
    }

    SIDE_DISH_QUESTION = {
        "recipient": {
            "id": "USER_ID"
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": "Potato",
                            "image_url": "http://consumerrecipe.conagrafoods.com/uploadedImages/img_1976_3591.jpg",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Potato",
                                    "payload": "side-dish_potato"
                                }
                            ]
                        },
                        {
                            "title": "Vegetable",
                            "image_url": "http://consumerrecipe.conagrafoods.com/uploadedImages/img_6043_3643.jpg",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Vegetable",
                                    "payload": "side-dish_vegetable"
                                }
                            ]
                        },
                        {
                            "title": "Rice",
                            "image_url": "http://consumerrecipe.conagrafoods.com/uploadedImages/img_1907_3613.jpg",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Rice",
                                    "payload": "side-dish_rice"
                                }
                            ]
                        },
                        {
                            "title": "Pasta",
                            "image_url": "http://consumerrecipe.conagrafoods.com/uploadedImages/img_5570_2455.jpg",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Pasta",
                                    "payload": "side-dish_pasta"
                                }
                            ]
                        },
                        {
                            "title": "Salad",
                            "image_url": "http://consumerrecipe.conagrafoods.com/uploadedImages/img_3812_1575.JPG",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Salad",
                                    "payload": "side-dish_salad"
                                }
                            ]
                        },
                        {
                            "title": "Beans",
                            "image_url": "http://consumerrecipe.conagrafoods.com/uploadedImages/img_6162_3889.jpg",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": "Beans",
                                    "payload": "side-dish_beans"
                                }
                            ]
                        }
                    ]
                }
            }
        }
    }
    DEFAULT_TEMPLATE = {
        "recipient": {
            "id": "USER_ID"
        },
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": []
                }
            }
        }
    }
    IMAGE_PATH = "http://consumerrecipe.conagrafoods.com/uploadedImages/"
    REPICE_PATH = "http://www.readyseteat.com"
    RECIPE_API_URL = "http://www.rws.conagrafoods.com/rest/site/246/recipes.json?sortby=season,newest,rating,publisheddate&order=desc,desc,desc,desc"
    PURE_RECIPE_API_URL = "http://www.rws.conagrafoods.com/rest/site/246/recipes.json?"
    DINNER_VIEW_MORE_URL = "http://www.readyseteat.com/advanced-search?keywords=&category=89&mainingredient=76&totaltime=60&cuisine=44"
    VIEW_MORE_URL = "http://www.readyseteat.com/advanced-search"

    QUICK_REPLY_MAIN =  {
        "recipient": {
            "id": "USER_ID"
        },
        "message": {
            "text": 'What type of recipe would you like to make?',
            "quick_replies": [
                {
                    "content_type": "text",
                    "title": "Dinner",
                    "payload": "category_dinner"
                },
                {
                    "content_type": "text",
                    "title": "Dessert",
                    "payload": "category_dessert"
                },
                {
                    "content_type": "text",
                    "title": "Breakfast/Brunch",
                    "payload": "category_breakfast"
                },
                {
                    "content_type": "text",
                    "title": "Appetizer/Snack",
                    "payload": "category_appetizer"
                },
                {
                    "content_type": "text",
                    "title": "Side Dish",
                    "payload": "category_side dish"
                }
            ]
        }
    }

    DINNER_GUICK_REPLY = {
        "recipient": {
            "id": "USER_ID"
        },
        "message": {
            "text": 'Select a main ingredient:',
            "quick_replies": [
                {
                    "content_type": "text",
                    "title": "Chicken",
                    "payload": "main-ingredient_chicken"
                },
                {
                    "content_type": "text",
                    "title": "Beef",
                    "payload": "main-ingredient_beef"
                },
                {
                    "content_type": "text",
                    "title": "Pork",
                    "payload": "main-ingredient_pork"
                },
                {
                    "content_type": "text",
                    "title": "Seafood/Fish",
                    "payload": "main-ingredient_seafood"
                },
                {
                    "content_type": "text",
                    "title": "Pasta/Rice",
                    "payload": "main-ingredient_pasta"
                },
                {
                    "content_type": "text",
                    "title": "Vegetarian",
                    "payload": "main-ingredient_vegetarian"
                }
            ]
        }
    }

    TIME_QUICK_REPLY = {
        "recipient": {
            "id": "USER_ID"
        },
        "message": {
            "text": 'How much time do you have?',
            "quick_replies": [
                {
                    "content_type": "text",
                    "title": "30 Minutes",
                    "payload": "time_30"
                },
                {
                    "content_type": "text",
                    "title": "45 Minutes",
                    "payload": "time_45"
                },
                {
                    "content_type": "text",
                    "title": "60 Minutes",
                    "payload": "time_60"
                }
            ]
        }
    }

    REGION_QUICK_REPLY = {
        "recipient": {
            "id": "USER_ID"
        },
        "message": {
            "text": 'What sounds good?',
            "quick_replies": [
                {
                    "content_type": "text",
                    "title": "Asian",
                    "payload": "region_asian"
                },
                {
                    "content_type": "text",
                    "title": "Italian",
                    "payload": "region_italian"
                },
                {
                    "content_type": "text",
                    "title": "Mediterranean",
                    "payload": "region_mediterranean"
                },
                {
                    "content_type": "text",
                    "title": "Mexican",
                    "payload": "region_mexican"
                },
                {
                    "content_type": "text",
                    "title": "American",
                    "payload": "region_american"
                }
            ]
        }
    }

    DESSERTS_QUICK_REPLY = {
        "recipient": {
            "id": "USER_ID"
        },
        "message": {
            "text": 'What kind of dessert would you like to make?',
            "quick_replies": [
                {
                    "content_type": "text",
                    "title": "Cookies",
                    "payload": "dessert_cookies"
                },
                {
                    "content_type": "text",
                    "title": "Cakes",
                    "payload": "dessert_cakes"
                },
                {
                    "content_type": "text",
                    "title": "Pies",
                    "payload": "dessert_pies"
                },
                {
                    "content_type": "text",
                    "title": "Healthier",
                    "payload": "dessert_healthier"
                },
                {
                    "content_type": "text",
                    "title": "Quick",
                    "payload": "dessert_quick"
                },
                {
                    "content_type": "text",
                    "title": "Seasonal",
                    "payload": "dessert_seasonal"
                }
            ]
        }
    }

    BREAKFAST_QUICK_REPLY = {
        "recipient": {
            "id": "USER_ID"
        },
        "message": {
            "text": 'What kind of breakfast do you want?',
            "quick_replies": [
                {
                    "content_type": "text",
                    "title": "Eggs",
                    "payload": "breakfast_eggs"
                },
                {
                    "content_type": "text",
                    "title": "Casserole",
                    "payload": "breakfast_casserole"
                },
                {
                    "content_type": "text",
                    "title": "Healthier",
                    "payload": "breakfast_healthier"
                },
                {
                    "content_type": "text",
                    "title": "Something Sweet",
                    "payload": "breakfast_sweet"
                }
            ]
        }
    }

    BREAKFAST_TIME_QUICK_REPLY = {
        "recipient": {
            "id": "USER_ID"
        },
        "message": {
            "text": 'How much time do you have?',
            "quick_replies": [
                {
                    "content_type": "text",
                    "title": "15 Minutes",
                    "payload": "bre-time_15"
                },
                {
                    "content_type": "text",
                    "title": "30 Minutes",
                    "payload": "bre-time_30"
                },
                {
                    "content_type": "text",
                    "title": "45 Minutes Or More",
                    "payload": "bre-time_45"
                }
            ]
        }
    }

    APPETIZER_QUICK_REPLY = {
        "recipient": {
            "id": "USER_ID"
        },
        "message": {
            "text": 'What kind of appetizer or snack sounds good?',
            "quick_replies": [
                {
                    "content_type": "text",
                    "title": "Cheesy",
                    "payload": "appetizer_cheesy"
                },
                {
                    "content_type": "text",
                    "title": "Meaty",
                    "payload": "appetizer_meaty"
                },
                {
                    "content_type": "text",
                    "title": "Veggies",
                    "payload": "appetizer_veggies"
                },
                {
                    "content_type": "text",
                    "title": "Healthier",
                    "payload": "appetizer_healthier"
                }
            ]
        }
    }

    HOT_OR_COLD_QUICK_REPLY = {
        "recipient": {
            "id": "USER_ID"
        },
        "message": {
            "text": 'Hot or Cold?',
            "quick_replies": [
                {
                    "content_type": "text",
                    "title": "Hot",
                    "payload": "hot-cold_hot"
                },
                {
                    "content_type": "text",
                    "title": "Cold",
                    "payload": "hot-cold_cold"
                }
            ]
        }
    }

    SIDE_DISH_QUICK_REPLY = {
        "recipient": {
            "id": "USER_ID"
        },
        "message": {
            "text": 'Select a main ingredient:',
            "quick_replies": [
                {
                    "content_type": "text",
                    "title": "Potato",
                    "payload": "side-dish_potato"
                },
                {
                    "content_type": "text",
                    "title": "Vegetable",
                    "payload": "side-dish_vegetable"
                },
                {
                    "content_type": "text",
                    "title": "Rice",
                    "payload": "side-dish_rice"
                },
                {
                    "content_type": "text",
                    "title": "Pasta",
                    "payload": "side-dish_pasta"
                },
                {
                    "content_type": "text",
                    "title": "Salad",
                    "payload": "side-dish_salad"
                },
                {
                    "content_type": "text",
                    "title": "Beans",
                    "payload": "side-dish_beans"
                }
            ]
        }
    }

    QUICK_REPLY_ANOTHER_RECIPE = {
        "recipient": {
            "id": "USER_ID"
        },
        "message": {
            "text": 'Looking for another recipe?',
            "quick_replies": [
                {
                    "content_type": "text",
                    "title": "Yes",
                    "payload": "start over"
                },
                {
                    "content_type": "text",
                    "title": "Ask tomorrow",
                    "payload": "ask-tomorrow-payload"
                },
                {
                    "content_type": "text",
                    "title": "Ask in a week",
                    "payload": "ask-week-payload"
                },
                {
                    "content_type": "text",
                    "title": "Don't ask again",
                    "payload": "payload_unsubscribe"
                }
            ]
        }
    }
