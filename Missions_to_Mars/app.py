# 1. import Flask
from flask import Flask, render_template, request
from flask_pymongo import PyMongo
    
import pandas as pd
import numpy as np
import scrape_mars

import pymongo

app = Flask(__name__)

#Database
app.config['MONGO_URI'] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


# 3. Define route
@app.route("/")
def index():

    mars_data = mongo.db.mars_data.find_one()
    return render_template('index.html', mars_data=mars_data)
    

@app.route("/scrape")
def scrape():

    mars_data = scrape_mars.scrape()

    mongo.db.mars_data.update({}, mars_data, upsert=True)
    return 'Complete!!'
    
# 4. Define main bahavior
if __name__ == "__main__":
    app.run(debug=True)
