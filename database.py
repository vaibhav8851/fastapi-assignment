from pymongo import MongoClient

# Your MongoDB connection string
client = MongoClient("mongodb+srv://vinayshikhawat882:MeFTW7TPYRUDxdB2@cluster0.x2kvg.mongodb.net/fastapi_db?retryWrites=true&w=majority")
db = client.cluster0
