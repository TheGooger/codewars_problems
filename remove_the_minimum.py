def remove_smallest(numbers):
    result = numbers[:]
    if result:
        min_val = min(result)
        result.remove(min_val)
    return result
