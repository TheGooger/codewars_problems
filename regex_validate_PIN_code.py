def validate_pin(pin):
    flag = False
    if len(pin) in (4, 6):
        for element in pin:
            try:
                element = int(element)
            except ValueError:
                return False
            else:
                flag = True
    return flag

a = "1234"
print(a.isdigit())