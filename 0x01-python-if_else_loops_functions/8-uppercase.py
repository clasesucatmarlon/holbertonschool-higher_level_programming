#!/usr/bin/python3
def uppercase(str):
    for aux in str:
        if ord(aux) >= 97 and ord(aux) <= 122:
            aux = chr(ord(aux) - 32)
        print("{}".format(aux), end="")
    print()
