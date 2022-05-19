def digitize(number):
    """Returns reversed list with digits of given number."""
    number = str(number)
    result = []
    for digit in number:
        result.append(int(digit))
    result.reverse()
    return result
