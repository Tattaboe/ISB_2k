
from work_file import read_json, write_text, read_columns_order_from_json, read_text


def vertical_rearrangement(path_key: str, text_to_encrypt: str) -> str:
    key = read_columns_order_from_json(path_key)
    max_number = max(key)
    table = ['' for _ in range(max_number)]
    text_to_encrypt = text_to_encrypt.replace(" ", "")

    for i, char in enumerate(text_to_encrypt):
        column = i % len(table)
        table[column] += char

    swapped_table = ['' for _ in range(len(table))]
    temp_table = table.copy()

    for i, column_index in enumerate(key):
        if column_index - 1 >= len(table):
            continue
        if column_index > i + 1:
            swapped_table[i] = temp_table[column_index - 1]
        else:
            swapped_table[i] = temp_table[column_index - 1]

    output_text = ' '.join([' '.join(column.split()) for column in swapped_table])
    return output_text


def main() -> None:
    paths = read_json("paths.json")
    if not paths:
        return

    path_t = paths.get("path_text_1")
    path_k = paths.get("path_key_1")
    path_e = paths.get("path_encryption_1")

    if path_t and path_k and path_e:
        text_to_encrypt = read_text(path_t)
        encrypted_text = vertical_rearrangement(path_k, text_to_encrypt)
        write_text(path_e, encrypted_text)


if __name__ == "__main__":
    main()
