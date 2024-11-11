import json
import requests

# given an item id, return the JSON response from the Omeka API
def get_item(id: int, key: str, url: str):
    r = requests.get(url + f"items/{id}?key={key}")
    return json.loads(r.text)

def get_all_tags(url: str):
    r = requests.get(url + "tags")
    return json.loads(r.text)

def get_tag(url: str, key: str, id: int):
    r = requests.get(url + f"tags/{id}?key={key}")
    return json.loads(r.text)

def create_item(url: str, key: str, payload: dict):
    r = requests.post(url + f"items?key={key}", json=payload)
    return json.loads(r.text)

def update_item(url: str, key: str, id: int, payload: dict):
    r = requests.put(url + f"items/{id}/?key={key}", json=payload)
    return json.loads(r.text)

def delete_tag(url: str, key: str, id: int):
    r = requests.delete(url + f"tags/{id}?key={key}")
    return json.loads(r.text)

# given an item id, add tag containing the text in tagContent
# returns False if item already contained tag with the same content
# otherwise, returns True if tag was successfully added
def add_tag_to_item(id: int, url: str, key: str, tagContent: str):

    # first, check if tag with same tag content already exists on item 
    item = get_item(id, key, url)

    for tag in item["tags"]:
        if tag["name"] == tagContent:
            return False
    
    # if it doesn't, we need to search through tags and check for existing tag
    tag_id = -1
    all_tags = get_all_tags(url)
    for tag in all_tags:
        if tag["name"] == tagContent:
            tag_id = int(tag["id"])

    # we did not find a matching existing tag, tag cannot be added
    if tag_id == -1: return False

    # else, we take the previous item returned by api and added a new tag to it
    item["tags"].append(get_tag(url, key, tag_id))
    update_item(url, key, id, item)
    
    return True
