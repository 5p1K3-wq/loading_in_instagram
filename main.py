import requests
import json
import os
import glob
import argparse
from pathlib import Path
from PIL import Image
from instabot import Bot


def prepare_images_for_publicatioin():
    INCL_EXTS = ('jpg', 'gif', 'jpeg', 'png')
    MAX_WIDTH_IMG = 1080
    MAX_HEIGHT_IMG = 1080
    EXTENSION_FILE = 'jpg'
    current_dir_images = get_directory_images()
    for dirpath, dirs, files in os.walk(current_dir_images):
        for file in files:
            extensions_file = get_file_extension(file)
            if extensions_file in INCL_EXTS:
                full_path_file = f'{dirpath}/{file}'
                image = Image.open(full_path_file)
                width, height = image.size
                if width > MAX_WIDTH_IMG and height > MAX_HEIGHT_IMG:
                    image.thumbnail((MAX_WIDTH_IMG, MAX_HEIGHT_IMG))
                    if extensions_file != EXTENSION_FILE:
                        name_file = file.split('.')
                        image.save(f'{dirpath}/{name_file}.{EXTENSION_FILE}')
                    else:
                        image.save(full_path_file)


def upload_pictures_to_instagram(args):
    bot = Bot()
    bot.login(username=args.u, password=args.p, proxy=args.proxy)
    folder_path = get_directory_images()
    pics = glob.glob(str(folder_path)+'/*.jpg')
    pics = sorted(pics)
    try:
        for pic in pics:
            pic_name = pic.split('.')[0]
            print("upload: " + pic_name)
            bot.upload_photo(pic)
            if bot.api.last_response.status_code != 200:
                print(bot.api.last_response)
    except Exception as e:
        print(str(e))


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


def fetch_spacex_last_launch():
    url = 'https://api.spacexdata.com/v3/launches/36'
    payload = {}
    headers = {}
    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()
    contents = json.loads(response.text)
    return contents['links']['flickr_images']


def fetch_hubble_images(image_id):
    url = f'http://hubblesite.org/api/v3/image/{image_id}'
    response = requests.get(url)
    response.raise_for_status()
    contents = json.loads(response.text)['image_files']
    images = []
    for content in contents:
        images.append(f'https:{content["file_url"]}')
    return images


def main():
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("-u", type=str, help="username")
    parser.add_argument("-p", type=str, help="password")
    parser.add_argument("-proxy", type=str, help="proxy")
    args = parser.parse_args()

    images_spacex = fetch_spacex_last_launch()
    file_name = 'spacex'
    save_images_in_directory(images_spacex, file_name)

    image_id_hubble = 1
    images_hubble = fetch_hubble_images(image_id_hubble)
    save_images_in_directory(images_hubble, str(image_id_hubble))
    prepare_images_for_publicatioin()
    upload_pictures_to_instagram(args)


if __name__ == '__main__':
    main()