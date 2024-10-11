import os
from dotenv import load_dotenv
import requests
import json
import utils
from nltk.probability import FreqDist

URL = "https://drvk.createuky.net/news-articles/api/items"
load_dotenv()
API_KEY = os.getenv("API_KEY")

def main():
    r = requests.get(URL)
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
    for word, f in freq.most_common():
        print(f"{word}: {f}")




if __name__ == '__main__':
    main()