# scrape https://www.lalithaajewellery.com/
import requests
from bs4 import BeautifulSoup

def get_gold_price():
    try:
        url = "https://www.grtjewels.com/"
        page = requests.get(url)
        soup = BeautifulSoup(page.content, "html.parser")
        rate_div = soup.find_all('div', class_='rate slide-rates')
        rate_text = rate_div[0].text
        return rate_text 
    except:
        return "Error in fetching."