#!/usr/bin/python3
def roman_to_int(roman_string):
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    sum = 0
    i = 0

    if not isinstance(roman_string, str):
        return None

    if roman_string is None:
        return None

    long = len(roman_string)

    if long == 1:
        sum += dic[roman_string[0]]
        return sum

    while i < len(roman_string) - 1:
        aux1 = dic[roman_string[i]]
        aux2 = dic[roman_string[i + 1]]

        if aux1 == aux2:
            sum = sum + aux2 + aux1
            i = i + 1
        elif aux1 < aux2:
            sum = sum + aux2 - aux1
            i = i + 1
        else:
            sum = sum + aux1
        i = i + 1
    return (sum)
