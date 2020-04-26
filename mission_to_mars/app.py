from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import pymongo
import scrape_mars

# Create an instance of our Flask app
app=Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.mars_db

# Drops collection if available to remove duplicates
db.mars.drop()

@app.route("/")
def index():
    # Find one record of data from the mongo database
    mars = db.collection.find_one()

    # Return template and data
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scraper():
    # Run the scrape function
    mars_data = scrape_mars.scrape()
    
    # Update the Mongo database using update and upsert=True
    db.collection.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)