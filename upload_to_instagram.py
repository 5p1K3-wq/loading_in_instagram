import glob
import os
import images
from instabot import Bot
from PIL import Image


def upload_pictures_to_instagram(args):
    bot = Bot()
    bot.login(username=args.u, password=args.p, proxy=args.proxy)
    folder_path = images.get_directory_images()
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


def prepare_images_for_publicatioin():
    INCL_EXTS = ('jpg', 'gif', 'jpeg', 'png')
    MAX_WIDTH_IMG = 1080
    MAX_HEIGHT_IMG = 1080
    EXTENSION_FILE = 'jpg'
    current_dir_images = images.get_directory_images()
    for dirpath, dirs, files in os.walk(current_dir_images):
        for file in files:
            extensions_file = images.get_file_extension(file)
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