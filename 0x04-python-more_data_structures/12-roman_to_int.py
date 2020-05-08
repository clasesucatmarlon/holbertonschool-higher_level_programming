#!/usr/bin/python3
def get_roman_value(char=''):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    return dic[char]


def roman_to_int(roman_string):
    if not roman_string.isupper():
        return 0
    if not roman_string:
        return 0

    if isinstance(roman_string, str):
        aux = list(map(get_roman_value, list(roman_string)))
        sum = 0
        for i in range(0, len(aux) - 1):
            if aux[i] < aux[i + 1]:
                sum -= aux[i]
            else:
                sum += aux[i]
        sum += aux[len(aux) - 1]
        return sum
    else:
        return 0
