def disemvowel(string):
    for vow in 'aeiouAEIOU':
        string = string.replace(vow, '')
    return string
    """vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    possibles = []
    for letter in string:
        if letter in vowels:
            possibles.append(letter)
    list_s = list(string)
    for vow in possibles:
        list_s.remove(vow)
    return ''.join(list_s)"""



print(disemvowel('This website is for losers LOL!'))
