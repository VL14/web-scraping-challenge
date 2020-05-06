# web-scraping-challenge

For this assignment, I built a web application that scrapes various websites for data related to Mars, then displays the information in a single HTML page. Requests, splinter, selenium, and pandas were used to scrape the websites. BeautifulSoup was used to parse website data. Mongo was used to store the scraped data, while Flask was used to render the data to the webpage.


The following websites were scraped:

--NASA Mars News Site(https://mars.nasa.gov/news/) - collected the latest news title and summary

--JPL Featured Space Image (https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars) - found image url for latest featured image

--Mars Facts webpage (https://space-facts.com/mars/) - scraped a table and converted it to an HTML table

--USGS Astrogeology site (https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) - scraped the hemisphere name and image url for the 4 hemispheres


Files included in Github:

--mission_to_mars jupyter notebook - used to write and test code

--scrape_mars python file - function with code from jupyter notebook that is called by the app

--app python file - calls the scrape function, saves the data to mongo, and sets up Flask routes

--templates -> index.html - code to render the webpage

--website1 & website2 - screenshots of final website

