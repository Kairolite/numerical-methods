# Matrix Regression
# Example 17.5, Numerical Methods for Engineers 7th Ed.
# Christopher S.E.
# November 2020

"""
Produces a polynomial equation for a Least-Squares Regression by matrix method.

Input:
The dataset and polynomial order can be input in the dataset() function.

Output:
Error analysis and estimation of errors are printed as tables.
Data set points and regression polynomial plotted using matplotlib.
"""

import numpy as np
import tabulate as tab
import statistics as stat
import matplotlib.pyplot as plt


def dataset():
    """Defines the data as a set of (x, y) points."""
    # x = [0, 1, 2, 3, 4, 5]
    # y = [2.1, 7.7, 13.6, 27.2, 40.9, 61.1]
    x = [1, 3, 4, 5, 6]
    y = [4, 3, 2, 1, 0]
    y = [4, 9, 8, 5, 0]

    # degree of polynomial regression,
    # m-order polynomial, where n >= m+1
    m = 2

    return x, y, m


def equation_matrix():
    """Generates the matrices of normal equations."""
    x, y, m = dataset()

    mat_eq_x = np.array([[xi ** i for i in range(m+1)] for xi in x])
    mat_eq_y = np.array([[yi] for yi in y])

    mat_x = np.matmul(np.transpose(mat_eq_x), mat_eq_x)
    mat_y = np.matmul(np.transpose(mat_eq_x), mat_eq_y)

    return mat_x, mat_y


def solve_coeff():
    """Solves the coefficients of the regression polynomial."""
    x, y = equation_matrix()

    a = np.linalg.solve(x, y)

    return a


def regression():
    """"Prints out the Least-Squares Fit polynomial."""
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
    """Calculates and prints estimation error factors."""
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
    """Calculates and prints an error analysis as an iterative table."""
    x, y, m = dataset()
    a = solve_coeff()

    # the squares of the residuals
    dev_sqrd = [(yi - stat.mean(y)) ** 2 for yi in y]

    # the squares
    e_sqrd = [(yi - sum([ai*(xi**i) for i, ai in zip(range(len(a)), a)])) ** 2 for xi, yi in zip(x, y)]

    # generate table
    table = []

    for i in range(len(x)):
        table.append([(i + 1), x[i], y[i], dev_sqrd[i], e_sqrd[i]])
    table.append(["---" for i in table[0]])
    table.append(["sum", sum(x), sum(y), sum(dev_sqrd), sum(e_sqrd)])

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
        y += a[term] * (x ** term)

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
    """Main function of the program"""
    debug_matrix()
    regression()
    error_analysis()
    estimation_errors()
    plot_function()


def debug_matrix():
    """Prints out the simultaneous linear equations matrices."""
    x, y = equation_matrix()
    print(f"Matrix X\n{x}\n")
    print(f"Matrix Y\n{y}\n")

    a = solve_coeff()
    print(f"Matrix A\n{a}\n")


if __name__ == '__main__':
    menu()
