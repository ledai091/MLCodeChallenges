#Write a Python function that computes the transpose of a given matrix.

# Example:
#         input: a = [[1,2,3],[4,5,6]]
#         output: [[1,4],[2,5],[3,6]]
#         reasoning: The transpose of a matrix is obtained by flipping rows and columns.

def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	return [list(i) for i in zip(*a)]