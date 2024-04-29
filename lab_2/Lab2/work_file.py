import json


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



