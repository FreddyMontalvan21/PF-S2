from pymongo import MongoClient

def conectar_db():
    mongo_base = MongoClient('mongodb://localhost:27017/')
    db = mongo_base['productodb']
    coleccion = db['productos']
    return mongo_base, db, coleccion
