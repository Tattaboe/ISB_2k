import argparse
import json
from methods.asymmetric import Asymmetric
from methods.symmetric import Symmetric
from methods.seri_deseri import *
from work_file import *


def save_paths_to_json(paths):
    """
    Save the paths dictionary to a JSON file.

    :param paths: Dictionary containing paths to be saved
    """
    try:
        with open('paths.json', 'w') as file:
            json.dump(paths, file)
    except Exception as e:
        print(f"Error save path to json {str(e)}")


def load_paths_from_json():
    """
    Load paths from a JSON file.

    :return: Loaded dictionary containing paths
    """
    try:
        with open('paths.json', 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error load paths from json {str(e)}")


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-gen", "--generation_symmetric", help="symmetric key generation", action="store_true")
    group.add_argument("-gen_a", "--generation_asymmetric", help="asymmetric key generation", action="store_true")
    group.add_argument("-enc", "--encryption_text", help="encryption text file", action="store_true")
    group.add_argument("-dec", "--decryption_text", help="decryption text file", action="store_true")
    group.add_argument("-enc_sym", "--encryption_symmetric_key", help="encryption symmetric key", action="store_true")
    group.add_argument("-dec_sym", "--decryption_symmetric_key", help="decryption symmetric key", action="store_true")

    parser.add_argument("-s_k", "--sym_key", help="Path for the symmetric key")
    parser.add_argument("-apu_k", "--asym_public_key", help="Path for the asymmetric public key")
    parser.add_argument("-apr_k", "--asym_private_key", help="Path for the asymmetric private key")
    parser.add_argument("-o_f", "--original_file", help="Path for the original text file")
    parser.add_argument("-e_f", "--encrypted_file", help="Path for the encrypted text file")
    parser.add_argument("-d_f", "--decrypted_file", help="Path for the decrypted text file")
    parser.add_argument("-ds_f", "--decrypted_sym_key", help="Path for the decrypted text file")
    parser.add_argument("-es_f", "--encrypted_sym_key", help="Path for the decrypted text file")

    args = parser.parse_args()
    symmetric = Symmetric(128)
    asymmetric = Asymmetric()

    paths = {key: getattr(args, key) for key in
             ["original_file", "encrypted_file", "decrypted_file", "sym_key", "decrypted_sym_key",
              "encrypted_sym_key", "asym_public_key", "asym_private_key"]}

    save_paths_to_json(paths)
    paths = load_paths_from_json()

    match args:
        case args if args.generation_symmetric:
            symmetric_key = symmetric.generate_key()
            ser_sym_key(paths["sym_key"], symmetric_key)

        case args if args.generation_asymmetric:
            public_key, private_key = asymmetric.generate_keys()
            ser_public_key(paths["asym_public_key"], public_key)
            ser_private_key(paths["asym_private_key"], private_key)

        case args if args.encryption_text:
            deser_sym_key(paths["sym_key"])
            encrypted_text = symmetric.encrypt_text_1(paths["original_file"], paths["encrypted_file"])
            print(f"Encrypted text: {encrypted_text}")

        case args if args.decryption_text:
            deser_sym_key(paths["sym_key"])
            decrypted_text = symmetric.decrypt_text_1(paths["encrypted_file"], paths["decrypted_file"])
            print(f"Decrypted text: {decrypted_text}")

        case args if args.encryption_symmetric_key:
            asymmetric.encrypt_2(paths["asym_public_key"], paths["sym_key"], paths["encrypted_sym_key"])

        case args if args.decryption_symmetric_key:
            asymmetric.decrypt_2(paths["encrypted_sym_key"], paths["asym_private_key"], paths["decrypted_sym_key"])


if __name__ == "__main__":
    main()
