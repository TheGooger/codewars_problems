def is_isogram(string):
    new_list = list(string.lower())
    for letter in new_list:
        if new_list.count(letter) > 1:
            return False
    return True


print(is_isogram('isogram'))