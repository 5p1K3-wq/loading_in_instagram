import requests
from pathlib import Path


def get_file_extension(link_file):
    return link_file.split('.')[-1]


def get_directory_images():
    current_dir = Path.cwd()
    image_dir = Path(current_dir, 'images')
    image_dir.mkdir(exist_ok=True)
    return image_dir


def save_images_in_directory(images, file_name):
    current_dir_img = get_directory_images()
    for image_number, image in enumerate(images):
        extension_file = get_file_extension(image)
        name = f'{file_name}_{image_number}.{extension_file}'
        path_where_to_save = current_dir_img / name
        download_image(image, path_where_to_save)


def download_image(url, path_where_to_save):
    response = requests.get(url)
    response.raise_for_status()
    with open(path_where_to_save, 'wb') as image:
        image.write(response.content)