from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes


class Asymmetric:

    def __init__(self):
        self.private_key = None
        self.public_key = None

    def generate_keys(self) -> None:

        keys = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        self.private_key = keys
        self.public_key = keys.public_key()

    def encrypt_text_2(self, sym_key: bytes) -> bytes:

        encrypted_sym_key = self.public_key.encrypt(sym_key,
                                                    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                                 algorithm=hashes.SHA256(), label=None))
        return encrypted_sym_key

    def decrypt_text_2(self, sym_key: bytes) -> bytes:

        decrypted_sym_key = self.private_key.decrypt(sym_key,
                                                     padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                                  algorithm=hashes.SHA256(), label=None))
        return decrypted_sym_key

