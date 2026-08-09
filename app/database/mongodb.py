from pymongo import MongoClient

from app.config.settings import settings


client = MongoClient(settings.mongodb_url)

db = client[settings.mongodb_database]

students_collection = db["students"]