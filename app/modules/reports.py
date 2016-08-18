from app.libraries import mongodb

import arrow

class Reports(object):
    """docstring for Reports"""
    def __init__(self, config):
        super(Reports, self).__init__()
        self.config = config
        self.database = mongodb.getDb(self.config)
        self.storage = self.database["unknowns"]

    def reportUnknown(self, message, user_id=None):
        record = {}
        if user_id:
            record["user"] = user_id
        record["message"] = message
        record["createdAt"] = arrow.utcnow().naive
        self.storage.insert(record)

    def getUnknowns(self):
        return list(self.storage.find())

    def getMonthlyUnknowns(self):
        lastMonth = self.storage.find({
                "createdAt": { 
                    "$gte" : arrow.utcnow().replace(months=-1).naive
                    }})
        return list(lastMonth)

    

