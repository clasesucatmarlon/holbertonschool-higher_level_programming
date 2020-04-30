#!/usr/bin/python3


def print_arg(long):
    for num_arg in range(1, long):
        print("{:d}: {:s}".format(num_arg, sys.argv[num_arg]))


if __name__ == "__main__":
    import sys
    # determine and print numbers of arguments input
    long = len(sys.argv)
    if long == 1:
        print("{:d} arguments.".format(long - 1))
    elif long == 1:
        print("{:d} arguments.".format(long - 1))
    else:
        print("{:d} arguments.".format(long - 1))

# Call function to print arguments
print_arg(long)
