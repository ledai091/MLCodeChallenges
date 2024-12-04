# Your task is to write a Python function that implements the k-Means clustering algorithm. This function should take specific inputs 
# and produce a list of final centroids. k-Means clustering is a method used to partition n points into k clusters. 
# The goal is to group similar points together and represent each group by its center (called the centroid).

# Function Inputs:
# points: A list of points, where each point is a tuple of coordinates (e.g., (x, y) for 2D points)
# k: An integer representing the number of clusters to form
# initial_centroids: A list of initial centroid points, each a tuple of coordinates
# max_iterations: An integer representing the maximum number of iterations to perform
# Function Output:
# A list of the final centroids of the clusters, where each centroid is rounded to the nearest fourth decimal.
import math
import numpy as np
def euclidean_distance(point1, point2):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(point1, point2)))
def k_means_clustering(points: list[tuple[float, float]], k: int, initial_centroids: list[tuple[float, float]], max_iterations: int) -> list[tuple[float, float]]:
    final_centroids = initial_centroids

    for _ in range(max_iterations):
        clusters = {i:[] for i in range(k)} 
        for point in points:
            dis = [euclidean_distance(center, point) for center in final_centroids]
            index = dis.index(min(dis))
            clusters[index].append(point)
            
        new_center = []
        for i in range(k):
            if clusters[i]:
                avg = tuple(np.mean([p[j] for p in clusters[i]]) for j in range(len(clusters[i][0])))
                new_center.append(tuple(round(x, 4) for x in avg))
            else:
                new_center.append(final_centroids[i])
        if new_center == final_centroids: break
        
        final_centroids = new_center
    
    return final_centroids
