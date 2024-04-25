import os

from work_file import read_json, write_text, read_text, write_json


def freq_analysis(path_text: str, path_freq_index: str) -> None:
    """
        Perform frequency analysis on the text and save the sorted character frequencies to a JSON file.

        Args:
            path_text (str): Path to the text file for frequency analysis.
            path_freq_index (str): Path to save the sorted character frequencies.

        Returns:
            None
        """
    text = read_text(path_text)
    char_frequency = {}
    total_chars = len(text)

    for char in text:
        char_frequency[char] = char_frequency.get(char, 0) + 1

    char_frequency_ratio = {char: count / total_chars for char, count in char_frequency.items()}
    sorted_char_frequency = dict(sorted(char_frequency_ratio.items(), key=lambda x: x[1], reverse=True))

    write_json(sorted_char_frequency, path_freq_index)
    print(f"Symbol frequency analysis is complete. The result is saved in '{path_freq_index}'.")


def decrypt_text(path_text: str, path_freq: str, path_original_freq: str) -> str:
    """
        Decrypt the text using frequency analysis and provided frequency maps.

        Args:
            path_text (str): Path to the text file to decrypt.
            path_freq (str): Path to the encrypted character frequencies JSON file.
            path_original_freq (str): Path to the original character frequencies JSON file.

        Returns:
            str: Decrypted text.
        """
    text = read_text(path_text)
    enc_frequencies = read_json(path_freq)
    original_frequencies = read_json(path_original_freq)
    decryption_map = {}

    for enc_char, orig_char in zip(enc_frequencies, original_frequencies):
        decryption_map[enc_char] = orig_char

    decrypted_text = ''
    for char in text:
        if char in decryption_map:
            decrypted_text += decryption_map[char]
        else:
            decrypted_text += char

    combined_map = {enc_char: decryption_map.get(enc_char, '?') for enc_char in enc_frequencies}
    paths = read_json("paths.json")
    output_path = paths.get("dec_key")
    write_json(combined_map, output_path)

    return decrypted_text


def decrypt_text_2(path_key: str, input_path: str, output_path: str) -> None:
    """
      Decrypt the text using a provided key and save the result to a file.

      Args:
          path_key (str): Path to the key JSON file for decryption.
          input_path (str): Path to the text file to decrypt.
          output_path (str): Path to save the decrypted text.

      Returns:
          None
      """
    key = read_json(path_key)
    result = ''
    text = read_text(input_path)

    for char in text:
        if char in key:
            result += key[char]
        else:
            result += char
    write_text(output_path, result)


def main() -> None:
    paths = read_json("paths.json")
    path_t2 = paths.get("path_text_2")
    path_i2 = paths.get("path_index_2")
    freq_analysis(path_t2, path_i2)

    path_i1 = paths.get("path_index_1")
    path_key = paths.get("key")
    path_final = paths.get("text")

    decrypted_text = decrypt_text(path_t2, path_i2, path_i1)
    output_path = paths.get("dec_text")
    write_text(output_path, decrypted_text)
    decrypt_text_2(path_key, path_t2, path_final)


main()
