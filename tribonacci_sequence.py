def tribonacci(signature, n):
    # result = signature.copy()
    # if n == 0:
    #     return []
    # elif n == 1:
    #     return result[0:1]
    # elif n == 2:
    #     return result[0:2]
    # elif n == 3:
    #     return result
    # else:
    #     for i in range(n - len(signature)):
    #         result.append(result[-3] + result[-2] + result[-1])
    #     return result
    if n in range(4):
        for i in range(4):
            if n == i:
                return signature[0:i]
    else:
        for i in range(n - len(signature)):
            signature.append(signature[-3] + signature[-2] + signature[-1])
        return signature



print(tribonacci([1, 1, 1], 5))
