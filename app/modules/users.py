from app.libraries import mongodb
import requests
import arrow

class Users(object):
    """docstring for Users"""

    def __init__(self, config):
        super(Users, self).__init__()
        self.config = config
        self.db = mongodb.getDb(self.config)
        self.storage = self.db["users"]

    def insert(self, user_data):
        user_id = self.storage.insert(user_data)
        return str(user_id)

    def updateUserLastNotification(self, fb_id):
        user = self.storage.find_one({"fb_id": fb_id})
        user["lastNotification"] = arrow.utcnow().naive
        self.storage.save(user)

    def makeNotificationDaily(self, fb_id):
        user = self.storage.find_one({"fb_id": fb_id})
        if user.get("notificationType", None) == "daily":
            return
        user["notificationType"] = "daily"
        user["lastNotification"] = arrow.utcnow().naive
        self.storage.save(user)

    def makeNotificationWeekly(self, fb_id):
        user = self.storage.find_one({"fb_id": fb_id})
        if user.get("notificationType", None) == "weekly":
            return
        user["notificationType"] = "weekly"
        user["lastNotification"] = arrow.utcnow().naive
        self.storage.save(user)

    def deactivateNotification(self, fb_id):
        user = self.storage.find_one({"fb_id": fb_id})
        user["notificationType"] = None
        user["lastNotification"] = None
        self.storage.save(user)

    def get_users_for_notification(self):
        dailyUsers = self.storage.find({
            "notificationType": "daily",
            "lastNotification": {"$lte": arrow.utcnow().replace(days=-1).naive}
        })
        daily = [user["fb_id"] for user in dailyUsers]
        weeklyUsers = self.storage.find({
            "notificationType": "weekly",
            "lastNotification": {"$lte": arrow.utcnow().replace(days=-7).naive}
        })
        weekly = [user["fb_id"] for user in weeklyUsers]
        return weekly + daily

    def get(self, fb_id):
        user = self.storage.find_one({"fb_id": fb_id})
        return user

    def get_all(self):
        users = self.storage.find()
        return list(users)

    def remove(self, fb_id):
        self.storage.remove({"fb_id": fb_id})
        return True
