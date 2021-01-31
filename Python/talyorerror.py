# This is a sample Python script.

import tabulate as tab
import math as m


def cosine(x):
    """
    calculates approximation of cosine function
    by Taylor expansion with error truncation values
    :param x:
    :return:
    """
    deg = x
    rad = x * m.pi / 180  # convert degrees to radians
    term = 1
    cos = 1
    error = 1
    i = 1

    table = []

    errorlimit = 0.0001
    while error >= errorlimit:
        ratio = ((-1) * (rad ** 2)) / (((2 * i) - 1) * (2 * i))
        table.append([i, deg, rad, term, cos, ratio, error, errorlimit, m.cos(rad)])
        term = term * ratio
        prevcos = cos
        cos = cos + term
        error = abs((cos / prevcos) - 1)
        i = i + 1

    print(tab.tabulate(table, headers=["i", "x [deg]", "x [rad]", "term",
                                       "cos [est]", "ratio", "error",
                                       "error limit", "cos [true]"]))

    return 0


def exponential(x):
    """
    calculates approximation of exponential function
    by Taylor expansion with error truncation values
    :param x:
    :return:
    """
    term = 1
    exp = 1
    error = 1
    i = 1

    table = []

    errorlimit = 0.0001
    while error >= errorlimit:
        ratio = x/i
        table.append([i, x, term, exp, ratio, error, errorlimit, m.exp(x)])
        term = term * ratio
        prevexp = exp
        exp = exp + term
        error = abs((exp/prevexp) - 1)
        i = i + 1

    print(tab.tabulate(table, headers=["i", "x", "term", "exp(x) [est]", "ratio",
                                       "error", "error limit", "exp(x) [true]"]))

    return 0


def menu():
    """
    prompts user to select a function
    :return:
    """
    print("Taylor Expansion and Error Truncation")
    i = 0
    while True:
        print("Cosine or Exponentional?")
        funct = input()

        if funct == "cos":
            num = input("Value for cos(x) in degrees:")
            cosine(float(num))
            return False
        elif funct == "exp":
            num = input("Value for exp(x):")
            exponential(float(num))
            return False
        elif i == 3:
            print("Invalid input. Please answer it correctly.")
        else:
            print("Invalid input. Try again.")
        i += 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # cosine(45)            # Test cosine function
    # exponential(2.71)     # Test exponential function

    menu()
