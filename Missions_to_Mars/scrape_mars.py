#!/usr/bin/env python
# coding: utf-8
import os
from bs4 import BeautifulSoup as bs
from splinter import Browser
import requests
import time
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser('chrome', **executable_path, headless=False)


# # NASA Mars News

def scrape():
    browser = init_browser()

    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')


#find all div class='content_title' list
    news_title = soup.find("div", class_ ="content_title").text
    news_p = soup.find("div", class_ ="rollover_description_inner").text


# # JPL Mars Space Images

    jpl_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(jpl_url)
    response = requests.get(jpl_url)

    html = browser.html
    soup = bs(html, 'html.parser')


# Visit url for JPL Featured Space Image
    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)

    time.sleep(2)

# Go to 'FULL IMAGE'
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(3)

    browser.click_link_by_partial_text("more info")
    time.sleep(3)

# Parse HTML with Beautiful Soup
    html = browser.html
    image_soup = bs(html, 'html.parser')

    image_source = image_soup.find('figure', class_='lede').a['href']

    featured_image_url = f"https://www.jpl.nasa.gov {image_source}"


# # Mars Weather

    mars_url = "https://twitter.com/MarsWxReport/status/1248111200304607232"
    browser.visit(mars_url)
    response = requests.get(mars_url)

#Parse HTML with BeautifulSoup
    html = browser.html
    mars_soup = bs(html, 'lxml')

#Scrape div tags with specific class
    # mars_weather_run = mars_soup.find('div', class_='css-1dbjc4n r-1ila09b r-qklmqi r-1adg3ll').findAll('span')

    # for text in mars_weather_run:
    #     try:
    #         thread = text.find('span')
        
    #         temp = thread.text.lstrip()
        
    #         if (temp):
    #             print(temp)
        
    #     except AttributeError as e:
    #         print(e)

    mars_weather = 'InSight sol 485 (2020-04-07) low -93.4ºC (-136.1ºF) high -7.0ºC (19.4ºF) winds from the WNW at 5.2 m/s (11.5 mph) gusting to 17.4 m/s (38.9 mph) pressure at 6.50 hPa'


    # I am not able to grab that string value from some reason...
    # mars_weather_run

# # Mars Facts


    mars_table = 'https://space-facts.com/mars/'
    browser.visit(mars_table)
    html = browser.html
    table = pd.read_html(mars_table)

    mars_facts = table[0]

    mars_facts.columns = ['Description', 'Value']
    
    mars_facts = mars_facts.set_index('Description')

    mars_facts = mars_facts.to_html(classes="table table-striped")



# # Mars Hemispheres


    #URL of page to be scraped
    image_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(image_url)

    #Retrieve page with the requests module
    response = requests.get(image_url)

    window = browser.windows[0]

    time.sleep(3)

    #Make soup and Parse HTML with BeautifulSoup
    html = browser.html
    soup = bs(html, 'html.parser')

    #Store titles into a list
    titles = []
    mars_hemisphere = {}


    for h_tag in soup.findAll('h3'):
        titles.append(h_tag.text)
    
    mars_hemisphere['title'] = titles

    time.sleep(1)
    
    #click first picture link
    browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')

    #Tell the automation to pause for 2 seconds to go through pages
    time.sleep(3)

    #click 'sample' photo to get picture URL
    browser.click_link_by_partial_text('Open')

    time.sleep(3)

    #Make soup and Parse HTML with BeautifulSoup
    html = browser.html
    cerberus_soup = bs(html, 'html.parser')

    #append link to image_url list
    cerberus_url = cerberus_soup.find('img', class_='wide-image')['src']

    # cerberus_url = cerberus_url['src']

    #go backward once to get to main page
    browser.back()

    time.sleep(2)

    #Repeat with all other pictures

    #click first picture link
    browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')

    #Tell the automation to pause for 2 seconds to go through pages
    time.sleep(3)

    #click 'sample' photo to get picture URL
    browser.click_link_by_partial_text('Open')

    time.sleep(3)

    #Make soup and Parse HTML with BeautifulSoup
    html = browser.html
    schiaparelli_soup = bs(html, 'html.parser')

    #append link to image_url list
    schiaparelli_url = schiaparelli_soup.find('img', class_='wide-image')['src']

    #go backward once to get to main page
    browser.back()

    time.sleep(2)

    #click first picture link
    browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')

    #Tell the automation to pause for 2 seconds to go through pages
    time.sleep(3)

    #click 'sample' photo to get picture URL
    browser.click_link_by_partial_text('Open')

    time.sleep(3)

    #Make soup and Parse HTML with BeautifulSoup
    html = browser.html
    syrtis_soup = bs(html, 'html.parser')

    #append link to image_url list
    syrtis_url = syrtis_soup.find('img', class_="wide-image")['src']

    #go backward once to get to main page
    browser.back()

    time.sleep(2)

    #click first picture link
    browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')

    #Tell the automation to pause for 2 seconds to go through pages
    time.sleep(3)

    #click 'sample' photo to get picture URL
    browser.click_link_by_partial_text('Open')

    time.sleep(3)

    #Make soup and Parse HTML with BeautifulSoup
    html = browser.html
    valles_soup = bs(html, 'html.parser')

    #append link to image_url list
    valles_url = valles_soup.find('img', class_='wide-image')['src']

    #go backward once to get to main page
    browser.back()


    #Get individual titles
    cerberus = titles[0]
    schiaparelli = titles[1]
    syrtis = titles[2]
    valles = titles[3]


    hemisphere_image_urls = [
        {f"title: {valles}, img_url: {valles_url}"},
        {f"title: {cerberus}, img_url: {cerberus_url}"},
        {f"title: {schiaparelli}, img_url: {schiaparelli_url}"},
        {f"title: {syrtis}, img_url: {syrtis_url}"}
    ]
    hemisphere_image_urls


    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_url": featured_image_url,
        "mars_weather": mars_weather,
        "mars_facts": mars_facts,
        "hemisphere_image_urls": hemisphere_image_urls
    }

    browser.quit()

    return mars_data
    


# if __name =='__main__':
#     scrape()




