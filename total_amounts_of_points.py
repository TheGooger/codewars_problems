def points(games):
    result = 0
    for element in games:
        if int(element[0]) > int(element[-1]):
            result += 3
        elif int(element[0]) == int(element[-1]):
            result += 1
    return result


print(points(['3:1', '1:1']))
