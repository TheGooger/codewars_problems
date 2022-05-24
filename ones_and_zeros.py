def binary_array_to_number(arr):
    i = 1
    res = 0
    for el in arr:
        res += el * pow(2, len(arr) - i)
        i += 1
    return res

"""
return int("".join(map(str, arr)), 2)
"""