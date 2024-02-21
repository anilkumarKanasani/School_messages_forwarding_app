import requests
from bs4 import BeautifulSoup

def get_gold_price():
    url = "https://www.grtjewels.com/"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    page = requests.get(url, headers=headers, verify=False, timeout=10)
    print(page.content)
    soup = BeautifulSoup(page.content, "html.parser")
    print(soup.prettify())
    rate_div = soup.find_all('div', class_='rate slide-rates')
    print(rate_div)
    rate_text = rate_div[0].text
    return rate_text 