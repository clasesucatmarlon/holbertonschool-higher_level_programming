#!/usr/bin/python3
def get_roman_value(char=''):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    return dic[char]


def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0

    aux = list(map(get_roman_value, list(roman_string)))
    print("aux = {} ".format(aux))
    sum = 0
    for i in range(0, len(aux)):
        if aux[i] > aux[i - 1] and i > 0:
            sum += aux[i] - (2 * aux[i - 1])
        else:
            sum += aux[i]
    return sum
