def square_digits(num):
    result = ""
    for digit in str(num):
        result += str(pow(int(digit), 2))
    return int(result)

