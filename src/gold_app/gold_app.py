import requests
from bs4 import BeautifulSoup

# get todays date
from datetime import date


def get_gold_price():
    url = 'https://www.indiagoldrate.co.in/'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        gold_rate_tag = soup.find('th', text='22K Gold').find_next('td').find_next('td')
        
        if gold_rate_tag:
            gold_rate = gold_rate_tag.text
        else:
            gold_rate = None
    else:
        gold_rate = None
    print("Gold rate is: ", gold_rate)
    return str(date.today()) + " gold rate is " + gold_rate 
