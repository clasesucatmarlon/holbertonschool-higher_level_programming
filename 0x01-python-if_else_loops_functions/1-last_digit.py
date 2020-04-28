#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    last = number % 10
else:
    last = number % -10
if last > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
        .format(number, last))
elif last == 0:
    print("{} {:d} {} {:d} {}".format("Last digit of",
        number, "is", last, "and is 0"))
elif last < 6:
    print("{} {:d} {} {:d} {}".format("Last digit of ",
        number, "is ", last, " and is less than 6 and not 0"))
