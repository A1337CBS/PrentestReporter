import pymongo
from gridfs import GridFS

__author__ = 'jslvtr'


class Database(object):
    #these two variables will be the same for each object of type database (static variables)
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None
    fs = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['PentestReporter']
        Database.fs = GridFS(Database.DATABASE)

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)

    @staticmethod
    def update_one(collection, obj, newObj):
        return Database.DATABASE[collection].update_one(obj, newObj)
    #update_one({"name":"John"}, {"$set":{"name":"Joseph"}})

    @staticmethod
    def delete_one(collection, query):
        return Database.DATABASE[collection].delete_one(query)

    @staticmethod
    def delete_many(collection, query):
        return Database.DATABASE[collection].delete_many(query)

    @staticmethod
    def delete_many(collection, query):
        return Database.DATABASE[collection].delete_many(query)

    @staticmethod
    def saveFile(image, filename):
        image_id = Database.fs.put(image, filename=filename)
        return image_id

    @staticmethod
    def getFile(image_id):
        imagedata = Database.fs.get(image_id).read()
        return imagedata

    @staticmethod
    def getFileByName(filename):
        file = Database.fs.find_one({"filename": filename})
        if file != None:
            imagedata = Database.fs.get(file._id).read()
            return imagedata
        else:
            return None