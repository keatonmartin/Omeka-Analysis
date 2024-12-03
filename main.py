import os
from dotenv import load_dotenv
import requests
import json
import utils
import csv
from api import *
from nltk.probability import FreqDist

# main.py outputs an html file to be used on simple pages

URL = "https://drvk.createuky.net/news-articles/api/"
load_dotenv()
API_KEY = os.getenv("API_KEY")

def main():
    freqs = gen_freq().most_common()
    gen_csv()
    #add_tag_to_item(271, URL, API_KEY, "Mt. Sterling")
    with open("freq.html", "w") as f:
        f.write(gen_html_report(freqs, 20))

def gen_csv():
    freqs = gen_freq().most_common()
    
    with open('res.csv', 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['word', 'count'])
        writer.writeheader()
        for elem in freqs:
            word, count = elem
            writer.writerow({'word':word, 'count':count})

# expects an ordered list of word, frequency pairs like that which results from freqdist.most_common()
def gen_html_report(frequencies: list, n: int):
    wordToFreq = {}
    for word, freq in frequencies:
        wordToFreq[word] = freq;
    # generate html report containing top n most frequent words
    res =  f"<h3>This page displays the top {n} most frequent words appearing in every transcription contained in the Documenting Racial Violence in Kentucky project.</h3>"
    for i in range(n):
        word, freq = frequencies[i]
        res += f"<p><a href=\"https://drvk.createuky.net/news-articles/search?query={word}&query_type=exact_match\">{word}</a>: {freq}</p>"
    highlight_words = ['beast', 'fiend', 'brute', 'rapist', 'innocent', 'murderer', 'girl', 'judge', 'governor', 'trial', 'indecent', 'white', 'drunk', 'confession', 'tree', 'swing', 'bullet', 'woman', 'women', 'assault', 'wound', 'fight', 'farm', 'jailer', 'jail']
    res += "<h3> The following is a list of words deemed important by Dr. Nikki Brown, manager of the DRVK project.</h3>"
    for word in highlight_words:
        if word not in wordToFreq: continue
        res += f"<p><a href=\"https://drvk.createuky.net/news-articles/search?query={word}&query_type=exact_match\">{word}</a>: {wordToFreq[word]}</p>"
    return res
    
def gen_freq():
    r = requests.get(URL + "items")
    items = json.loads(r.text)

    descriptions = []
    for item in items:
        for text in item["element_texts"]:
            if text["element"]["name"] == "Description":
                descriptions.append(text["text"])
    
    combined = " ".join(descriptions)
    stopwords = ["one", "two"]
    tokens = utils.tokens(combined, stopwords)
    freq = FreqDist(tokens)
    return freq

if __name__ == '__main__':
    main()