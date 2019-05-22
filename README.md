# Airbnb Scraper
Completed for an exercise

Written in Python 2
(Compiled using 2.7.10)

## Dependencies

BeautifulSoup<br>
re<br>
requests<br>

## Solution

To begin, I looked at the source of one of the listings to gain an understanding of the structure of the page. From here I decided to add functionality incrementally - attempting to scrape the title first, checking for errors, then adding the others. I also downloaded the HTML of each page to work locally before changing the program to use live URLs. I also chose to use BeautifulSoup to scrape the pages. I looked at the title on the live page, and pasted this into a search to locate it within the source. I noticed a CSS class name that was non-descriptive but unique within a span tag. I looked at the source of another listing to see if the class name was the same. It was the same across each listing, so this would provide a reliable way to get the correct title.

I used a similar process to get the number of bedrooms and bathrooms, searching for another specific class, though this time using regex to get the right data from a larger string. Retrieving a list of amenities from the page was more challenging and required a different approach. I created a separate function that converted the page HTML to a string, and used regex to retrieve this data. This did not cause performance issues.

The program requests an URL to the Airbnb listing (live webpage) as user input and displays the retrieved data as a string within the terminal.

Tested with:

https://www.airbnb.co.uk/rooms/19278160?guests=1&adults=1&sl_alternate_dates_exclusion=true&source_impression_id=p3_1558560250_evzQ4wHgRihsgtP4&check_in=&check_out=&children=0&infants=0

https://www.airbnb.co.uk/rooms/1939240?guests=1&adults=1&sl_alternate_dates_exclusion=true&source_impression_id=p3_1558560254_fQHVfU32DxGDnBQL

https://www.airbnb.co.uk/rooms/14531512?guests=1&adults=1&sl_alternate_dates_exclusion=true&source_impression_id=p3_1558560761_9eLFptTcwI9V3iCa&check_in=&check_out=&children=0&infants=0

For testing purposes, I have also included the HTML files for each of the pages.
