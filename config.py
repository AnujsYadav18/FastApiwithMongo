
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://anujyadav:sde180699@learnmongo.xggv0ri.mongodb.net/?retryWrites=true&w=majority&appName=learnmongo"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

#add db, collection


db = client.employee_info  #create database named "employee_info"
collection = db["emp_info"]  #create collection named "emp_info"