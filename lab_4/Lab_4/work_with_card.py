import multiprocessing
import hashlib

from typing import List
from work_with_file import *


def get_card_num(hash_str: str, last_nums: str, bin_str: str) -> List[str]:

    valid_card_numbers = []
    for middle_num in range(0, 999999 + 1):
        card_num = f"{bin_str}{middle_num:06d}{last_nums}"
        if hashlib.sha3_256(card_num.encode()).hexdigest() == hash_str:
            valid_card_numbers.append(card_num)
    return valid_card_numbers


def find_num(hash_str: str, last_nums: str, bins: List[int], path_to: str) -> List[str]:
    ans = []
    args = [(hash_str, last_nums, str(bin_num)) for bin_num in bins]

    with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
        for res in pool.starmap(get_card_num, args):
            ans += res

    write_file(path_to, "\n".join(ans))

    return ans


def algorithm_luhn(card_num: str) -> bool:
    total_sum = 0
    second_elem = False

    for elem in reversed(card_num):
        elem = int(elem)

        if second_elem:
            elem *= 2
            if elem > 9:
                elem -= 9

        total_sum += elem
        second_elem = not second_elem

    return total_sum % 10 == 0
