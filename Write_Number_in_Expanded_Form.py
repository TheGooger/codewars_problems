# def expanded_form(num):
#     divider = 10
#     result = []
#     res_str = ''
#     for i in range(len(str(num)) - 1):
#         temp = num % divider
#         if temp != 0:
#             result.append(str(temp))
#         num -= temp
#         divider *= 10
#     result.append(str(num))
#     for i in range(1, len(result) + 1):
#         if i in range(1, len(result)):
#             res_str += result[-i] + ' + '
#         else:
#             res_str += result[-i]
#     return res_str
def expanded_form(num):
    num = list(str(num))
    return ' + '.join(x + '0' * (len(num) - y - 1) for y,x in enumerate(num) if x != '0')


print(expanded_form(70304))
