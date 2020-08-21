from flask import Flask, render_template, request, redirect, url_for
import os
# from flask_pymongo import PyMongo

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("base.html")