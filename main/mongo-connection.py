import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv('../.env')

password = os.getenv('MONGO_PASSWORD')

connection_string = f"mongodb+srv://guntherhaaseng:{password}@cluster.1ze8ias.mongodb.net/"

client = MongoClient(connection_string)

db = client.ProjetBibleDatabase

try:
    collections = db.list_collection_names()
    print("Connection successful. Collections in database are:", collections)
except Exception as e:
    print("Connection failed. Error:", e)
