from app.controllers import bot

import configs

BOTS = {}
config = configs.get()

def getBotOfUser(user_id):
    
    global BOTS
    
    isNew = True

    if user_id in BOTS:
        isNew = False
        return BOTS[user_id], isNew
    b = bot.Bot(config, user_id)
    BOTS[user_id] = b
    return b, isNew


