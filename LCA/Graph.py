# Adjacency Matrix representation in Python taken from Progamiz.com

class Graph(object):

    # Initialize the matrix
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    # Add edges
    def add_edge(self, v1, v2):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.adjMatrix[v1][v2] = 1
        # self.adjMatrix[v2][v1] = 1
        # I commented out the line above because this is a DAG.

    # Remove edges
    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 0
        # self.adjMatrix[v2][v1] = 0
        # Same logic as line 18

    def __len__(self):
        return self.size

    # Print the matrix
    def print_matrix(self):
        for i in self.adjMatrix:
            print('\t'.join(map(str, i)))
