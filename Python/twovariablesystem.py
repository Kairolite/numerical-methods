# Two Variable System of Equations

import sympy as sp
import tabulate as tab


def function1():
    """
    States the first function with two
    variables in terms of x and y
    :return: f: the function as a SymPy object
    """
    x = sp.Symbol('x')
    y = sp.Symbol('y')
    # f = sp.exp(0.1*x) - 10*y
    f = (0.05 * (x**3)) - y

    return f


def function2():
    """
    States the first function with two
    variables in terms of x and y
    :return: f: the function as a SymPy object
    """
    x = sp.Symbol('x')
    y = sp.Symbol('y')
    # f = 0.2 * x - 20 + 3 * y ** 2
    f = 6*x + y**2 - 100

    return f


def derivation(f):
    """
    Differentiates a function in terms of x and then in terms of y
    :param f: the function to be differentiated
    :return: the differentiated function in terms of x and y respectively
    """
    x = sp.Symbol('x')
    y = sp.Symbol('y')
    f_primex = f.diff(x)
    f_primey = f.diff(y)
    print(f"{f}\n"
          f"f'x = {f_primex}\n"
          f"f'y = {f_primey}\n")
    return f_primex, f_primey


def solve(f1, f2):
    """
    Receives sample input values for x and y, and solves for true values for x and y.
    Prints table of iterations until established error limit is reached.
    :param f1: function 1
    :param f2: function 2
    :return:
    """
    a, b, x, y = sp.symbols('a b x y')

    func_matrix = sp.Matrix([f1, f2])

    print("Function 1")
    f1p1, f1p2 = derivation(f1)
    print("Function 2")
    f2p1, f2p2 = derivation(f2)
    diff_matrix = sp.Matrix([[f1p1, f1p2],
                             [f2p1, f2p2]])

    print("Formulating Gauss-Jordan solution...")
    gauss_sol, gauss_params = diff_matrix.gauss_jordan_solve(func_matrix)
    gauss = sp.lambdify([x, y], gauss_sol)
    print("Gauss-Jordan solution found.\n")

    i = 1
    error_limit = 0.001
    error = 1
    x_sample = float(input("Initial value for x: "))
    y_sample = float(input("Initial value for y: "))
    print("")

    table = []

    while error >= error_limit:
        sol_matrix = gauss(x_sample, y_sample)

        table.append([i, x_sample, y_sample,
                      sol_matrix[0][0], sol_matrix[1][0],
                      error, error_limit])

        old_x = x_sample
        old_y = y_sample
        x_sample = old_x - sol_matrix[0][0]
        y_sample = old_y - sol_matrix[1][0]
        error = abs(old_x - x_sample)
        i += 1

    print(tab.tabulate(table, headers=["i", "x", "y", "(a-x)", "(b-y)", "error", "error limit"]))

    return None


if __name__ == '__main__':
    print("Creating Functions...\n")
    func1 = function1()
    func2 = function2()
    print(f"Functions\n"
          f"f1 = {func1}\n"
          f"f2 = {func2}\n")

    solve(func1, func2)
