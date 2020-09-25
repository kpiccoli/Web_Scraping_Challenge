Mars Facts and Images Scraped from Multiple Sources

Initial

Project Description

The goal of the project is to scrape the multiple web sources with information and images about Mars and NASA, store it in a database and finally display it in a customized web site. For this project, a flask server was created to scrape a series of URLs described below, the information was stored in a MongoDBdatabase and the information was displayed into a website. A screenshot of the final result is presented below too.

Sample website

Initial

Scraped Urls

NASA Mars News (text)
JPL Mars Space Images - Featured Image (image)
Mars Weather (text)
Mars Facts (table)
Mars Hemispheres (images)
Necessary Steps to Run all the Project

Install or have installed these libraries in your Git Environment: - pandas - splinter - bs4 - urllib.parse - time - flask - flask_pymongo
Download or have downloaded the chromedriver.exe in the path "/usr/local/bin/chromedriver" for Mac Users
Run the Mongo daemon, in one terminal window run ~/mongodb/bin/mongod. This will start the Mongo server.
Run the \Missions_to_Mars\app.py file
Open your browser and visit the URL: http://127.0.0.1:5000/
File Description

- Missions_to_Mars\

- app.py

Contains Python app that uses the flask library that runs the server in the URL: http://127.0.0.1:5000/ and calls the Missions_to_Mars\templates\index.html file
- mission_to_mars.ipynb

Contains the Jupyter Notebook with the explained code for scrapping the different URLs used in the project
- scrape_mars

Contains Python routine used and called by the main routine \Missions_to_Mars\app.py and it is called by pressing the Scrape New Databutton in the URL: http://127.0.0.1:5000/
- ScreenShots

1. Initial.png - It is the screenshot of the initial state of the Missions_to_Mars\templates\index.html file before running the Scrape New Data button which calls the \Missions_to_Mars\scrape_mars.py routine
2. Final.png - It is the screenshot of the final state of the Missions_to_Mars\templates\index.html file after running the Scrape New Databutton which calls the \Missions_to_Mars\scrape_mars.py routine
- templates

index.html - Contains the HTML and CSS codes necessary for the presentation of the scrapped data obtained by Scrape New Databutton which calls the \Missions_to_Mars\scrape_mars.py routine
