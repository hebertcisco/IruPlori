import ctypes
import random
import os

random = random.SystemRandom()

SPI_SETDESKWALLPAPER = 20


def changeBG(path):
    """Change background depending on bit size"""

    ctypes.windll.user32.SystemParametersInfoW(
        SPI_SETDESKWALLPAPER, 0, path, 3)


def get_background():
    """Returns a random background in data/backgrounds/"""

    background = random.choice(os.listdir('backgrounds'))

    return os.path.abspath(os.path.join(os.path.dirname(__file__), f'..\\backgrounds\\{background}'))
