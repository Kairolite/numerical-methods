# 6.2 Newton-Raphson Method
"""
Approximates the root of a function using
the Newton-Raphson Method
"""

import numpy as np
import sympy as sp
import tabulate as tab
import matplotlib.pyplot as plt


def function():
    """Defines the function to be analyzed, and it's first derivative."""
    x = sp.Symbol('x')
    f = sp.exp(-x) - x  # define function
    df = f.diff(x)
    return f, df


def newton_raphson(xi):
    """
    Defines the Newton-Raphson formula.
    :param xi: Previous iteration of x
    :return x_new: Next iteration of x
    """
    x = sp.Symbol('x')
    f = function()[0]
    df = function()[1]
    newrap = sp.lambdify([x], x - (f/df))

    x_new = newrap(xi)

    return x_new


def iteration(x):
    """
    Executes Newton-Raphson iteration up to termination criteria.
    Then prints table of iterations.
    :param x: initial guess value for x
    """
    i = 0
    x_old = 0
    approx_error = 100
    termination = 0.5  # Set termination criteria (approximate relative error %)
    table = []

    while approx_error > termination:
        i += 1
        x = newton_raphson(x)
        approx_error = abs((x - x_old) / x) * 100
        x_old = x
        table.append([i, x, approx_error])

    print("Done\n")
    print(f"Termination Error = {termination}%")
    print(tab.tabulate(table, headers=["i", "x", "approximate error (%)"]))


def plot_function():
    """Generates visual plot for the function."""
    print("Plotting graph...")

    # 100 linearly spaced numbers
    t = np.linspace(-2, 10, 100)

    # calls the function
    x = sp.Symbol('x')
    f = sp.lambdify([x], function()[0])
    y = f(t)

    # setting the axes at the centre
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    # move left y-axis and bottom x-axis to centre, passing through (0,0)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')

    # eliminate upper and right axes
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # show ticks in the left and lower axes only
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # plot the function
    plt.plot(t, y, 'g')

    # show the plot
    plt.show()
    print("Done\n")


def guess():
    """
    Prompts for initial x value input and checks input validity.
    :return xi: initial x value
    """
    while True:
        try:
            xi = float(input("Select initial guess: "))
            break
        except (TypeError, ValueError):
            print("Input values invalid. Please enter a number.")
    return xi


def menu():
    """
    Core function of the program.
    :return:
    """
    print("Newton-Raphson Method\n")
    print("Function\n"
          f"f(x)  = {function()[0]}\n"
          f"f'(x) = {function()[1]}\n")

    while True:
        plot_function()

        while True:
            ans = input("View graph again? (Y/N)\n")
            if ans == 'Y' or ans == 'N':
                break
        if ans == 'N':
            break

    iteration(guess())


if __name__ == '__main__':
    menu()
