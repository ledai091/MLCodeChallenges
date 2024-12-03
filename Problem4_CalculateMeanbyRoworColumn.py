# Write a Python function that calculates the mean of a matrix either by row or by column, based on a given mode. 
# The function should take a matrix (list of lists) and a mode ('row' or 'column') as input and return a list of means according to the specified mode.

# Example1:
#         input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], mode = 'column'
#         output: [4.0, 5.0, 6.0]
#         reasoning: Calculating the mean of each column results in [(1+4+7)/3, (2+5+8)/3, (3+6+9)/3].

#Example 2:
#         input: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], mode = 'row'
#         output: [2.0, 5.0, 8.0]
#         reasoning: Calculating the mean of each row results in [(1+2+3)/3, (4+5+6)/3, (7+8+9)/3].

def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	means = []
	if mode == "row":
		for i in matrix:
			means.append(sum(i)/len(i))
	else:
		new_matrix = [list(i) for i in zip(*matrix)]
		for i in new_matrix:
			means.append(sum(i)/len(i))
	return means