# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt
from webdriver_manager.chrome import ChromeDriverManager


def scrape_all():
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    news_title, news_paragraph = mars_news(browser)


# Scrape Mars News
def mars_news(browser):
    
    # Visit the Mars NASA news site
    url = 'https://data-class-mars.s3.amazonaws.com/Mars/index.html'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('div.list_text')
        # Use the parent element to find the first 'a' tag and save it as 'news_title'
        news_title = slide_elem.find('div', class_='content_title').get_text()
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

    except AttributeError:
        return None, None

    return news_title, news_p


# Scrape NASA News Featured Image
def featured_image(browser):
    # Visit URL
    url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    time.sleep(1)
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    # ! full_image_elem = browser.find_by_tag('button')[0]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None

    # Use the base url to create an absolute url
    img_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{img_url_rel}'

    return img_url


def mars_facts():
    # Add try/except for error handling
    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('https://data-class-mars-facts.s3.amazonaws.com/Mars_Facts/index.html')[0]

    except BaseException:
        return None

    # Assign columns and set index of dataframe
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)

    # Convert dataframe into HTML format, add bootstrap
    return df.to_html(classes="table table-striped")

   
# ! hemispheric codes start from here
# Scrape hemispheres data
    browser.visit('https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars')
    
    time.sleep(1)
    
    # Scrape page into Soup
    html = browser.html
    soup = bs(html, 'html.parser')

    hemi_names = []

    # Search for the names of all four hemispheres
    results = soup.find_all('div', class_="collapsible results")
    hemispheres = results[0].find_all('h3')

    # Get text and store in list
    for name in hemispheres:
        hemi_names.append(name.text)

    # Search for thumbnail links
    thumbnail_results = results[0].find_all('a')
    thumbnail_links = []

    # Iterate through thumbnail links for full-size image
    for thumbnail in thumbnail_results:
        
        # If the thumbnail element has an image 
        if (thumbnail.img):
            
            # then retrieve the attached link
            thumbnail_url = 'https://astrogeology.usgs.gov/' + thumbnail['href']
            
            # Append list with links
            thumbnail_links.append(thumbnail_url)
    
    full_imgs = []

    for url in thumbnail_links:
        
        # Click through each thumbanil link
        browser.visit(url)
        
        html = browser.html
        soup = bs(html, 'html.parser')
        
        # Scrape each page for the relative image path
        results = soup.find_all('img', class_='wide-image')
        relative_img_path = results[0]['src']
        
        # Combine the reltaive image path to get the full url
        img_link = 'https://astrogeology.usgs.gov/' + relative_img_path
        
        # Add full image links to a list
        full_imgs.append(img_link)

    # Zip together the list of hemisphere names and hemisphere image links
    mars_hemi_zip = zip(hemi_names, full_imgs)

    hemisphere_image_urls = []

    # Iterate through the zipped object
    for title, img in mars_hemi_zip:
        
        mars_hemi_dict = {}
        
        # Add hemisphere title to dictionary
        mars_hemi_dict['title'] = title
        
        # Add image url to dictionary
        mars_hemi_dict['img_url'] = img
        
        # Append the list with dictionaries
        hemisphere_image_urls.append(mars_hemi_dict)
    


    # Run all scraping functions and store results in a dictionary
    mars_data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now(),
        "hemispheres": hemisphere_image_urls
    }

    # ! Stop webdriver and return data
    browser.quit()

# if __name__ == "__main__":

    # Return results
    mars_data


