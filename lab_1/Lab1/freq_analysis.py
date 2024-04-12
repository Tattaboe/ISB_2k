
from work_file import read_json, write_text, read_text, write_json

def freq_analysis(path_text: str, path_freq_index: str) -> None:
    text = read_text(path_text)
    char_frequency = {}
    total_chars = len(text)

    for char in text:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    char_frequency_ratio = {char: count / total_chars for char, count in char_frequency.items()}
    sorted_char_frequency = dict(sorted(char_frequency_ratio.items(), key=lambda x: x[1], reverse=True))
    write_json(sorted_char_frequency, path_freq_index)

def main() -> None:
    paths = read_json("paths.json")
    path_text = paths.get("path_text_2")
    path_index = paths.get("path_index_2")
    freq_analysis(path_text, path_index)

main()
