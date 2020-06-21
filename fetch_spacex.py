import requests
import json


def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v3/launches/36'
    payload = {}
    headers = {}
    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()
    contents = json.loads(response.text)
    return contents['links']['flickr_images']