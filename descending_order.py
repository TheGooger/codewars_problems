def descending_order(num):
    reordered_num = sorted(str(num), reverse=True)
    return int(''.join(reordered_num))
