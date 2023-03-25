import numpy as np



def gaussian_elimination(A, b):
    """
    Solves a system of linear equations using Gaussian elimination.

    Parameters:
        A (ndarray): Coefficient matrix.
        b (ndarray): Right-hand side vector.

    Returns:
        ndarray: Solution vector.
    """
    # Augment the matrix with the right-hand side vector
    M = np.column_stack((A, b))

    # Apply row operations to create an upper triangular matrix
    n_rows, n_cols = M.shape
    for i in range(n_rows):
        # Find pivot row
        max_row = i
        for j in range(i + 1, n_rows):
            if abs(M[j, i]) > abs(M[max_row, i]):
                max_row = j

        # Swap rows to move pivot to (i, i)
        M[[i, max_row]] = M[[max_row, i]]

        # Eliminate entries below (i, i)
        for j in range(i + 1, n_rows):
            factor = M[j, i] / M[i, i]
            M[j] -= factor * M[i]

    # Solve for variables using back-substitution
    x = np.zeros(n_rows)
    for i in range(n_rows - 1, -1, -1):
        x[i] = M[i, n_cols - 1] / M[i, i]
        for j in range(i - 1, -1, -1):
            M[j, n_cols - 1] -= M[j, i] * x[i]

    return x

for i in output_dict:
    A=[]

A = np.array([[2, 1, -1, 1],
              [4, -6, 0, -7],
              [4, -2, 2, 8],
              [1, 1, 1, 1]])

for i in output_dict:
    b=[]
    b.append(0)

x = gaussian_elimination(A, b)

print(x)