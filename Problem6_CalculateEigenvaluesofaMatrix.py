# Write a Python function that calculates the eigenvalues of a 2x2 matrix. 
# The function should return a list containing the eigenvalues, sort values from highest to lowest.

# Example:
#         input: matrix = [[2, 1], [1, 2]]
#         output: [3.0, 1.0]
#         reasoning: The eigenvalues of the matrix are calculated using the characteristic equation of the matrix, 
#         which for a 2x2 matrix is $\lambda^2 - 	ext{trace}(A)\lambda + 	ext{det}(A) = 0$, where $\lambda$ are the eigenvalues.

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	eigenvalues = []
	a = matrix[0][0]
	b = matrix[0][1]
	c = matrix[1][0]
	d = matrix[1][1]
	
	lamda_1 = ((a+d) + ((a+d)**2 - 4*(a*d-b*c))**0.5)/2.0
	eigenvalues.append(lamda_1)
	lamda_2 = ((a+d) - ((a+d)**2 - 4*(a*d-b*c))**0.5)/2.0
	eigenvalues.append(lamda_2)
	return eigenvalues