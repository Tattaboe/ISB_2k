
from work_with_card import *
from work_with_file import *


if __name__ == "__main__":

    consts = read_json("INFO.json")

    data_str = read_file("time.txt")
    data = [float(item) for item in data_str.split() if item.replace(".", "", 1).isdigit()]
    print(data)

    graph(data, "graph.png")