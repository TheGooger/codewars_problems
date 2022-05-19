def sum_array(array):
    """Returns sum of array numbers. If there's no numbers - returns zero."""
    sum = 0
    if array:
        for elements in array:
            sum += elements
    return sum
