import os
import math


from work_file import read_json


def frequency_bit_test(path: str, key: str) -> float:
    try:
        sub = read_json(path)
        n = len(sub)
        sum_xi = sum(-1 if bit == "0" else 1 for bit in sub.get(key))
        s_n = sum_xi / math.sqrt(n)
        p_v = math.erfc(math.fabs(s_n) / math.sqrt(2))
        return p_v
    except Exception as e:
        print("Error when performing a frequency bitwise test:", e)




if __name__ == "__main__":
    seq = read_json("paths.json")
    path_s = seq["sequences"]
    d = frequency_bit_test(path_s, "java")
    print(d)
