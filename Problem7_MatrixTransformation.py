# Write a Python function that transforms a given matrix A using the operation A = T^-1 * A * S, 
# where T and S are invertible matrices. The function should first validate if the matrices T and S are invertible, 
# and then perform the transformation. In cases where there is no solution return -1

# Example:
#         input: A = [[1, 2], [3, 4]], T = [[2, 0], [0, 2]], S = [[1, 1], [0, 1]]
#         output: [[0.5,1.5],[1.5,3.5]]
#         reasoning: The matrices T and S are used to transform matrix A by computing $T^{-1}AS$.

import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	T = np.array(T)
	S = np.array(S)
	A = np.array(A)
	
	if np.linalg.det(T) == 0 or np.linalg.det(S) == 0:
		return -1
	T_inverse = np.linalg.inv(T)
	transformed_matrix = np.matmul(np.matmul(T_inverse, A), S)
	return transformed_matrix