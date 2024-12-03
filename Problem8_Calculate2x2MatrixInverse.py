# Write a Python function that calculates the inverse of a 2x2 matrix. Return 'None' if the matrix is not invertible.

# Example:
#         input: matrix = [[4, 7], [2, 6]]
#         output: [[0.6, -0.7], [-0.2, 0.4]]
#         reasoning: The inverse of a 2x2 matrix [a, b], [c, d] is given by (1/(ad-bc)) * [d, -b], [-c, a], provided ad-bc is not zero.

def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:
	a = matrix[0][0]
	b = matrix[0][1]
	c = matrix[1][0]
	d = matrix[1][1]
	det = a*d - b*c
	if det == 0:
		return None
	temp_matrix = [[d, -b], [-c, a]]
	inverse = []
	for i in temp_matrix:
		temp_list = []
		for j in i:
			temp_list.append(1/det * j)
		inverse.append(temp_list)
	
	return inverse