def is_triangle(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        return True
    return False


def is_triangle_2(*args):
    for element in args:
        if element >= sum(args) - element:
            return False
    return True


is_triangle_2(1, 2, 3)
