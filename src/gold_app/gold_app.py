from serpapi import GoogleSearch
from environs import Env

env = Env()
env.read_env("./.env")

params = {
    "engine": "google",
    "google_domain": "google.com",
    "gl": "in",
    "hl": "en",
    "q": env("GOLD_QUESTION"),
    "api_key": env("SERPAPI_API_KEY")
}

def get_gold_price():
    try:
        search = GoogleSearch(params)
        result = search.get_dict()
        try:
            return result["organic_results"][0]["snippet"]
        except:
            return "Failed to extract the price"
    except:
        return "Failed to get the access to site"
    
