import glob
import os
import images
from instabot import Bot
from PIL import Image


def upload_pictures_to_instagram(instagram_username, instagram_password, instagram_proxy):
    bot = Bot()
    bot.login(username=instagram_username, password=instagram_password, proxy=instagram_proxy)
    folder_path = images.get_directory_images()
    pics = glob.glob(str(folder_path)+'/*.jpg')
    pics = sorted(pics)
    for pic in pics:
        try:
            bot.upload_photo(pic)
            if bot.api.last_response.status_code != 200:
                print(bot.api.last_response)
        except Exception as e:
            print(str(e))

# Instagram requires a photo only with the extension jpg
def prepare_images_for_publicatioin():
    photo_extensions = ('jpg', 'gif', 'jpeg', 'png')
    max_width_img = 1080
    max_height_img = 1080
    extension_file = 'jpg'
    current_dir_images = images.get_directory_images()
    for dirpath, dirs, files in os.walk(current_dir_images):
        for file in files:
            extensions_current_file = images.get_file_extension(file)
            if extensions_current_file not in photo_extensions:
                continue

            if extensions_current_file == 'jpg':
                continue

            full_path_file = f'{dirpath}/{file}'
            image = Image.open(full_path_file)
            width, height = image.size
            mode = image.mode
            if width > max_width_img and height > max_height_img:
                image.thumbnail((max_width_img, max_height_img))

            name_file = file.split('.')[0]
            image = image.convert('RGB')
            image.save(f'{dirpath}/{name_file}.{extension_file}')
