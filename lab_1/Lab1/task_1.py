def find_max_number_in_key(key):
    max_number = max(key)
    return max_number


def distribute_text_in_table(text, key):
    table = ['' for _ in range(find_max_number_in_key(key))]
    text = text.replace(" ", "")
    for i, char in enumerate(text):
        column = i % len(table)
        table[column] += char

    return table


def swap_columns(table, key):
    swapped_table = ['' for _ in range(len(table))]
    temp_table = table.copy()

    for i, column_index in enumerate(key):
        if column_index - 1 >= len(table):
            continue
        if column_index > i + 1:
            swapped_table[i] = temp_table[column_index - 1]
        else:
            swapped_table[i] = temp_table[column_index - 1]

    return swapped_table




key = [5, 3, 8, 4, 6, 1, 9, 7, 2]  #Петербург
text = "Family is best friend for you"

table = distribute_text_in_table(text, key)
print("Source table:")
for i, column in enumerate(table):
    print(f"Column {i + 1}: {column}")

swapped_table = swap_columns(table, key)
print("\nTable after replacing columns by key:")
for i, column in enumerate(swapped_table):
    print(f"Column {key[i]}: {column}")
