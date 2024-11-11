import os
from dotenv import load_dotenv
import requests
import json
import utils
from api import *
from nltk.probability import FreqDist

# main.py outputs an html file to be used on simple pages

URL = "https://drvk.createuky.net/news-articles/api/"
load_dotenv()
API_KEY = os.getenv("API_KEY")

def main():
    add_tag_to_item(271, URL, API_KEY, "Lexington")
    pass
    
def gen_freq():
    r = requests.get(URL + "items")
    items = json.loads(r.text)

    descriptions = []
    for item in items:
        for text in item["element_texts"]:
            if text["element"]["name"] == "Description":
                descriptions.append(text["text"])
    
    combined = " ".join(descriptions)
    tokens = utils.tokens(combined)
    print(f"{len(tokens)} words")

    freq = FreqDist(tokens)
    return freq

if __name__ == '__main__':
    main()