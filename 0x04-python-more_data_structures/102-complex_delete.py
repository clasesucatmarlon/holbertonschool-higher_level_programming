#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for aux in list(a_dictionary):
        if a_dictionary[aux] == value:
            del a_dictionary[aux]
    return a_dictionary
