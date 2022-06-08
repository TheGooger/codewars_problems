def delete_nth(order, max_e):
    # info = {}
    # for element in order:
    #     if order.count(element) > max_e:
    #         info[element] = order.count(element)
    # order.reverse()
    # for number in info.keys():
    #     while info[number] > max_e:
    #         order.remove(number)
    #         info[number] -= 1
    # order.reverse()
    res = []
    for element in order:
        if res.count(element) < max_e:
            res.append(element)
    return res


print(delete_nth([1, 2, 3, 1, 2, 1, 2, 3], 2))
