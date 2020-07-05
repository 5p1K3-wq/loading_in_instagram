import requests
from pathlib import Path


def get_file_extension(image_url):
    return Path(image_url).suffix


def get_directory_images():
    image_dir = Path.cwd().joinpath('images')
    image_dir.mkdir(exist_ok=True)
    return image_dir


def save_images_in_directory(image_urls, file_name):
    current_dir_img = get_directory_images()
    for image_number, image_url in enumerate(image_urls):
        extension_file = get_file_extension(image_url)
        name = f'{file_name}_{image_number}.{extension_file}'
        path_where_to_save = Path(current_dir_img).joinpath(name)
        download_image(image_url, path_where_to_save)


def download_image(url, path_where_to_save):
    response = requests.get(url)
    response.raise_for_status()
    with open(path_where_to_save, 'wb') as image:
        image.write(response.content)