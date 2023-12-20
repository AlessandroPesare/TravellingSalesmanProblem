import math
import random
import numpy as np

# geometric istance
def vectorToDistMatrix(coords):
    """
    Create the distance matrix
    """
    num_points = len(coords)
    dist_matrix = np.zeros((num_points, num_points))

    for i in range(num_points):
        for j in range(i + 1, num_points):
            # Calcola la distanza euclidea tra i punti i e j
            distance = np.linalg.norm(coords[i] - coords[j])
            # Assegna la distanza alla matrice delle distanze (simmetrica)
            dist_matrix[i][j] = distance
            dist_matrix[j][i] = distance  # La matrice è simmetrica

    return dist_matrix
    
#non geometric istance
def vectorToDistMatrixRandom(coords):
    """
    Create the distance matrix
    """
    num_points = len(coords)
    dist_matrix = np.zeros((num_points, num_points))

    for i in range(num_points):
        for j in range(i + 1, num_points):
            # Calcola la distanza euclidea tra i punti i e j
            distance = np.random.randint(1, 11)
            # Assegna la distanza alla matrice delle distanze (simmetrica)
            dist_matrix[i][j] = distance
            dist_matrix[j][i] = distance  # La matrice è simmetrica

    return dist_matrix

def nearestNeighbourSolution(dist_matrix):
    num_nodes = len(dist_matrix)
    start_node = random.randrange(num_nodes)
    unvisited_nodes = set(range(num_nodes))
    unvisited_nodes.remove(start_node)

    current_node = start_node
    result = []
    result.append(start_node)

    while unvisited_nodes:
        nearest_node = min(unvisited_nodes, key=lambda x: dist_matrix[current_node][x])
        result.append(nearest_node)
        unvisited_nodes.remove(nearest_node)
        current_node = nearest_node

    return result
