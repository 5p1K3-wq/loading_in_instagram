import argparse
import fetch_spacex
import fetch_hubble
import images
import upload_to_instagram


def main():
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("-u", type=str, help="username")
    parser.add_argument("-p", type=str, help="password")
    parser.add_argument("-proxy", type=str, help="proxy")
    args = parser.parse_args()

    images_spacex = fetch_spacex.fetch_spacex_last_launch()
    file_name = 'spacex'
    images.save_images_in_directory(images_spacex, file_name)

    image_id_hubble = 1
    images_hubble = fetch_hubble.fetch_hubble_images(image_id_hubble)
    images.save_images_in_directory(images_hubble, str(image_id_hubble))
    upload_to_instagram.prepare_images_for_publicatioin()
    upload_to_instagram.upload_pictures_to_instagram(args)


if __name__ == '__main__':
    main()