import instaloader
import re
import datetime


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
        drop_date = re.search('\d{2}/\d{2}/\d{4}', string).group(0)
        return [collab, drop_date]

    except Exception as e:
        print(f'Error formatting drop info: {e}')


def drop_has_happened(drop_date):
    return datetime.datetime.strptime(drop_date, '%m/%d/%Y') < datetime.datetime.now()


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
                collab, drop_date = format_drop_info(post.caption)
                if drop_has_happened(drop_date):
                    print('-' * len(collab))
                    print(
                        f'No drop has been scheduled for this week\nPrevious drop:\nCollab: {collab} \nDrop Date: {drop_date}')
                    print('-' * len(collab))
                else:
                    print('-' * len(collab))
                    print(f'Collab: {collab} \nDrop Date: {drop_date}')
                    print('-' * len(collab))
                break
    except Exception as e:
        print(f'Error extracting latest drop: {e}')


if __name__ == '__main__':
    check_drop_date()
