import json
import requests

# This file is currently defunct in that there's no (from my understanding)
# possible way to upload tags through the Omeka API

# given an item id, return the JSON response from the Omeka API
def get_item(id: int, url: str):
    r = requests.get(url + f"items/{id}")
    return json.loads(r.text)

def get_all_tags(url: str):
    r = requests.get(url + "tags")
    return json.loads(r.text)

# attempt to create a new tag object
def create_tag(url: str, payload: dict):
    r = requests.post(url + "tags", json=payload)
    print(r.text)

# TODO: auth
def create_item(url: str, payload: dict):
    r = requests.post(url + "items", json=payload)
    print(r.text)

# TODO: auth
def delete_tag(url: str, id: int):
    r = requests.delete(url + f"tags/{id}")
    print(r.text)

# given an item id, add tag containing the text in tagContent
# returns False if item already contained tag with the same content
# otherwise, returns True if tag was successfully added
def add_tag_to_item(id: int, url: str, tagContent: str):
    # first, check if tag with same tag content already exists on item 
    item = get_item(id, url)
    for tag in item["tags"]:
        if tag["name"] == tagContent:
            return False
    
    # if it doesn't, we need to search through tags and check for existing tag or create a new one
    tag_id = -1
    # perhaps extract this logic out of the function and perform on library load
    all_tags = get_all_tags(url)
    for tag in all_tags:
        if tag["name"] == tagContent:
            tag_id = int(tag["id"])

    # we did not find a matching existing tag, we need to create a new tag resource
    if tag_id == -1:
        tag_id = int(all_tags[-1]["id"]) + 1
        new_tag = json.dumps({
            "id" : tag_id,
            "url" : url + "/tags/" + str(tag_id),
            "name" : tagContent,
            "extended_resources" : []
        })
