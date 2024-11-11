from utils import clean_html_tags, tokens

# clean_html_tags

def test_clean_html_tags_remove():
    assert clean_html_tags("<h1>test</h1>") == "test"

def test_clean_html_tags_remove_fragment():
    assert clean_html_tags("<h1>test") == "test"

def test_clean_html_tags_no_change():
    assert clean_html_tags("test") == "test"

def test_clean_html_tags_keep_arrow():
    assert clean_html_tags("<test") == "<test"

def test_clean_html_tags_empty_string():
    assert clean_html_tags("") == ""

# tokens

sample_text = "<html><h1>The quick brown fox jumped over; the! lazy? dog.</h1></html>"

def test_tokens_removes_custom_stopword():
    res = tokens(sample_text, stops=['fox'])
    assert "fox" not in res
    
def test_tokens_removes_english_stopwords():
    res = tokens(sample_text)
    stopwords = {"the", "over"}
    assert not any([True if t in stopwords else False for t in res])

def test_tokens_contains_expected_tokens():
    res = tokens(sample_text)
    expected = ["quick", "brown", "fox", "lazy", "dog", "jumped"]
    assert all([True if e in res else False for e in expected])