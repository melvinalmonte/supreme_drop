import instaloader
import re


def has_drop_date(string):
    try:
        drop_date = re.findall('\d{2}/\d{2}/\d{4}', string)
        if drop_date:
            return True
        else:
            return False
    except ValueError:
        return False


def format_drop_info(string):
    try:
        collab = re.split('\d{2}/\d{2}/\d{4}', string)[0]
        drop_date = re.findall('\d{2}/\d{2}/\d{4}', string)[0]
        drop_info = f'Collab: {collab} \nDrop Date: {drop_date}'
        print('_' * len(drop_info))
        return drop_info

    except Exception as e:
        print(f'Error formatting drop info: {e}')


def check_drop_date():
    try:
        print('Instagram loader init...')
        insta = instaloader.Instaloader()

        instagram_account = "supremenewyork"

        print('Loading Supreme Instagram profile...')
        profile = instaloader.Profile.from_username(insta.context, instagram_account)
        print('Loaded Instagram profile...')

        print('Loading Supreme Instagram posts...')
        posts = profile.get_posts()
        print('Loaded Instagram posts...')

        print('Checking for latest drop...')
        for post in posts:
            if has_drop_date(post.caption):
                print(format_drop_info(post.caption))
                break
    except Exception as e:
        print(f'Error extracting latest drop: {e}')


if __name__ == '__main__':
    check_drop_date()
