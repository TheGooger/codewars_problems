def order(sentence):
    result = []
    for i in range(1, 10):
        for word in sentence.split(' '):
            if str(i) in word:
                result.append(word)
    return ' '.join(result)


print(order('is2 Thi1s T4est 3a'))
