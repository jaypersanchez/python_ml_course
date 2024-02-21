import requests
from bs4 import BeautifulSoup

# URL of the website
url = 'http://books.toscrape.com'

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Find all book titles on the page
for book in soup.find_all('h3'):
    title = book.find('a')['title']
    print(title)
