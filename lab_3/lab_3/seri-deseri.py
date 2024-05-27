import os


def ser_sym_key(name: str, key_len: bytes) -> None:
    try:
        with open(name, 'wb') as key_file:
            key_file.write(key_len)
        print(f"The symmetric key has been successfully written to the file '{name}'.")
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"Error writing file {str(e)}")


def deser_sym_key(name: str) -> bytes:
    try:
        with open(name, "rb") as file:
            key_len = file.read()
            return key_len
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"Error writing file {str(e)}")


