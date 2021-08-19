# Import Splinter and BeautifulSoup
# Import dependencies
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Set up Splinter (executable path & URL for scraping)
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# ### NASA News Titles and Paragraphs

def mars_news(browser):
    
    # Visit the mars nasa news site
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Set up HTML parser
    html = browser.html
    news_soup = soup(html, 'html.parser')
    
    # Try/except for error handling
    try:
        slide_elem = news_soup.select_one('div.list_text')
        # Scrape content title
        slide_elem.find('div', class_='content_title')

        # Use the parent element to find the first <a> tag and save it as  `news_title`
        news_title = slide_elem.find('div', class_='content_title').get_text()

        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
   
    except AttributeError:
        return None, None
    
    # Return
    return news_title, news_p

# ### JPL Space Featured Image

def featured_image(browser):

    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')
    
    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
    
    except AttributeError:
        return None
        
    # Use the base URL to create an absolute URL
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'
    
    # Return
    return img_url

# ### Mars Fact Table

def mars_facts():

    try:
        # Use pandas to read the data (instead of scraping each row)
        df = pd.read_html('https://galaxyfacts-mars.com')[0]
    except BaseException:
        return None

    # Assign columns and set index of DataFrame
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)

    # Convert DataFrame to HTML-ready code
    return df.to_html()

# Close automated browsing session
browser.quit()
