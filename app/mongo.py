from pymongo import MongoClient

def conectar_db():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['mi_base_de_datos']
    collection = db['productos']
    return client, db, collection

def obtener_productos(collection):
    return [Producto(**prod) for prod in collection.find()]

def insertar_producto(collection, producto):
    collection.insert_one(producto.__dict__)

def actualizar_producto(collection, codigo, producto):
    collection.update_one({'codigo': codigo}, {'$set': producto.__dict__})

def eliminar_producto(collection, codigo):
    collection.delete_one({'codigo': codigo})
