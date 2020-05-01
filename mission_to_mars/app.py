from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars
from pprint import pprint

# Create an instance of our Flask app
app=Flask(__name__)

# Pass connection to the pymongo instance.
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")

@app.route("/")
def index():
    # Find one record of data from the mongo database
    mars = mongo.db.mars.find_one()
        
    # Return template and data
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scraper():
    # Run the scrape function
    mars_data = scrape_mars.scrape()
    
    # Update the Mongo database using update and upsert=True
    mongo.db.mars.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)