# Airbnb Scraper
Completed for an exercise

Written in Python 2
(Compiled using 2.7.10)

## Dependencies

BeautifulSoup<br>
re<br>
requests<br>

## Solution

To begin, I looked at the source of one of the listings to gain an understanding of the structure of the page. From here I decided to add functionality incrementally - attempting to scrape the title first, checking for errors, then adding the others. I also chose to use BeautifulSoup to scrape the pages. I looked at the title on the live page, and pasted this into a search to locate it within the source. I noticed a CSS class name that was non-descriptive but unique within a span tag. I looked at the source of another listing to see if the class name was the same. It was the same across each listing, so this would provide a reliable way to get the correct title.

I used a similar process to get the number of bedrooms and bathrooms, searching for another specific class, though this time using regex to get the right data from a larger string. Retrieving a list of amenities from the page was more challenging and required a different approach. I created a separate function that converted the page HTML to a string, and used regex to retrieve this data. This did not cause performance issues.

The program displays the retrieved data as a string within the terminal.
