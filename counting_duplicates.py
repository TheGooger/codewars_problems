def duplicate_count(text):
    counter = 0
    text = list(text.lower())
    list_of_checked = []
    for value in text:
        if text.count(value) > 1 and value not in list_of_checked:
            counter += 1
            list_of_checked.append(value)
    return counter


print(duplicate_count('UJJdSSz716ODOo6z1i'))