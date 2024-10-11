import re
import html
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
nltk.download('punkt_tab')
nltk.download('punkt')


# clean_html_tags removes all sequences from a text of the form <...> 
def clean_html_tags(text: str) -> str:
    pattern = re.compile(r'<.*?>')
    return pattern.sub('', text)

# clean_html_entities replaces html entities like &nbsp; with their proper characters
def clean_html_entities(text: str) -> str:
    return html.unescape(text)

# tokens takes a text, cleans it for html tags and entities, 
# and returns a list of all words within the text
# not including punctuation or common english stopwords
# 
# a list of custom stopwords may be passed to stopwords
def tokens(text: str, stops: list = None):
    if stops == None:
        stops = []
    # clean text
    cleaned = clean_html_entities(clean_html_tags(text))
    
    # tokenize
    words = word_tokenize(cleaned)

    stopwords_list = stopwords.words("english")
    stopwords_list.extend(stops)

    # remove punctuation, make lower case, don't include stopwords
    return [word.lower() for word in words if (word.isalpha() and word.lower() not in stopwords_list)]

    

        
