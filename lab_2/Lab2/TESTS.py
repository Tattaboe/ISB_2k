import os
import math
from work_file import read_json, write_json


def frequency_bit_test(path: str, key_f: str) -> float:
    try:
        sub = read_json(path)
        sum_xi = [-1 if bit == "0" else 1 for bit in sub.get(key_f)]
        n = len(sum_xi)
        s_n = sum(sum_xi) / math.sqrt(n)
        p_v = math.erfc(math.fabs(s_n) / math.sqrt(2))
        return p_v
    except Exception as e:
        print(f"Error frequency_bit_test: {e}")


if __name__ == "__main__":
    seq = read_json("paths.json")
    path_s = seq["sequences"]
    path_r = seq["result"]

    results = {}
    keys = ["cpp", "java"]

    for key in keys:
        result = frequency_bit_test(path_s, key)
        if result is not None:
            results[key] = result

    write_json(results, path_r)