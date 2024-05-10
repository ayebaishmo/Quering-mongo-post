import pymongo

# Credentials

DBNAME = 'test'
PASSWORD = 'Lord'

def mongo_connect(password = PASSWORD, dbname = DBNAME, collection_name = 'armory_item'):
    client = pymongo.MongoClient(f'mongodb+srv://ishmo:{password}@cluster0.egh1tqc.mongodb.net/{dbname}?retryWrites=true&w=majority&appName=Cluster0')
    db = client[dbname]
    collection = db[collection_name]
    return collection

if __name__ == "__main__":
    collection = mongo_connect(collection_name='charactercreator_character')
    result = collection.count_documents({})
    print(result)