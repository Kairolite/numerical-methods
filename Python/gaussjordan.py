# 9.7 Gauss-Jordan

import numpy as np
import sympy as sp
import tabulate as tab
import matplotlib.pyplot as plt


def system():
    mat_a = [[3, -0.1, -0.2],
             [0.1, 7, -0.3],
             [0.3, -0.2, 10]]

    mat_b = [[7.85],
             [-19.3],
             [71.4]]

    mat_c = []
    for i in range(len(mat_a)):
        mat_c.append(mat_a[i][:])
        mat_c[i].append(mat_b[i][0])

    return mat_a, mat_b, mat_c


def gaussjo(mat_aug):
    print(mat_aug)

    # Forward Section
    for i in range(len(mat_aug)):
        pivot = mat_aug[i][i]
        for j in range(len(mat_aug[i])):
            mat_aug[i][j] = mat_aug[i][j]/pivot     # normalize the row
        for n in range(len(mat_aug)-(i+1)):
            row = n+(i+1)
            print(f"Row {row}")
            elim_pivot = mat_aug[row][i]
            for col in range(len(mat_aug[i])):
                print(mat_aug[row], elim_pivot, mat_aug[i][col])
                mat_aug[row][col] = mat_aug[row][col] - (elim_pivot*mat_aug[i][col])    # eliminate terms below
            print(mat_aug[row])
        print(mat_aug)

    # Backward Section
    for i in range(len(mat_aug)):
        print(-(i+1), -(i+2))
        # this is too confusing ...



if __name__ == '__main__':
    print("Hello")

    aug = system()[2]
    gaussjo(aug)
