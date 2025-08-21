from pymongo import MongoClient

class LoaderData:

    def __init__(self,uri, db_name):
        self.URI = uri
        self.open_connection()
        self.db = self.client[db_name]
        self.collections =  self.db.list_collection_names()
        self.collection = self.collections[0]



    def open_connection(self):
        """ create connection to mongo db """
        try:
            self.client = MongoClient(self.URI)
            self.client.admin.command("ping")
            return True
        except Exception as e:
            self.client = None
            print("Error: ", e)
            return False


    def close_connection(self):
        if self.client:
            self.client.close()


    def get_all(self):
        """ return all the data of the db given """
        if self.client:
            collection = self.db[str(self.collection)]
            data = collection.find({}, {"_id": 0})
            return list(data)


#
# d = LoaderData("mDB")
# data = d.get_all()
# print(data)
