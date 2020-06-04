#!/usr/bin/python3
"""inserts a line of text to a file
    """


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file
    """
    aux = ""
    with open(filename, "r", encoding="utf-8") as file_data:
        for k in file_data:
            # aux += k
            if search_string in k:
                aux += k[:] + new_string
            else:
                aux += k

    with open(filename, "w", encoding="utf-8") as file_data:
        file_data.write(aux)
