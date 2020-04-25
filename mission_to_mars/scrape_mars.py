from bs4 import BeautifulSoup as bs
import pandas as pd 
from splinter import Browser
from selenium import webdriver
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
    # Scrape summary of latest article
    p = result2_first.string.strip()

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
    featured_image_url = f"{url2}{url_end}"

    # Retrieve Mars Weather Twitter page with Chromedriver
    url3 = 'https://twitter.com/marswxreport?lang=en'
    driver = webdriver.Chrome()
    driver.get(url3)
    time.sleep(3)
    # Find first tweet
    tweet_div = driver.find_elements_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div/div/div/div/div/div[2]/section/div/div/div[1]/div/div/div/article/div/div[2]/div[2]/div[2]/div[1]/div')

    # Import Mars Facts url with pandas
    url4 = 'https://space-facts.com/mars/'
    table = pd.read_html(url4)
    # Convert table to a dataframe
    df = table[0]
    # Generate html table
    html_table = df.to_html()
    # Strip newlines
    table_stripped = html_table.replace('\n', '')

    # Retrieve Mars Hemispheres image urls with 'get requests' module
    url5 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    response5 = requests.get(url5)
    # Save hemispheres page data into Soup
    hemi_soup = bs(response5.text, "html.parser")
    # Filter results to find image url data
    hemi_results = hemi_soup.find_all('div', class_="item")
    # Set prefix and suffix for each image url
    base_url = 'https://astropedia.astrogeology.usgs.gov/download/'
    url_suffix = '.tif'
    # Loop through results to get hemisphere name
    for item in hemi_results:
        name = item.find('h3').text.rsplit(" ",1)
        hemi = name[0]    
        # Loop through results to get url to add to base url
        hemi_href = item.find('a')['href']
        href_split = hemi_href.split("/",3)
        href = href_split[2]
        hemi_url = f"{base_url}{href}{url_suffix}"

    # Create dictionary to hold scraped data
    Mars_Dict:{
        "News Title": title,
        "News Summary": p,
        "Featured Image URL": featured_image_url,
        "Current Mars Weather": tweet_div,
        "Mars Facts Table": table_stripped,
        "Hemisphere Image URL": hemi_url,
        "Hemisphere Name": hemi
    }

    browser.quit()
    
    return Mars_Dict
    