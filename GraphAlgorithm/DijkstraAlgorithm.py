# Dijkstra Algorithm

'''
Given a graph and a source vertex in the graph, find the shortest paths from the source to all vertices in the given graph.

'''

from collections import defaultdict
import heapq

class Graph:

    def __init__(self, v):
        self.graph = [[] for _ in range(v)]
        self.V = v

    def addEdge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))
    
    def dijkstra(self, s):
        # set the distance to infinity
        distance = [float("inf")] * self.V
        distance[s] = 0
        
        pq = []
        heapq.heappush(pq, (0, s))
        
        # set to include visited nodes
        visited = set()

        while pq:
            cur = heapq.heappop(pq)
            d, n = cur[0], cur[1]
            visited.add(n)
            for nxt, wgt in self.graph[n]:
                if nxt not in visited and distance[nxt] > distance[n] + wgt:
                    distance[nxt] = distance[n] + wgt
                    heapq.heappush(pq, (distance[n], nxt))
        
        print(distance)
        return distance
    
    '''
    Time: o(E * logV)
    Space: o(E + V)
    '''

if __name__ == "__main__":
    # create the graph given in above figure
    V = 9
    g = Graph(V)
 
    # making above shown graph
    g.addEdge(0, 1, 4)
    g.addEdge(0, 7, 8)
    g.addEdge(1, 2, 8)
    g.addEdge(1, 7, 11)
    g.addEdge(2, 3, 7)
    g.addEdge(2, 8, 2)
    g.addEdge(2, 5, 4)
    g.addEdge(3, 4, 9)
    g.addEdge(3, 5, 14)
    g.addEdge(4, 5, 10)
    g.addEdge(5, 6, 2)
    g.addEdge(6, 7, 1)
    g.addEdge(6, 8, 6)
    g.addEdge(7, 8, 7)
 
    g.dijkstra(0)

        
        
        
        