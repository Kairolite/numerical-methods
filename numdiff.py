# 23.1 Finite Divided Difference

import sympy as sp


def function():
    """Defines the function to be analyzed, and it's first derivative."""
    x = sp.Symbol('x')

    # define the function
    f = -0.1*(x**4) - 0.15*(x**3) - 0.5*(x**2) - 0.25*x + 1.2

    df = f.diff(x)
    ddf = df.diff(x)
    return f, df, ddf


def forward_fdd(xi, h):
    x = sp.Symbol('x')
    f, df, ddf = function()
    f = sp.lambdify(x, f)

    # first derivative
    xi_df_1 = (f(xi + h) - f(xi)) / h
    xi_df_2 = (-f(xi + 2 * h) + 4 * f(xi + h) - 3 * f(xi)) / (2 * h)

    print("Forward First Derivative")
    print(xi_df_1)
    print(xi_df_2)
    print()

    # second derivative
    xi_ddf_1 = (f(xi + 2 * h) - 2 * f(xi + h) + f(xi)) / (h ** 2)
    xi_ddf_2 = (-f(xi + 3 * h) + 4 * f(xi + 2 * h) - 5 * f(xi + h) + 2 * f(xi)) / (h ** 2)

    print("Forward Second Derivative")
    print(xi_ddf_1)
    print(xi_ddf_2)
    print()

    # third derivative

    # fourth derivative
    pass


def backward_fdd(xi, h):
    x = sp.Symbol('x')
    f, df, ddf = function()
    f = sp.lambdify(x, f)

    # first derivative
    xi_df_1 = (f(xi) - f(xi - h)) / h
    xi_df_2 = (f(xi - 2 * h) - 4 * f(xi - h) + 3 * f(xi)) / (2 * h)

    print("Backward First Derivative")
    print(xi_df_1)
    print(xi_df_2)
    print()

    # second derivative
    xi_ddf_1 = (f(xi - 2 * h) - 2 * f(xi - h) + f(xi)) / (h ** 2)
    xi_ddf_2 = (-f(xi - 3 * h) + 4 * f(xi - 2 * h) - 5 * f(xi - h) + 2 * f(xi)) / (h ** 2)

    print("Backward Second Derivative")
    print(xi_ddf_1)
    print(xi_ddf_2)
    print()

    # third derivative

    # fourth derivative
    pass


def centered_fdd(xi, h):
    x = sp.Symbol('x')
    f, df, ddf = function()
    f = sp.lambdify(x, f)

    print(f"xi + h {f(xi + h)}\n")
    print(f"xi - h {f(xi - h)}\n")

    # first derivative
    xi_df_1 = (f(xi + h) - f(xi - h)) / (2 * h)
    xi_df_2 = (-f(xi + 2 * h) + 8 * f(xi + h) - 8 * f(xi - h) + f(xi - 2 * h)) / (12 * h)

    print("Centered First Derivative")
    print(xi_df_1)
    print(xi_df_2)
    print()

    # second derivative
    xi_ddf_1 = (f(xi + h) - 2 * f(xi) + f(xi - h)) / (h ** 2)
    xi_ddf_2 = (-f(xi + 2 * h) + 16 * f(xi + h) - 30 * f(xi) + 16 * f(xi - h) - f(xi - 2 * h)) / (12 * h ** 2)

    print("Centered Second Derivative")
    print(xi_ddf_1)
    print(xi_ddf_2)
    print()

    # third derivative

    # fourth derivative
    pass


def menu():
    x, h = 3.5, 0.5
    forward_fdd(x, h)
    backward_fdd(x, h)
    centered_fdd(x, h)


if __name__ == '__main__':
    menu()
