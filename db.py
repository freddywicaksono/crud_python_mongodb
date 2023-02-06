import pymongo

class MongoDB:
    def __init__(self, db_name, collection_name):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_one(self, document):
        return self.collection.insert_one(document)

    def find_one(self, filter=None):
        return self.collection.find_one(filter)

    def find(self, filter=None):
        return self.collection.find(filter)

    def update_one(self, filter, update):
        return self.collection.update_one(filter, update)

    def delete_one(self, filter):
        return self.collection.delete_one(filter)