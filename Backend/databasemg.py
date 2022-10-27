import pymongo
import certifi
from flask import Flask, jsonify, request
from flask_pymongo import PyMongo, ObjectId
from os import environ

MONGO_HOST="localhost"
MONGO_PUERTO="27017"
ca= certifi.where()

MONGO_URI="mongodb://"+MONGO_HOST+":"+MONGO_PUERTO+"/"
def dbconeccion():
    try:
        cliente=pymongo.MongoClient(MONGO_URI,tlsCAFile=ca)
        db = cliente["proyecto"]
        print("Coneccion a mongo exitosa")
        cliente.close()
    except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
        print("Tiempo exedido "+errorTiempo)
    except pymongo.errors.ConnectionFailure as errorConexion:
        print("Fallo al conectarse a mongodb "+errorConexion)
    return db
