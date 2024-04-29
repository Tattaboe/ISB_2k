import os
import math
import mpmath

from work_file import read_json, write_json

PI = {0: 0.2148, 1: 0.3672, 2: 0.2305, 3: 0.1875}


def frequency_bit_test(path: str, key_f: str) -> float:
    sub = read_json(path)
    try:
        x_i = [-1 if bit == "0" else 1 for bit in sub.get(key_f)]
        n = len(x_i)
        s_n = sum(x_i) / math.sqrt(n)
        p_v = math.erfc(math.fabs(s_n) / math.sqrt(2))
        return p_v
    except Exception as e:
        print(f"Error frequency_bit_test: {e}")


def identical_bit_test(path: str, key_i: str) -> float:
    sub = read_json(path)
    try:
        sequence = sub.get(key_i)
        n = len(sequence)

        numbers_units = sequence.count("1")
        share_units = numbers_units / n

        if abs(share_units - 0.5) > 2 / math.sqrt(n):
            return 0

        v_n = sum(1 for bit in range(n - 1) if sequence[bit] != sequence[bit + 1])

        num = abs(v_n - 2 * n * share_units * (1 - share_units))
        denom = 2 * math.sqrt(2 * n) * share_units * (1 - share_units)
        p_v = math.erfc(num / denom)
        return p_v

    except Exception as e:
        print(f"Error identical_bit_test: {e}")


def long_sequence_ones_test(path: str, key_l: str) -> float:
    sub = read_json(path)
    try:
        sequence = sub.get(key_l)
        n = len(sequence)
        m = 8

        blocks = [sequence[i:i + m] for i in range(0, n, m)]
        v = {1: 0, 2: 0, 3: 0, 4: 0}

        for block in blocks:
            max_ones = max(len(ones) for ones in "".join(block).split("0"))

            match max_ones:
                case 0 | 1:
                    v[1] += 1
                case 2:
                    v[2] += 1
                case 3:
                    v[3] += 1
                case _:
                    v[4] += 1
        xi_square = 0
        for i in range(4):
            xi_square += pow(v[i + 1] - 16 * PI[i], 2) / (16 * PI[i])
        p_v = mpmath.gammainc(1.5, xi_square / 2)
        return p_v

    except Exception as e:
        print(f"Error long_sequence_ones_test: {e}")


if __name__ == "__main__":
    seq = read_json("paths.json")
    path_s = seq["sequences"]
    path_r = seq["result"]

    results = {}
    keys = ["cpp", "java"]

    for key in keys:
        result_freq = frequency_bit_test(path_s, key)
        result_identical = identical_bit_test(path_s, key)
        result_long = long_sequence_ones_test(path_s, key)

        if result_freq is not None:
            results[key] = {
                "frequency_bit_test": result_freq,
                "identical_bit_test": result_identical,
                "long_sequence_ones_test": float(result_long)
            }

    write_json(results, path_r)


