# Chapter 5.2 The Bisection Method
# Example 5.4
import numpy as np
import tabulate as tab
import matplotlib.pyplot as plt


def function(x):
    """
    Defines the function.
    :param x:
    :return:
    """
    # y = np.sin(10 * x) + np.cos(3 * x)
    y = (((9.81*68.1)/x)*(1-np.exp(-(x/68.1)*10)))-40
    return y


def plot_function():
    """
    Generates visual plot for the function.
    :return:
    """
    print("Plotting graph...")

    # 100 linearly spaced numbers
    x = np.linspace(-20, 20, 100)

    # calls the function
    y = function(x)

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
    plt.plot(x, y, 'g')

    # show the plot
    plt.show()
    # plt.pause(0.001)
    # input("Press [enter] to continue.")
    print("Done")


def guess():
    """
    Prompts guess input values for lower x and upper x.
    :return:
    """
    print("Determining brackets...")
    while True:

        # Checks if input is a valid number
        while True:
            try:
                x_low = float(input("Lower x value: "))
                x_up = float(input("Upper x value: "))
                check = function(x_low) * function(x_up)
                break
            except (TypeError, ValueError):
                print("Input values invalid. Please enter a number.")

        # Checks if x_low and x_up are valid guesses
        if x_low > x_up:
            print("Lower x  is larger than Upper x. Try again.")
        elif check < 0:
            break
        elif check >= 0:
            print("Invalid guess. Function does not "
                  "change sign over interval."
                  + f" [check = {check}]")
        else:
            print("Something went wrong. Try again.")

    return x_low, x_up


def find_root():
    """
    Executes bisection iteration up to termination criteria.
    Prints table of iterations.
    :return:
    """
    xl, xu = guess()
    i = 0
    xr_old = 0
    approx_error = 100
    termination = 0.5       # Set termination criteria (approx. rel. error %)
    table = []

    print("Evaluating...")

    while approx_error >= termination:
        i += 1
        xr = (xl + xu) / 2
        subinterval = function(xl) * function(xr)
        approx_error = abs((xr-xr_old)/xr)*100
        table.append([i, xl, xu, xr, subinterval, approx_error])
        if subinterval < 0:
            xu = xr
            xr_old = xr
        elif subinterval > 0:
            xl = xr
            xr_old = xr
        elif subinterval == 0:
            break
        else:
            print("Something went wrong.")
            break
    print("Done")
    print(tab.tabulate(table, headers=["i", "lower x", "upper x",
                                       "root estimate", "subinterval",
                                       "approximate error"]))


if __name__ == '__main__':
    print("Bracketing: The Bisection Method")
    plot_function()
    find_root()
