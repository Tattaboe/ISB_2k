import json


def read_text(name: str) -> str:
    try:
        with open(name, 'r', encoding='utf-8') as file:
            data = file.read()
            return data
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return f"Error reading file: {str(e)}"


def write_text(name: str, data: str) -> None:
    try:
        with open(name, 'w', encoding='utf-8') as file:
            file.write(data)
        return None
    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print(f"Error writing to file: {str(e)}.")


def read_json(name: str) -> dict:
    try:
        with open(name, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("File not found")
    except Exception as e:
        print(f"Error reading file {str(e)}")


def read_columns_order_from_json(file_path: str) -> list:
    with open(file_path, 'r') as file:
        data = json.load(file)
        columns_order = data.get("columns_order", [])
    return columns_order



