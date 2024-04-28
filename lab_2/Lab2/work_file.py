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


