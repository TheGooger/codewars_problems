def get_middle(word):
    if len(word) % 2 == 0:
        mid_index = len(word) / 2
        return word[int(mid_index) - 1: int(mid_index) + 1]
    else:
        mid_index = len(word) // 2 + 1
        return word[mid_index - 1]


print(get_middle("abcd"))