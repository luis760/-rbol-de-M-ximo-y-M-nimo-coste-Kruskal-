# -*- coding: utf-8 -*-
"""
Created on Wed May 17 10:46:38 2023

@author: 52331
"""

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1


def kruskal(graph):
    num_vertices = len(graph)
    union_find = UnionFind(num_vertices)
    edges = []

    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if graph[i][j] != 0:
                edges.append((i, j, graph[i][j]))

    edges.sort(key=lambda x: x[2])  # Ordenar las aristas por peso

    minimum_spanning_tree = []
    for edge in edges:
        u, v, weight = edge
        if union_find.find(u) != union_find.find(v):
            union_find.union(u, v)
            minimum_spanning_tree.append(edge)

    return minimum_spanning_tree


# Ejemplo de uso
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

minimum_spanning_tree = kruskal(graph)

print("Aristas del árbol de expansión mínima:")
for edge in minimum_spanning_tree:
    print(f"({edge[0]}, {edge[1]}) - Peso: {edge[2]}")
