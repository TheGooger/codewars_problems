def high(words):
    scores = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7,
              'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14,
              'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21,
              'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
    results = {}
    counter = 0
    for word in words.split():
        for letter in scores.keys():
            if letter in word:
                counter += scores[letter] * word.count(letter)
        results[word] = counter
        counter = 0
    values = []
    for score in results.values():
        values.append(score)
    max_score = max(values)
    for final in results.keys():
        if results[final] == max_score:
            return final


print(high('man i need a taxi'))
