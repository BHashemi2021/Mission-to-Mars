from flask import Flask, render_template, redirect, url_for 
from flask_pymongo import PyMongo
import scraping

# Set up Flask
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase" 
mongo = PyMongo(app)


# First, define the route for the HTML page
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)


# We add the next route and function to our code
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   # Now that we've gathered new data, we need to update the database
   mars.update({}, mars_data, upsert=True)
   return "Scraping Successful!"
   # return redirect('/', code=302)


# Tell Flask to run the code 
if __name__ == "__main__":
   app.run(debug=True)