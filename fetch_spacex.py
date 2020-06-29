import requests


def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v3/launches/latest'
    response = requests.get(url)
    response.raise_for_status()
    contents = response.json()['links']['flickr_images']
    return contents