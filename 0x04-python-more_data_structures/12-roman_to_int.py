#!/usr/bin/python3
def roman_to_int(roman_string):
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    if not isinstance(roman_string, str):
        return 0

    if not roman_string.isupper():
        return 0

    if not roman_string:
        return 0

    sum, i = 0, 0
    if len(roman_string) == 1:
        return dic[roman_string[0]]

    while i < len(roman_string) - 1:
        aux1 = dic[roman_string[i]]
        aux2 = dic[roman_string[i + 1]]

        if aux1 == aux2:
            sum += aux2 + aux1
            i += 1
        elif aux1 < aux2:
            sum += aux2 - aux1
            i += 1
        else:
            sum += aux1
        i = i + 1
    return (sum)
