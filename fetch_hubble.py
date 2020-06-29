import requests


def receive_images_from_collection(collection_name):
    url = f'http://hubblesite.org/api/v3/images/{collection_name}'
    response = requests.get(url)
    response.raise_for_status()
    contents = response.json()
    images_data = []
    for content in contents:
        image_id = content['id']
        url = fetch_hubble_image(image_id)
        images_data.append({
            'image_name': image_id,
            'url': f'https:{url}',
        })
    return images_data


def fetch_hubble_image(image_id):
    url = f'http://hubblesite.org/api/v3/image/{image_id}'
    response = requests.get(url)
    response.raise_for_status()
    contents = response.json()['image_files']
    last_element = -1
    image_url = contents[last_element]['file_url']
    return image_url