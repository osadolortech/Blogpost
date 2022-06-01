from pymongo import MongoClient

client = MongoClient("mongodb+srv://osadolortech:Computer333@cluster0.ve2nnja.mongodb.net/NEWBASE?retryWrites=true&w=majority")

db = client.blog_post

collections_post = db["blog_app"]

 