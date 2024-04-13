from work_file import read_json, write_text, read_text, write_json
import os


def freq_analysis(path_text: str, path_freq_index: str) -> None:
    if not os.path.exists(path_text):
        print(f"Ошибка: Файл '{path_text}' не найден.")
        return

    text = read_text(path_text)
    char_frequency = {}
    total_chars = len(text)

    for char in text:
        char_frequency[char] = char_frequency.get(char, 0) + 1

    char_frequency_ratio = {char: count / total_chars for char, count in char_frequency.items()}
    sorted_char_frequency = dict(sorted(char_frequency_ratio.items(), key=lambda x: x[1], reverse=True))

    write_json(sorted_char_frequency, path_freq_index)
    print(f"Анализ частот символов завершен. Результат сохранен в '{path_freq_index}'.")


def decrypt_text(path_text: str, path_freq: str, path_original_freq: str) -> str:
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
            decrypted_text += char  # сохраняем символ, если нет соответствия

    combined_map = {enc_char: decryption_map.get(enc_char, '?') for enc_char in enc_frequencies}
    paths = read_json("paths.json")
    output_path = paths.get("path_index_3")
    write_json(combined_map, output_path)


    return decrypted_text


def decrypt_text_2(path_key: str, input_path: str, output_path: str) -> str:

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
    if paths is None:
        print("Ошибка: Не удалось прочитать файл JSON.")
        return

    path_text = paths.get("path_text_2")
    path_index = paths.get("path_index_2")
    freq_analysis(path_text, path_index)

    path_t = paths.get("path_text_2")
    path_e = paths.get("path_index_2")
    path_o = paths.get("path_index_1")
    path_l = paths.get("path_index_3")
    if path_e is None or path_o is None:
        print("Ошибка: Не удалось получить пути к файлам с частотами.")
        return

    decrypted_text = decrypt_text(path_t, path_e, path_o)
    output_path = paths.get("dec_text")
    write_text(output_path, decrypted_text)
    decrypt_text_2(path_l,output_path,path_text)


main()
