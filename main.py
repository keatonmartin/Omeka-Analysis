import os
from dotenv import load_dotenv
import requests
import json
import utils
from api import *
from nltk.probability import FreqDist

URL = "https://drvk.createuky.net/news-articles/api/"
load_dotenv()
API_KEY = os.getenv("API_KEY")

def main():
    # create_tag(URL, {
    #     "id" : 276,
    #     "url" : URL + "/tags/276",
    #     "name" : "test",
    #     "extended_resources" : []
    # })
    delete_tag(URL, 276)
    


def gen_report():
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