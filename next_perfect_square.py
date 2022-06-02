def find_next_square(sq):
    root = pow(sq, 0.5)
    if root == int(root):
        return int(pow((root + 1), 2))
    return -1
