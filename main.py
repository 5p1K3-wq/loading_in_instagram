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

    current_images_directory = images.get_directory_images()
    collection_hubble_name = 'holiday_cards'
    images_data = fetch_hubble.receive_images_from_collection(collection_hubble_name)
    for image_numerator, image_data in enumerate(images_data):
        image_name = image_data['image_name']
        url = image_data['url']
        extension_image = images.get_file_extension(url)
        name = f'{image_name}_{image_numerator}.{extension_image}'
        full_name = current_images_directory / name
        images.download_image(url, full_name)

    upload_to_instagram.prepare_images_for_publicatioin()
    upload_to_instagram.upload_pictures_to_instagram(args.u, args.p, args.proxy)


if __name__ == '__main__':
    main()
