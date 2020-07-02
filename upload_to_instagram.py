import images
from pathlib import Path
from instabot import Bot
from PIL import Image


def upload_pictures_to_instagram(instagram_username, instagram_password, instagram_proxy):
    bot = Bot()
    bot.login(username=instagram_username, password=instagram_password, proxy=instagram_proxy)
    images = Path.cwd().joinpath('images')
    currentPattern = '*.jpg'
    for image in images.glob(currentPattern):
        try:
            bot.upload_photo(image)
            if bot.api.last_response.status_code != 200:
                print(bot.api.last_response)
        except Exception as e:
            print(str(e))


def prepare_images_for_publicatioin():
    image_extensions = ('.jpg', '.gif', '.jpeg', '.png')
    max_width_img = 1080
    max_height_img = 1080
    extension_file = '.jpg'
    images_dir = images.get_directory_images()
    for path in images_dir.glob('*.*'):
        image_path = Path(path)
        image_extension = image_path.suffix
        if image_extension not in image_extensions:
            continue

        if image_extension == extension_file:
            continue

        image = Image.open(path)
        width, height = image.size
        if width < max_width_img and height < max_height_img:
            continue

        image.thumbnail((max_width_img, max_height_img))
        image = image.convert('RGB')
        image_name = image_path.name
        parent = image_path.parent
        image.save(Path(parent).joinpath(f'{image_name}{image_extension}'))




