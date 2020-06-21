import requests
import json

def fetch_hubble_images(image_id):
    url = f'http://hubblesite.org/api/v3/image/{image_id}'
    response = requests.get(url)
    response.raise_for_status()
    contents = json.loads(response.text)['image_files']
    images = []
    for content in contents:
        images.append(f'https:{content["file_url"]}')
    return images