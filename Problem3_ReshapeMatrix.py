#Write a Python function that reshapes a given matrix into a specified shape.

# Example:
#         input: a = [[1,2,3,4],[5,6,7,8]], new_shape = (4, 2)
#         output: [[1, 2], [3, 4], [5, 6], [7, 8]]
#         reasoning: The given matrix is reshaped from 2x4 to 4x2.

import numpy as np
def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	return np.array(a).reshape(new_shape).tolist()