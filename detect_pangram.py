import string


def is_pangram(s):
    for char in string.ascii_lowercase:
        if char not in s.lower():
            return False
    return True
