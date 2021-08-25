# Mission-to-Mars
Module 10 Challenge Data Analysis File Links
- ![Mission_to_Mars_Challenge.ipynb](https://github.com/aseo67/Mission-to-Mars/blob/main/Mission_to_Mars_Challenge.ipynb)
- ![scraping.py](https://github.com/aseo67/Mission-to-Mars/blob/main/scraping.py)
- ![app.py](https://github.com/aseo67/Mission-to-Mars/blob/main/app.py)
- ![index.html](https://github.com/aseo67/Mission-to-Mars/blob/main/templates/index.html)

## Overview of Mission-to-Mars Analysis
This analysis compiles information, news and images regarding Mars into one convenient location. By scraping web data using Splinter and BeatifulSoup and storing data in MongoDB, this analysis will display the results on a web application, that also is able to scrape new data and update the page with a click of a button. 

## Summary
### Deliverable 1
In addition to the code for scraping recent news about Mars, a facts table comparing Mars vs. Earth, and a featured image, further code has been added to scrape and store Mars Hemisphere Images. The corresponding titles and URLs for the 4 hemispheres were retrieved. 

  ![Screenshot](https://github.com/aseo67/Mission-to-Mars/blob/main/Screenshot_Challenge_Image%20URLs.png)
 
### Deliverable 2
The web app has also been updated to include the newly scraped Mars Hemisphere images and titles, by updating the scraping.py file, updating the Mongo database holding the scraped data, and updating the index.html file to display the info. 

  ![scraping.py](https://github.com/aseo67/Mission-to-Mars/blob/main/scraping.py)
  ![index.html](https://github.com/aseo67/Mission-to-Mars/blob/main/templates/index.html)
  
  ![Screenshot](https://github.com/aseo67/Mission-to-Mars/blob/main/Screenshot_MongoDB.png)
  
### Deliverable 3
Finally, the web app was modified to be mobile-responsive and customized in appearance.  
- To accommodate multiple device displays, the code has been adjusted for both desktop monitors and smaller screens, ensuring that the images and fact table will adjust accordingly for the smaller screens. 
- Furthermore, the fact table has been adjusted to allow horizontal scrolling for smaller screens, to ease readability. 


  ![Screenshot](https://github.com/aseo67/Mission-to-Mars/blob/main/Screenshot_Challenge_Final_iPad%20ver.png)
  ![Screenshot](https://github.com/aseo67/Mission-to-Mars/blob/main/Screenshot_Challenge_Final_iPhoneX%20ver.png)

- The Scrape button has been customized to have bolded font, and display a light blue color. 
- The Mars Fact table has been customized to be in a striped-table format. 
- The Hemispheres images have been displayed as thumbnails. 

The final web page is screenshotted below.

  ![Screenshot](https://github.com/aseo67/Mission-to-Mars/blob/main/Screenshot_Challenge_Final.png)
  
