def filter_list(list_of_values):
    result = []
    for element in list_of_values:
        if type(element) == int:
            result.append(element)
    return result


print(filter_list([1, 2, 'a', 'b']))
