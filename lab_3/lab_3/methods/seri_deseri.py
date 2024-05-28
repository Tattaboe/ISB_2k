from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import load_pem_public_key, load_pem_private_key


def ser_sym_key(name: str, key_len: bytes) -> None:
    """
     Serialize a symmetric key to a file.

     Args:
         name (str): The file name to write the key to.
         key_len (bytes): The symmetric key to write.

     Raises:
         FileNotFoundError: If the file is not found.
         Exception: If an error occurs while writing the file.
     """

    try:
        with open(name, 'wb') as key_file:
            key_file.write(key_len)
        print(f"The symmetric key has been successfully written to the file '{name}'.")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"Error writing file {str(e)}")


def deser_sym_key(name: str) -> bytes:
    """
    Deserialize a symmetric key from a file.

    Args:
        name (str): The file name to read the key from.

    Returns:
        bytes: The deserialized symmetric key.

    Raises:
        FileNotFoundError: If the file is not found.
        Exception: If an error occurs while reading the file.
    """

    try:
        with open(name, "rb") as file:
            key_len = file.read()
            return key_len
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"Error writing file {str(e)}")


def ser_public_key(public_pem: str, public_key: rsa.RSAPublicKey) -> None:
    """
    Serialize a public key to a file.

    Args:
        public_pem (str): The file name to write the public key to.
        public_key (rsa.RSAPublicKey): The public key to write.

    Raises:
        FileNotFoundError: If the file is not found.
        Exception: If an error occurs while writing the file.
    """

    try:
        with open(public_pem, "wb") as public_out:
            public_out.write(
                public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo,
                )
            )
        print(f"The public key has been successfully written to the file '{public_pem}'.")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"Error: {str(e)}")


def ser_private_key(private_pem: str, private_key: rsa.RSAPrivateKey) -> None:
    """
    Serialize a private key to a file.

    Args:
        private_pem (str): The file name to write the private key to.
        private_key (rsa.RSAPrivateKey): The private key to write.

    Raises:
        FileNotFoundError: If the file is not found.
        Exception: If an error occurs while writing the file.
    """

    try:
        with open(private_pem, "wb") as private_out:
            private_out.write(
                private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.NoEncryption(),
                )
            )
            print(f"The private key has been successfully written to the file '{private_pem}'.")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"Error: {str(e)}")


def deser_public_key(public_pem: str) -> rsa.RSAPublicKey:
    """
    Deserialize a public key from a file.

    Args:
        public_pem (str): The file name to read the public key from.

    Returns:
        rsa.RSAPublicKey: The deserialized public key.

    Raises:
        FileNotFoundError: If the file is not found.
        Exception: If an error occurs while reading the file.
    """

    try:
        with open(public_pem, "rb") as pem_in:
            public_bytes = pem_in.read()
        deser_key = load_pem_public_key(public_bytes)
        return deser_key
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"Error: {str(e)}")


def deser_private_key(private_pem: str) -> rsa.RSAPrivateKey:
    """
    Deserialize a private key from a file.

    Args:
        private_pem (str): The file name to read the private key from.

    Returns:
        rsa.RSAPrivateKey: The deserialized private key.

    Raises:
        FileNotFoundError: If the file is not found.
        Exception: If an error occurs while reading the file.
    """

    try:
        with open(private_pem, "rb") as pem_in:
            private_bytes = pem_in.read()
        deser_key = load_pem_private_key(
            private_bytes,
            password=None,
        )
        return deser_key
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"Error: {str(e)}")

