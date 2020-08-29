from flask import Flask, render_template, request, redirect, url_for
import os
import pytz
from flask_pymongo import pymongo
from decouple import config
from datetime import datetime
from bson.objectid import ObjectId

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

    cate = request.args.get('cate')
    aStarter = request.args.get('aStarter')
    aTitle = request.args.get('aTitle')
    aDesc = request.args.get('aDesc')

    # Render the data in 'index.html' page
    if cate and aStarter and aTitle and aDesc:
        return render_template("index.html", data=cursor, cate=cate, aStarter=aStarter, aTitle=aTitle, aDesc=aDesc)

    elif aTitle and aDesc:
        return render_template("index.html", data=cursor, aTitle=aTitle, aDesc=aDesc)

    else:
        return render_template("index.html", data=cursor)
    

# POST route : Create task
@app.route('/', methods=["POST"])
def insert_data():
    
    try:
        # Get form data
        title = request.form.get('title')               # Get create task form title
        description = request.form.get('description')   # Get create task form description
        dtObj = datetime.now(tz=pytz.timezone('Asia/Singapore'))                          # Get current timestamp        

    except Exception as e:
        print(e)
    
    else:
        # Update statement and insert into alert later on                
        aTitle = title
        aDesc = description

        # Insert data into MongoDB with
        # title, description and current timestamp
        collection.insert({        
            "title": title,
            "description": description,
            "timestamp": dtObj.strftime('%Y-%m-%d %H:%M:%S %z')
        })

    # Redirect to 'index' route
    return redirect(url_for('index', aTitle=aTitle, aDesc=aDesc))


# POST route : Delete task
@app.route("/delete", methods=["POST"])
def delete_data():
    
    try:        
        # Retrieve object id
        taskID = request.form.get('hTaskID')         # TaskID
        title = request.form.get('delete-title')    # Title
        description = request.form.get('delete-desc')      # Description 

    except Exception as e:
        print(e)        
    
    else:

        # Update statement and insert into alert later on
        cate = "delete"
        aStarter = 'Task: {}'.format(taskID)
        aTitle = title
        aDesc = description

        # Delete one record of selected object ID       
        collection.delete_one({'_id': ObjectId(taskID)})        

    # Redirect to 'index' route
    return redirect(url_for('index', cate=cate, aStarter=aStarter, aTitle=aTitle, aDesc=aDesc))


# POST route : Update task
@app.route("/update", methods=["POST"])
def update_data():

    try:
        taskID = request.form.get('hTaskID')     # Get TaskID
        title = request.form.get('edit-title')  # Get Title content
        description = request.form.get('edit-desc') # Get Description content
        dtObj = datetime.now(tz=pytz.timezone('Asia/Singapore')) # Timestamp

    except Exception as e:
        print(e)        

    else:

        # Update statement and insert into alert later on
        cate = "update"
        aStarter = "TaskID: {}".format(taskID)
        aTitle = title
        aDesc = description

        # Update one record of selected object ID
        # with title, description and current timestamp
        collection.update_one({ '_id': ObjectId(taskID) },
            {'$set': 
                {
                    'title': title,
                    'description': description,
                    "timestamp": dtObj.strftime('%Y-%m-%d %H:%M:%S %z')
                }
            }, upsert=False)        
        
    # Redirect to 'index' route
    return redirect(url_for('index', cate=cate, aStarter=aStarter, aTitle=aTitle, aDesc=aDesc))


if __name__ == '__main__':  # Script executed directly?    
    app.run()