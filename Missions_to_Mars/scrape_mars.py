# Import dependencies
from bs4 import BeautifulSoup
import pandas as pd
import requests
import pymongo
from splinter import Browser
import time



def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


#create mars_data dict that we can insert into mongo
mars_data = {}

### Nasa Mars News
def scrape_news():
    browser = init_browser()

    try:
        # Visit the following URL
        url = 'https://mars.nasa.gov/news/'
        #response = requests.get(url)
        browser.visit(url)

        time.sleep(1)

        # Scrape page into Soup
        html = browser.html
        soup = BeautifulSoup(html, 'lxml')

        title = soup.find_all('div', class_= 'content_title')[1].text
        paragraph = soup.find_all('div', class_= 'article_teaser_body')[1].text

        # Store data in a dictionary
        mars_data ["title"] = title
        mars_data ["paragraph"] = paragraph

        return mars_data 

    finally:
        
        browser.quit()



### JPL Mars Space Images - Featured Image
def scrape_image():
    try:

        browser = init_browser()
        
        # Visit the following URL
        url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
        browser.visit(url)

        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        
        image_url = soup.find('div', class_='img').find('img', class_= 'thumb')['src']

        main_url = 'https://www.jpl.nasa.gov'

        feature_image_url = main_url + image_url

        mars_data ['feature_image_url'] = feature_image_url
        
        return mars_data
    
    finally:
        
        browser.quit()

        
### Mars Weather
def scrape_weather():
    try:
        
        browser = init_browser()
        
        # Visit the following URL
        url = "https://twitter.com/marswxreport?lang=en"
        browser.visit(url)

        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        
        results = soup.find('div', class_= 'css-1dbjc4n')
        weather = results.find_all('span')

        for x in range(len(weather)):
            if 'sol' in weather[x].text:
                break
        weather = (weather[x].text)

        mars_data ['weather'] = weather
                                            
        return mars_data
    
    finally:
        
        browser.quit()


### Mars Facts
def scrape_facts():
    try:

        url = 'https://space-facts.com/mars/'

        facts = pd.read_html(url)
        #facts

        df_mars = facts[0]
        df_mars.columns = ['Mars','Data']
        df_mars.set_index('Mars', inplace=True)
        df_mars

        html_table = df_mars.to_html()
        #html_table


        html_table.replace('\n', '')


        df_mars.to_html('table.html')

        mars_data ['facts'] = html_table
        
        return mars_data
    
    finally:
        
        pass
    

### Mars Hemispheres
def scrape_hemis():
    try:

        url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

        browser = init_browser()

        browser.visit(url)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        items = soup.find_all('div', class_='item')

        hemis_title = []
        hemis_url = []

        main_url = 'https://astrogeology.usgs.gov'

        for item in items:
            title = item.find('h3').text
            hemis_title.append(title)

            partial_img = item.find('a', class_= 'itemLink product-item')['href']

            browser.visit(main_url + partial_img)
            partial_img = browser.html
            soup = BeautifulSoup(partial_img, 'lxml')

            img_url = main_url + soup.find('img', class_='wide-image')['src']

            hemis_url.append(img_url)

        mars_data ['hemis_title'] = hemis_title
        mars_data ['hemis_url'] = hemis_url

        return mars_data
    
    finally:

        browser.quit() 