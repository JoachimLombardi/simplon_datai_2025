from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.gpt_db
collection = db.quotes

collection.create_index([("quote", "text"), ("author", "text")])