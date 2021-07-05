# Mission To Mars
* Scraping web with HTML and CSS*

## Overview

Robin, who loves astronomy and wants to work for NASA one day, has decided to use a specific method of gathering the latest data: web scraping. We have been tasked to help Robin build a web app is looking good and functioning well to pull and display the latest feature stories from NASA and the related image. She also likes a table to hold and compare facts between the two planets, the Earth and Mars. Moreover she has been admiring images of Mars’s hemispheres online on another website and realizes that the site is scraping-friendly. She would like to adjust the current web app to include all four of the hemisphere images. To do this, we have to use BeautifulSoup and Splinter to scrape full-resolution images of Mars’s hemispheres and the titles of those images, store the scraped data on a Mongo database, use a web application to display the data, and alter the design of the web app to accommodate these images (Figure 1).



#### Figure 1: The resultant Website pulling data from NASA and two other websites

-------------------

<p align="center">  
<img src="https://github.com/BHashemi2021/Mission-to-Mars/blob/main/Mars_Scraping/Resources/scraping-NASA-Mars-website.png" width="75%" height="75%">
</p>

------------------

The data Robin wants to collect from this particular website is the most recent news article. More specifically, we need the summary of the latest news article. 

The code for this will eventually be used in an application that will scrape live data by click a button — this site is dynamic and the articles will change frequently, which is why Robin is removing the manual task of retrieving each news article.


## Technically:
	
	
	1- We will write two separate scripts in Python Environment language in Jupyter Notebook to test the results at every step of the way and finally export them as app.py and scraping.py.
	
	2- We will run the app by calling it through Anaconda terminal using Python language. The app.py will employ the scraping script to scrape data from the three websites.
	
	
	3- To scrape the data we will identify the HTML and CSS components of the three aforesaid websites by  ** Chrome Developer Tool.
	
	4- The we will extract the needed data by * Beautiful Soup 
	
	5- Automate the web browser to visit each website by * Splinter
	
	6- Store the scraped data by MongoDB, NoSQL database for un-formatted data (data that is not tabular - we use SQL for holding tabular data).
	
	7- The Flask component of the app will provide us with tools, libraries and technologies that allow to build the web application to display the retrieved data. 
	 
	 8- We will use  **HTML**, **CSS** and **Bootstrap 3**  languages to customize the web application to display the data in a neat and organized fashion

 


### Deliverable 1 Outputs

The screenshot of the web application displating the retrieved data (Figure 2) and the images of Mars Hemispheres are shown in Figure 3.

#### Figure 2: Screen-shot of the Website

-----------------

<p align="center">  
<img src="https://github.com/BHashemi2021/Mission-to-Mars/blob/main/Mars_Scraping/Resources/hemi1.png" width="75%" height="75%">
</p>

----------------- 



#### Figure 3: Mars Hemispheres

-----------------

<p align="center">  
<img src="https://github.com/BHashemi2021/Mission-to-Mars/blob/main/Mars_Scraping/Resources/hemispheres.png" width="75%" height="75%">
</p>


-----------------


URLS
 
-   https://mars.nasa.gov/news/
-   https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars
-   https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars















