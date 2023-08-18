import requests
from bs4 import BeautifulSoup

url = 'http://quotes.toscrape.com/'
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
quotes = soup.findAll('span')

output_file = open("scraped_quotes.txt", "w")

for quote in quotes[:-12]:
    quote_text = quote.text
    cleaned_text = quote_text.replace("(about)", "").strip()
    output_file.write(cleaned_text + "\n")

output_file.close()