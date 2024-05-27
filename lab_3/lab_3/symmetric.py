import os

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from work_file import read_bytes, write_bytes_text, write_file


class Symmetric:
    def __init__(self):
        self.key_len = None

    def generate_key(self) -> bytes:
        return os.urandom(self.key_len // 8)

    def encrypt_text(self, path_text: str, encrypted_path: str) -> bytes:

        text = read_bytes(path_text)
        try:
            iv = os.urandom(8)
            cipher = Cipher(algorithms.Blowfish(self.key_len), modes.CBC(iv))
            encryptor = cipher.encryptor()
            padder = padding.PKCS7(128).padder()
            padded_text = padder.update(text) + padder.finalize()
            cipher_text = iv + encryptor.update(padded_text) + encryptor.finalize()
            write_bytes_text(encrypted_path, cipher_text)
            return cipher_text
        except Exception as e:
            print(f"Error in encryption - {e}")

    def decrypt_text(self, encrypted_path: str, decrypted_path: str) -> str:

        encrypted_text = read_bytes(encrypted_path)
        try:
            iv = encrypted_text[:8]
            encrypted_text = encrypted_text[8:]
            cipher = Cipher(algorithms.Blowfish(self.key_len), modes.CBC(iv))
            decryptor = cipher.decryptor()
            decrypted_text = decryptor.update(encrypted_text) + decryptor.finalize()
            unpadder = padding.PKCS7(128).unpadder()
            unpadded_dc_text =unpadder.update(decrypted_text) + unpadder.finalize()
            decrypted_text = unpadded_dc_text.decode('UTF-8')
            write_file(decrypted_path, decrypted_text)
            return decrypted_text
        except Exception as e:
            print(f"Error in decryption - {e}")

