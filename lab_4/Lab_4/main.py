
from work_with_card import *
from work_with_file import *


if __name__ == "__main__":

    consts = read_json("INFO.json")
    find_num(consts["hash"], consts["last_num"], consts["bins"], "card_num.txt")