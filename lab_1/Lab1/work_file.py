import json


def read_text(name: str) -> str:
    """
    Read text data from a file.

    Args:
        name (str): The path to the file to read.

    Returns:
        str: The text data read from the file.
    """
    try:
        with open(name, 'r', encoding='utf-8') as file:
            data = file.read()
            return data
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return f"Error reading file: {str(e)}"


def write_text(name: str, data: str) -> None:
    """
    Write text data to a file.

    Args:
        name (str): The path to the file to write to.
        data (str): The text data to write to the file.
    """
    try:
        with open(name, 'w', encoding='utf-8') as file:
            file.write(data)
        return None
    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print(f"Error writing to file: {str(e)}.")


def read_json(name: str) -> dict:
    """
    Read JSON data from a file.

    Args:
        name (str): The path to the JSON file to read.

    Returns:
        dict: The JSON data read from the file.
    """
    try:
        with open(name, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"Error reading file {str(e)}")


def read_columns_order_from_json(file_path: str) -> list:
    """
    Read columns order from a JSON file.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        list: The list of column orders.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            columns_order = data.get("columns_order", [])
        return columns_order
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"Error reading file {str(e)}")


def write_json(data: dict, path: str) -> None:
    """
    Write JSON data to a file.

    Args:
        data (dict): The JSON data to write.
        path (str): The path to the file to write to.
    """
    try:
        with open(path, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=1)
            print(f"The data has been successfully written to the file '{path}'.")
    except Exception as e:
        print(f"Error writing to the file: '{e}'.")
