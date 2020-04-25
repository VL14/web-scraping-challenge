from flask, import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Create an instance of our Flask app
app=Flask(__name__)

# Use flask_pymongo to set up mongo connection
conn = "mongodb://localhost:27017"
client = PyMongo.MongoClient(conn)
db = client.mars_scraperDB

@app.route("/")
def index():
    # Find one record of data from the mongo database
    mars_db = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", data=mars_db)

@app.route("/scrape")
def scrape():
    # Run the scrape function
    mars_data = scrape_mars.scrape()
    
    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)