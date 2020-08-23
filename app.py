from flask import Flask, render_template, request, redirect, url_for
import os
from flask_pymongo import pymongo
from decouple import config

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
    
    title = request.form.get('title')
    description = request.form.get('description')
    task_count = collection.count() + 1

    print(title, description, task_count)

    collection.insert({
        "task_no": task_count,
        "title": title,
        "description": description
    })

    return redirect(url_for('index'))

# # Testing purposes
# @app.route('/test')
# def test():
#     collection.insert({
#         "text" : "hihi",
#         "complete" : False
#     })
#     return '<h1>Data has been inserted!</h1>'

# @app.route('/verify')
# def verify():
#     return '<h1>' + pwd + '</h1>'