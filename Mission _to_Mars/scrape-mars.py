# Declare Dependencies 
from bs4 import BeautifulSoup
from splinter import Browser
import pandas as pd
import os
import time
import requests
import warnings
warnings.filterwarnings('ignore')

def init_browser():
    executable_path = {r"C:\Users\alann\.wdm\drivers\chromedriver\win32\86.0.4240.22\chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=True)

# Create Mission to Mars global dictionary that can be imported into Mongo
mars_info = {}

# NASA MARS NEWS
def scrape_mars_news():

        # Initialize browser 
        browser = init_browser()

        # Visit Nasa news url through splinter module
        url = 'https://mars.nasa.gov/news/'
        browser.visit(url)

        # HTML Object
        html = browser.html

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')

        # Retrieve the latest element that contains news title and news_paragraph
        news_title = soup.find('div', class_='content_title').find('a').text
        news_p = soup.find('div', class_='article_teaser_body').text

        # Dictionary entry from MARS NEWS
        mars_info['news_title'] = news_title
        mars_info['news_paragraph'] = news_p

        return mars_info

        browser.quit()

# FEATURED IMAGE
def scrape_mars_image():

        # Initialize browser 
        browser = init_browser()

        #browser.is_element_present_by_css("img.jpg", wait_time=1)

        # Visit Mars Space Images through splinter module
        featured_image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars/spaceimages/images/wallpaper/PIA24242-640x350.jpg'
        browser.visit(featured_image_url)

        # HTML Object 
        html_image = browser.html

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')

        # Retrieve background-image url from style tag 
        image_url  = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]

        # Website Url 
        main_url = 'https://www.jpl.nasa.gov'

        # Concatenate website url with scrapped route
        image_url = main_url + image_url

        # Display full link to featured image
        image_url 

        # Dictionary entry from FEATURED IMAGE
        mars_info['image_url'] = image_url 
        
        browser.quit()

        return mars_info


# Mars Facts
def scrape_mars_facts():

        # Initialize browser 
        browser = init_browser()

         # Visit Mars facts url 
        facts_url = 'http://space-facts.com/mars/'
        browser.visit(url)

        # Use Pandas to "read_html" to parse the URL
        tables = pd.read_html(url)
        #Find Mars Facts DataFrame in the lists of DataFrames
        mars_facts_df = tables[2]
        #Assign the columns
        mars_facts_df.columns = ['Description', 'Value']
        mars_html_table = df.to_html(table_id="html_tbl_css",justify='left',index=False)

        # Dictionary entry from Mars Facts

        mars['tables'] = html_table

        return mars_info

# Mars Hemisphere

def scrape_mars_hemispheres():

        # Initialize browser 
        browser = init_browser()

        # Visit hemispheres website through splinter module 
        hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(hemispheres_url)

        # HTML Object
        hemispheres_html = browser.html

        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(hemispheres_html, 'html.parser')

        # Retreive all items that contain mars hemispheres information
        all_mars_hemispheres = hemispheres_soup.find('div', class_='collapsible results')
        mars_hemispheres = all_mars_hemispheres.find_all('div', class_='item')


        # Create empty list for hemisphere urls 
        hemisphere_image_urls = []

        # Store the main_ul 
        usgs_url = 'https://astrogeology.usgs.gov' 

        # Loop through the items previously stored
        for i in mars_hemispheres: 
            # Collect Title
            hemisphere = i.find('div', class_="description")
            title = hemisphere.h3.text
            
            # Collect image link by browsing to hemisphere page
            hemisphere_link = hemisphere.a["href"]    
            browser.visit(usgs_url + hemisphere_link)
            
            image_html = browser.html
            image_soup = BeautifulSoup(image_html, 'html.parser')
            
            image_link = image_soup.find('div', class_='downloads')
            image_url = image_link.find('li').a['href']

            # Create Dictionary to store title and url info
            image_dict = {}
            image_dict['title'] = title
            image_dict['img_url'] = image_url
            
            hemisphere_image_urls.append(image_dict)

        mars_info['hemisphere_image_urls'] = hemisphere_image_urls
        
       
        browser.quit()

        # Return mars_data dictionary 

        return mars_info
