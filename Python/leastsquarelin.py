# 17.1 Linear Regression

import matplotlib.pyplot as plt
import statistics as stat
import tabulate as tab
import numpy as np


def dataset():
    x = [1, 2, 3, 4, 5, 6, 7]
    y = [0.5, 2.5, 2.0, 4.0, 3.5, 6.0, 5.5]
    return x, y


def coefficient_a1():
    x, y = dataset()
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_xx = sum([i**2 for i in x])
    sum_xy = sum([a*b for a, b in zip(x, y)])

    a1 = ((n * sum_xy) - (sum_x * sum_y)) / ((n * sum_xx) - sum_x ** 2)

    return a1


def coefficient_a0():
    x, y = dataset()
    x_mean = stat.mean(x)
    y_mean = stat.mean(y)
    a1 = coefficient_a1()

    a0 = y_mean - (a1*x_mean)
    return a0


def lin_regress():
    a0 = coefficient_a0()
    a1 = coefficient_a1()

    lq_fit = f"y = {a0} + {a1} * x"
    print(f"Least-Squares Fit\n"
          f"{lq_fit}\n")

    return lq_fit


def regress_errors():
    x, y = dataset()
    a0 = coefficient_a0()
    a1 = coefficient_a1()
    n = len(x)

    sr = sum([(yi - a0 - (a1 * xi)) ** 2 for xi, yi in zip(x, y)])  # sum of the squares
    st = sum([(yi - stat.mean(y)) ** 2 for xi, yi in zip(x, y)])    # total sum of squares of deviations

    sy = (st/(n-1)) ** 0.5          # standard deviation
    syx = (sr/(n - 2)) ** 0.5       # standard error of the estimate

    r_squared = (st - sr) / st      # coefficient of determination
    r = r_squared ** 0.5            # correlation coefficient

    if syx < sy:
        merit = True
    else:
        merit = False

    table = [["Total sum of squares", "Sr", sr],
             ["Total sum of the squares of residuals", "St", st],
             ["Standard deviation", "sy", sy],
             ["Standard error of the estimate", "sy/x", syx],
             ["Linear regression validity", "merit", merit],
             ["Coefficient of determination", "r^2", r_squared],
             ["Correlation coefficient", "r", r]
             ]

    print("Estimation of Errors for the Linear Least-Squares Fit")
    print(tab.tabulate(table))
    print(f"{round(r_squared*100,2)}% of the original uncertainty "
          f"has been explained by the linear model.\n")

    return sr, syx, r


def analysis_table():
    x, y = dataset()
    y_mean = stat.mean(y)
    a0 = coefficient_a0()
    a1 = coefficient_a1()

    dev_sqrd = [(yi - y_mean) ** 2 for yi in y]                     # square of the deviation
    e_sqrd = [(yi - a0 - (a1 * xi)) ** 2 for xi, yi in zip(x, y)]   # square of the residual e

    table = []

    for i in range(len(x)):
        table.append([(i+1), x[i], y[i], dev_sqrd[i], e_sqrd[i]])
    table.append(["---" for i in table[0]])
    table.append(["sum", sum(x), sum(y), sum(dev_sqrd), sum(e_sqrd)])

    print("Error Analysis of the Linear Fit")
    print(tab.tabulate(table, headers=["i", "xi", "yi",
                                       "(yi - y bar)^2", "(yi - a0 - a1xi)^2"]))
    print()

    return table


def plot_function():
    """Generates visual plot for the function."""
    print("Plotting graph...")

    # 100 linearly spaced numbers
    x = np.linspace(-10, 10, 100)

    # calls the function
    xi, yi = dataset()
    a0 = coefficient_a0()
    a1 = coefficient_a1()
    y = a0 + (a1 * x)

    # creating the figure
    fig = plt.figure()
    fig.canvas.set_window_title('Linear Least-Squares Fit')

    # setting the axes at the centre
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
    plt.scatter(xi, yi, c='g')
    plt.plot(x, y, 'r')

    # show the plot
    plt.show()
    print("Done\n")


def menu():
    lin_regress()
    analysis_table()
    regress_errors()
    plot_function()


if __name__ == '__main__':
    menu()
