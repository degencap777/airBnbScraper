from bs4 import BeautifulSoup
import re, requests

# Prints scraped data
def print_listing(listing):
    for i in listing:
        print(i)

# Get amenities from the listing
def get_amenities(soup):
    # Whole page to string
    listing_html = str(soup)

    # Search html for unformatted string containing amenities
    amenities_unformatted = re.search('\[\{\"category\"\:\"[a-zA-Z]*\"\,\"amenities\"\:\"[a-zA-Z", 0-9\}]*', listing_html).group(0)

    # Get amenities
    amenities = re.search('[A-Z][a-z]*\,[a-zA-Z \,0-9]*', amenities_unformatted).group(0)

    return amenities

# Get property name, type, num. of bedrooms and bathrooms
def get_info(soup):
    # Contains scraped listing data
    listing = []

    property_name = soup.find("span", {"class": "_18hrqvin"}).get_text()

    property_type = soup.find("a", {"class": "_10k87om"}).get_text()

    # Get other listing info as string
    listing_info = str(soup.findAll("div", {"class": "_czm8crp"}))

    num_beds = re.search("\d+ bed", listing_info).group(0)
    num_baths = re.search("\d+ bath", listing_info).group(0)

    listing.append(property_name)
    listing.append(property_type)
    listing.append(num_beds)
    listing.append(num_baths)
    listing.append(get_amenities(soup))

    return listing

print("Airbnb Listing Scraper")
print("")
print("Please enter a listing URL: ")
url = raw_input()
print("")


# Get listing webpage
listing_page = requests.get(url)

soup = BeautifulSoup(listing_page.text, "html.parser")

listing = get_info(soup)

# Print the listing info
print_listing(listing)
