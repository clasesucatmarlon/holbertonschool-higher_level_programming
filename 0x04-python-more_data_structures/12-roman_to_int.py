#!/usr/bin/python3
dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0

    sum = 0
    i = 0
    if len(roman_string) == 1:
        sum += dic[roman_string[0]]
        return sum

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
