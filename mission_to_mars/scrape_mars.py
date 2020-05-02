from bs4 import BeautifulSoup as bs
import pandas as pd 
from selenium import webdriver
from splinter import Browser
import requests
import time

def scrape():
    # Retrieve NASA Mars News page with the requests module
    url = 'http://mars.nasa.gov/news/'
    response = requests.get(url)
    # Save page data into Soup
    soup = bs(response.text, "html.parser")
    # Filter results to article data to find titles
    results = soup.find_all('div', class_="content_title")
    # Filter to the latest article on the site
    result_first = results[0]
    # Scrape title of latest article
    title = result_first.a.string.strip()
    # Filter results to find article summary
    results2 = soup.find_all('div', class_="rollover_description_inner")
    # Filter to the latest article summary
    result2_first = results2[0]
    # Scrape summary of latest article
    p = result2_first.string.strip()
    # Save into dictionary
    
    # Retrieve JPL Mars page with the requests module
    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    response2 = requests.get(url2)
    jpl_soup = bs(response2.text, "html.parser")
    # Filter results to find featured image data
    jpl_results = jpl_soup.find('div', class_="carousel_container")
    # Filter results to url
    featured_image = jpl_results.find("a")
    # Scrape end of url for featured image
    url_end = featured_image.get("data-fancybox-href")
    # Create variable to hold whole url
    jpl_prefix = 'https://www.jpl.nasa.gov'
    featured_image_url = f"{jpl_prefix}{url_end}"

    # Import Mars Facts url with pandas
    url4 = 'https://space-facts.com/mars/'
    table = pd.read_html(url4)
    # Convert table to a dataframe
    df = table[0]
    # Name columns
    df.columns=["Description","Value"]
    # Set first column to index
    df.index.drop
    # Convert table to html & save
    mars_facts = df.to_html(classes=["table-bordered"], index=False)
      
    # Retrieve Mars Hemispheres image urls with splinter
    executable_path = {"executable_path": "C:/Users/vll14/chromedriver.exe"}
    browser = Browser("chrome", **executable_path, headless=False)
    url5 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url5)
    time.sleep(5)
    # Save hemispheres page data into Soup
    html5 = browser.html
    hemi_soup = bs(html5, "html.parser")
    # Find correct div and class
    hemi_links_div = hemi_soup.find_all('div', class_='item')
    # Set prefix for each image url
    base_url = 'https://astrogeology.usgs.gov'
    # Set up list to hold urls with image info
    hemi_names = []
    mars_links = []
    for result in hemi_links_div:
        href = result.find('a', class_='itemLink').get('href')
        hemi = result.find('h3').text
        hemi_names.append(hemi)
        url = f"{base_url}{href}"
        mars_links.append(url) 
        browser.quit()
    # Array for image url links - not working so didn't include in scraper
        
    # Create dictionary to hold scraped data
    Mars_Dict={
        "title": title,
        "summary": p,
        "featured_image_url": featured_image_url,
        "mars_facts": mars_facts,
        #"hemi_url1": hemi_links[0],
        "hemi1": hemi_names[0],
        #"hemi_url2": hemi_links[1],
        "hemi2": hemi_names[1],
        #"hemi_url3": hemi_links[2],
        "hemi3": hemi_names[2],
        #"hemi_url4": hemi_links[3],
        "hemi4": hemi_names[3], 
    }

    return Mars_Dict
    