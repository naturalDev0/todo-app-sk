from flask import Flask, render_template, request, redirect, url_for
import os
from flask_pymongo import pymongo
from decouple import config
from datetime import datetime

app = Flask(__name__)

# User credentials
usr = config('MONGO_DB_USER')
pwd = config('MONGO_DB_PASS')
db_collection = config('MONGO_COLLECTION')
db_name = config('MONGO_DB_NAME')

# MongoDB filepath
client  = pymongo.MongoClient("mongodb+srv://" + usr + ":" + pwd + "@clusterx.pg3wu.mongodb.net/"+ db_collection +"?retryWrites=true&w=majority")

# MongoDB variables
db = client[db_name]
collection = db[db_collection]

# Default route
@app.route('/')
def index():
    
    # Retrieve all data from collection
    cursor = collection.find({})

    # Render the data in 'index.html' page
    return render_template("index.html", data=cursor)

# Post route
@app.route('/', methods=["POST"])
def insert_data():
    
    # Get form data
    title = request.form.get('title')               # Form Title
    description = request.form.get('description')   # Form Description
    task_count = collection.count() + 1             # Current total count of documents within collection

    # Insert data into MongoDB
    collection.insert({
        "task_no": task_count,
        "title": title,
        "description": description
    })

    # Redirect to 'index' route
    return redirect(url_for('index'))

@app.route("/<id>")
def delete_data():

    return True

# @app.route("/test")
# def insert_new_field():

#     dtObj = datetime.now()
#     # collection.updateMany({}, {"$set": {"timestamp": dtObj}},False,True) 
#     print(dtObj)
#     print(collection)
    
#     cursor = collection.distinct('_id')
#     for c in cursor:
#         print(c)
#         collection.update_one({'_id':c},{'$set': {'timestamp':dtObj }})

#     return "<h1>Data Inserted</h1>"