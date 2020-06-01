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


# create mars_data dict that we can insert into mongo
#mars_data = {}



### Nasa Mars News
def scrape_info():
    mars_data = {}
    
    
    # Visit the following URL
    url = 'https://mars.nasa.gov/news/'
    response = requests.get(url)
        
    browser = init_browser()
    
    browser.visit(url)

    #html = browser.html
    soup = BeautifulSoup(response.text, 'lxml')

    #article = soup.find('ul', class_='item_list')
    #print(article)

    title = soup.find('div', class_= 'content_title').find('a').text
    paragraph = soup.find('div', class_= 'rollover_description_inner').text.strip()

    # Store data in a dictionary
    mars_data ["title"] = title
    mars_data ["paragraph"] = paragraph

    print(mars_data)
    return mars_data 

if __name__ == "__main__":
    print(scrape_info())



        # ### JPL Mars Space Images - Featured Image

        # # Visit the following URL
        # url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
        # browser.visit(url)

        # html = browser.html
        # soup = BeautifulSoup(html, 'html.parser')
        
        # image_url = soup.find('div', class_='img').find('img', class_= 'thumb')['src']

        # main_url = 'https://www.jpl.nasa.gov'

        # feature_image_url = main_url + image_url

        # mars_data ['feature_image_url'] = feature_image_url

        
        # # ### Mars Weather

        # # Visit the following URL
        # url = "https://twitter.com/marswxreport?lang=en"
        # browser.visit(url)

        # html = browser.html
        # soup = BeautifulSoup(html, 'html.parser')
        
        # results = soup.find('div', class_= 'css-1dbjc4n')
        # weather = results.find_all('span')

        # for x in range(len(weather)):
        #     if 'sol' in weather[x].text:
        #         print (weather[x].text)
        #         mars_data ['weather'] = weather[x]
        #         break
        
        


        # # ### Mars Facts

        # url = 'https://space-facts.com/mars/'

        # facts = pd.read_html(url)
        # facts

        # df_mars = facts[0]
        # df_mars.columns = ['Mars','Data']
        # df_mars.set_index('Mars', inplace=True)
        # df_mars

        # html_table = df_mars.to_html()
        # html_table


        # html_table.replace('\n', '')


        # df_mars.to_html('table.html')

        # mars_data ['facts'] = html_table


        # # ### Mars Hemispheres

        # url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

        # browser.visit(url)
        # html = browser.html
        # soup = BeautifulSoup(html, 'html.parser')

        # items = soup.find_all('div', class_='item')

        # images = []

        # main_url = 'https://astrogeology.usgs.gov'

        # for item in items:
        #     title = item.find('h3').text
        #     partial_img = item.find('a', class_= 'itemLink product-item')['href']

        #     browser.visit(main_url + partial_img)
        #     partial_img = browser.html
        #     soup = BeautifulSoup(partial_img, 'html.parser')

        #     img_url = main_url + soup.find('img', class_='wide-image')['src']

        #     images.append({'Title': title, 'img_url': img_url})

        # mars_data ['images'] = images


        # # Close the browser after scraping
        # browser.quit()

        # # Retrun results
        # return mars_data
