def dig_pow(number, power):
    sum = 0
    for digit in str(number):
        sum += pow(int(digit), power)
        power += 1
    if sum % number == 0:
        return int(sum / number)
    return -1
