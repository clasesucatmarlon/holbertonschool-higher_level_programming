#!/usr/bin/python3
"""module read lines
    """


def read_lines(filename="", nb_lines=0):
    """read n lines de file text
    """
    array = []
    with open(filename, "r", encoding="utf-8") as data_file:
        count = 0
        for count, line in enumerate(data_file):
            if count < nb_lines or nb_lines == 0:
                array.append(line)
            else:
                break
        print("{}".format("".join(array)), end="")
