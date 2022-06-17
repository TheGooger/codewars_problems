def is_square(n):
    if n >= 0:
        if pow(n, 1/2) % 1 == 0:
            return True
    return False
