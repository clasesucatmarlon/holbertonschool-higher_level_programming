#!/usr/bin/python3


def extract_string():
    import hidden_4
    for count in dir(hidden_4):
        if count[0] != "_" and count[1] != "_":
            print(count)


if __name__ == "__main__":
    extract_string()
