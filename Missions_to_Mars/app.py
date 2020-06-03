from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


# Create an instance of Flask app
app = Flask(__name__)

#Use flask_pymongo to set up connection through mongo
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")

# Route to render index.html template using data from Mongo
@app.route('/')
def index():
    # Find one record of data from the mongo database
    mars_info = mongo.db.collection.find_one()

    # Return template and data
    return render_template('index.html', mars=mars_info)

# Route that will trigger scrape function
@app.route('/scrape')
def scrape():
    # Run the scrape functions
    mars_data = scrape_mars.scrape_news()
    mars_data = scrape_mars.scrape_image()
    mars_data = scrape_mars.scrape_facts()
    mars_data = scrape_mars.scrape_weather()
    mars_data = scrape_mars.scrape_hemis()
    # Update the Mongo database using update and upsert=True
    mongo.db.collection.update({}, mars_data, upsert=True)

    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
