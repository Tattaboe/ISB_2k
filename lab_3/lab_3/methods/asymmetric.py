from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from work_file import *
from methods.seri_deseri import *


class Asymmetric:
    """
    Class for working with asymmetric encryption.
    """
    def __init__(self):
        """
        Initializes an object of the Asymmetric class.
        """
        self.private_key = None
        self.public_key = None

    def generate_keys(self) -> tuple[rsa.RSAPublicKey, rsa.RSAPrivateKey]:
        """
        Generates RSA public and private keys.

        Returns:
             tuple[rsa.RSAPublicKey, rsa.RSAPrivateKey]: Public and private RSA keys.
        """
        keys = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        self.private_key = keys
        self.public_key = keys.public_key()
        return self.public_key, self.private_key

    def encrypt_2(self, public_key_path: str, sym_key_path: str, encrypted_sym_key_path: str) -> None:
        """
        Encrypts a symmetric key using a public key.

        Args:
            public_key_path (str): Path to the file containing the public key.
            sym_key_path (str): Path to the file containing the symmetric key.
            encrypted_sym_key_path (str): Path to save the encrypted symmetric key.

        Raises:
            RuntimeError: If there is an error encrypting the symmetric key.
        """
        try:
            sym_key = deser_sym_key(sym_key_path)
            public_key = deser_public_key(public_key_path)
            encrypted_sym_key = public_key.encrypt(sym_key,
                                                   padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                                algorithm=hashes.SHA256(), label=None))
            write_bytes_text(encrypted_sym_key_path, encrypted_sym_key)

        except Exception as e:
            raise RuntimeError(f"Failed to encrypt symmetric key with public key: {e}")

    def decrypt_2(self, encrypted_sym_key_path: str, private_key_path: str, decrypted_sym_key_path: str) -> bytes:
        """
        Decrypts an encrypted symmetric key using a private key.

        Args:
            encrypted_sym_key_path (str): Path to the file containing the encrypted symmetric key.
            private_key_path (str): Path to the file containing the private key.
            decrypted_sym_key_path (str): Path to save the decrypted symmetric key.

        Returns:
            bytes: The decrypted symmetric key.

        Raises:
            RuntimeError: If there is an error decrypting the symmetric key.
        """
        try:
            encrypted_sym_key = deser_sym_key(encrypted_sym_key_path)
            private_key = deser_private_key(private_key_path)
            decrypted_sym_key = private_key.decrypt(encrypted_sym_key,
                                                    padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                                 algorithm=hashes.SHA256(), label=None))

            ser_sym_key(decrypted_sym_key_path, decrypted_sym_key)
            return encrypted_sym_key
        except Exception as e:
            raise RuntimeError(f"Failed to decrypt symmetric key: {e}")
