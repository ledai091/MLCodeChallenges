# Write a Python function that approximates the Singular Value Decomposition on a 2x2 matrix by using the jacobian method 
# and without using numpy svd function, i mean you could but you wouldn't learn anything. return the result in this format.

# Example:
#         input: a = [[2, 1], [1, 2]]
#         output: (array([[-0.70710678, -0.70710678],
#                         [-0.70710678,  0.70710678]]),
#         array([3., 1.]),
#         array([[-0.70710678, -0.70710678],
#                [-0.70710678,  0.70710678]]))
#         reasoning: U is the first matrix sigma is the second vector and V is the third matrix

import numpy as np

def svd_2x2_singular_values(A: np.ndarray) -> tuple:
    A_T_A = A.T @ A
    theta = 0.5 * np.arctan2(2 * A_T_A[0, 1], A_T_A[0, 0] - A_T_A[1, 1])
    j = np.array([[np.cos(theta), -np.sin(theta)],
                  [np.sin(theta), np.cos(theta)]])
    A_prime = j.T @ A_T_A @ j 
    
    singular_values = np.sqrt(np.diag(A_prime))
    
    return j, singular_values, j.T