def find_nb(m):
    counter = 0
    while m > 0:
        m -= pow(counter, 3)
        counter += 1
    if m == 0:
        return counter - 1
    return -1


print(find_nb(9))
