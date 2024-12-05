# Write a Python function that performs k-fold cross-validation data splitting from scratch. 
# The function should take a dataset (as a 2D NumPy array where each row represents a data sample and each column represents a feature) 
# and an integer k representing the number of folds. The function should split the dataset into k parts, 
# systematically use one part as the test set and the remaining as the training set, 
# and return a list where each element is a tuple containing the training set and test set for each fold.

# Example:
#         input: data = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]), k = 5
#         output: [[[[3, 4], [5, 6], [7, 8], [9, 10]], [[1, 2]]],
#                 [[[1, 2], [5, 6], [7, 8], [9, 10]], [[3, 4]]],
#                 [[[1, 2], [3, 4], [7, 8], [9, 10]], [[5, 6]]], 
#                 [[[1, 2], [3, 4], [5, 6], [9, 10]], [[7, 8]]], 
#                 [[[1, 2], [3, 4], [5, 6], [7, 8]], [[9, 10]]]]
#         reasoning: The dataset is divided into 5 parts, each being used once as a test set while the remaining parts serve as the training set.
import numpy as np
def cross_validation_split(data: np.ndarray, k: int, seed=42) -> list:
    np.random.seed(seed)
    np.random.shuffle(data)
    folds = []
    
    for i in range(0, len(data), int(np.ceil(len(data)/ k))):
        if i + int(np.ceil(len(data)/ k)) > len(data):
            index = len(data)
        else:
            index = i + int(np.ceil(len(data)/ k))
        test = data[i:index]
        train = [fold for j, fold in enumerate(data) if j not in range(i, index)]
        folds.append([train] + [test])
    return folds