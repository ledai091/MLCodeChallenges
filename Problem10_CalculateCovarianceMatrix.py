# Write a Python function that calculates the covariance matrix from a list of vectors. 
# Assume that the input list represents a dataset where each vector is a feature, and vectors are of equal length.

# Example:
#         input: vectors = [[1, 2, 3], [4, 5, 6]]
#         output: [[1.0, 1.0], [1.0, 1.0]]
#         reasoning: The dataset has two features with three observations each. 
#         The covariance between each pair of features (including covariance with itself) is calculated and returned as a 2x2 matrix.

def calculate_covariance_matrix(vectors: list[list[float]]) -> list[list[float]]:
	features = len(vectors)
	samples = len(vectors[0])
	cov_matrix = [[0 for _ in range(features)] for _ in range(features)]
	list_means = [sum(feature)/samples for feature in vectors]
	
	for i in range(features):
		for j in range(i, features):
			cov = sum((vectors[i][k] - list_means[i]) * (vectors[j][k] - list_means[j]) for k in range(samples)) / (samples - 1)
			cov_matrix[i][j] = cov_matrix[j][i] = cov
	return cov_matrix