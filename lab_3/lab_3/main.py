import argparse

from methods.asymmetric import Asymmetric
from methods.symmetric import Symmetric
from methods.seri_deseri import *
from work_file import *


def main():

    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-gen", "--generation_symmetric", help="symmetric key generation"
    )
    group.add_argument(
        "-gen_a", "--generation_asymmetric", help="asymmetric key generation"
    )
    group.add_argument("-enc", "--encryption_text", help="encryption text file")
    group.add_argument("-dec", "--decryption_text", help="decryption text file")
    group.add_argument(
        "-enc_sym", "--encryption_symmetric_key", help="encryption symmetric key"
    )
    group.add_argument(
        "-dec_sym", "--decryption_symmetric_key", help="decryption symmetric key"
    )
    parser.add_argument(
        "setting", type=str, help="Path to the json file with the settings"
    )

    args = parser.parse_args()
    symmetric = Symmetric(128)
    asymmetric = Asymmetric()
    paths = read_json(args.setting)

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
            encrypted_text = symmetric.encrypt_text_1(
                paths["original_file"],
                paths["encrypted_file"]
            )
            print(f"Encrypted text: {encrypted_text}")

        case args if args.decryption_text:
            deser_sym_key(paths["sym_key"])
            decrypted_text = symmetric.decrypt_text_1(
                paths["encrypted_file"],
                paths["decrypted_file"]
            )
            print(f"Decrypted text: {decrypted_text}")

        case args if args.encryption_symmetric_key:
            asymmetric.encrypt_2(
                paths["asym_public_key"],
                paths["sym_key"],
                paths["encrypted_sym_key"],
            )

        case args if args.decryption_symmetric_key:
            asymmetric.decrypt_2(
                paths["encrypted_sym_key"],
                paths["asym_private_key"],
                paths["decrypted_sym_key"],
            )


if __name__ == "__main__":
    main()
