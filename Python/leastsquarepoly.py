# 17.2 Polynomial Regression
# Example 17.5

import numpy as np
import tabulate as tab
import statistics as stat
import matplotlib.pyplot as plt


def dataset():
    x = [0, 1, 2, 3, 4, 5]
    y = [2.1, 7.7, 13.6, 27.2, 40.9, 61.1]

    # degree of polynomial regression,
    # m-order polynomial where n >= m+1
    m = 2

    return x, y, m


def equation_matrix():
    x, y, m = dataset()

    mat_y = [[sum([(xi**i)*yi for xi, yi in zip(x, y)])] for i in range(m+1)]

    sum_power_x = [sum([xi**i for xi in x]) for i in range(2*m+1)]

    mat_x = []
    for row in range(m+1):
        rowlist = []
        for col in range(m+1):
            rowlist.append(sum_power_x[col+row])
        mat_x.append(rowlist)

    return mat_x, mat_y


def solve_coeff():
    x, y = equation_matrix()

    x = np.array(x)
    y = np.array(y)

    a = np.linalg.solve(x, y)

    return a


def regression():
    a = solve_coeff()

    lq_fit = f"y = {a[0]} + {a[1]}*x"

    if len(a > 2):
        for i in range(len(a)-2):
            term = f" + {a[i+2]}*x^{i+2}"
            lq_fit = lq_fit + term

    print(f"Least-Squares Fit\n"
          f"{lq_fit}\n")

    return lq_fit


def estimation_errors():
    x, y, m = dataset()
    a = solve_coeff()

    # calculate the total sum of the squares of the residuals
    st = sum([(yi - stat.mean(y)) ** 2 for yi in y])

    # calculate the sum of the squares
    sr = sum([(yi - sum([ai*(xi**i) for i, ai in zip(range(len(a)), a)])) ** 2 for xi, yi in zip(x, y)])

    # calculate the standard error
    std_err = (sr/(len(x)-(m+1)))

    # calculate the coefficient of determination
    r2 = (st - sr)/st

    # calculate the correlation coefficient
    r = r2 ** 0.5

    # print the values
    table = [["Total sum of squares", "Sr", sr],
             ["Total sum of the squares of residuals", "St", st],
             ["Standard error of the estimate", "sy/x", std_err],
             ["Coefficient of determination", "r^2", r2],
             ["Correlation coefficient", "r", r]]

    print("Estimation of Errors for the Least-Squares Fit")
    print(tab.tabulate(table))
    print(f"{round(r2[0] * 100, 2)}% of the original uncertainty "
          f"has been explained by the model.\n")

    return table


def error_analysis():
    x, y, m = dataset()
    a = solve_coeff()

    # the squares of the residuals
    dev_sqrd = [(yi - stat.mean(y)) ** 2 for yi in y]

    # the squares
    e_sqrd = [(yi - sum([ai*(xi**i) for i, ai in zip(range(len(a)), a)])) ** 2 for xi, yi in zip(x, y)]

    table = []

    for i in range(len(x)):
        table.append([(i + 1), x[i], y[i], dev_sqrd[i], e_sqrd[i][0]])
    table.append(["---" for i in table[0]])
    table.append(["sum", sum(x), sum(y), sum(dev_sqrd), sum(e_sqrd)[0]])

    print("Error Analysis of the Least-Squares Fit")
    print(tab.tabulate(table, headers=["i", "xi", "yi",
                                       "(yi - y bar)^2", "squares (e^2)"]))
    print()

    return table


def plot_function():
    """Generates visual plot for the function."""
    print("Plotting graph...")

    # 100 linearly spaced numbers
    x = np.linspace(-10, 10, 100)

    # calls the function
    xi, yi, m = dataset()
    a = solve_coeff()

    y = 0
    for term in range(len(a)):
        y += a[term][0] * (x ** term)

    # creating the figure
    fig = plt.figure()
    fig.canvas.set_window_title('Polynomial Least-Squares Fit')

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
    regression()
    error_analysis()
    estimation_errors()
    plot_function()


if __name__ == '__main__':
    x, y = equation_matrix()
    print(x)
    print(y)
    a = solve_coeff()
    print(a)
