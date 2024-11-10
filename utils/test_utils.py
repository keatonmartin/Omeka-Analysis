from utils import clean_html_entities, clean_html_tags, tokens

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