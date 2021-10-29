from Graph import *
from collections import deque

class LCA_DAG:
    def lowestCommonAncestor(self, graph: 'Graph', x, y):
        self.blue = [0] * graph.size
        self.red = [0] * graph.size
        self.count = [0] * graph.size

        self.markBFS(graph, x, self.blue)
        self.markBFS(graph, y, self.red)

        # eliminate all ancestors of Y that are not ancestors of X
        j = 0
        for i in self.red:
            if (self.blue[j] != i):
                self.red[j] = 0
            j = j + 1

        # all potential LCA candidates marked '1' in red
        # for every LCA candidate, increment parent's count
        vertex = 0
        for i in self.red:
            if (i == 1):
                index = 0
                for v in graph.adjMatrix[vertex]:
                    if (v == 1):
                        self.count[index]  = self.count[index] + 1
                    index = index + 1
            vertex = vertex + 1

        # every 'red' vertex with count = 0 is a solution
        solutions = []

        index = 0
        for i in self.red:
            if (i == 1 and self.count[index] == 0):
                solutions.append(index)
            index = index + 1
        return solutions

    def markBFS(self, graph: 'Graph', root, visited):
        q = deque()
        q.append(root)

        while q:
            vertex = q.popleft()
            # print(vertex)
            visited[vertex] = 1

            to = 0
            for i in graph.adjMatrix[vertex]:
                if (i == 1):
                    q.append(to)
                to = to + 1
