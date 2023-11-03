# Kruskal Algorithm

import heapq

class Graph:

    def __init__(self, v) -> None:
        self.graph = [[] for _ in range(v)]
        self.V = v

    def addEdge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))
    
    def find(self, parent, v):
        if parent[v] != v:
            parent[v] = self.find(parent, parent[v])
        return parent[v]

    def union(self, rank, parent, u, v):
        x = self.find(parent, u)
        y = self.find(parent, v)
        if x != y:
            if rank[x] > rank[y]:
                parent[y] = x
            elif rank[x] < rank[y]:
                parent[x] = y
            else:
                parent[y] = x
                rank[x] += 1
    


    def kruskal(self):
        queue = []
        res = []

        for a in range(len(self.graph)):
            for b in self.graph[a]:
                heapq.heappush(queue, (b[1], b[0], a))
        
        heapq.heappush(queue, (0, 0, 0))

        rank = [0] * self.V
        parent = [0] * self.V
        for i in range(self.V):
            parent[i] = i
        
        while queue:
            cur = heapq.heappop(queue)
            d, a, b = cur[0], cur[1], cur[2]
            if self.find(parent, a) != self.find(parent, b):
                self.union(rank, parent, a, b)
                res.append(cur) 

        print(res)
        tot = 0 
        for i in res:
            tot += i[0]
        print("mst weight", tot)
        return res   

graph = Graph(9)
graph.addEdge(0, 1, 4)
graph.addEdge(0, 7, 8)
graph.addEdge(1, 2, 8)
graph.addEdge(1, 7, 11)
graph.addEdge(2, 3, 7)
graph.addEdge(2, 8, 2)
graph.addEdge(2, 5, 4)
graph.addEdge(3, 4, 9)
graph.addEdge(3, 5, 14)
graph.addEdge(4, 5, 10)
graph.addEdge(5, 6, 2)
graph.addEdge(6, 7, 1)
graph.addEdge(6, 8, 6)
graph.addEdge(7, 8, 7)
graph.kruskal()

'''
time complexity: O(E * log E)
space complexity: O(E + V)
'''