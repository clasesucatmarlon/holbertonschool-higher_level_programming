#!/usr/bin/python3
def no_c(my_string):
    array_letter = ""
    for letter in my_string:
        if letter != "c" and letter != "C":
            array_letter += letter
    return array_letter
