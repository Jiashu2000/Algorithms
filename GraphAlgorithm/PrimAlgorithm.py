# Prim Algorithm

'''
The algorithm starts with an empty spanning tree. 
The idea is to maintain two sets of vertices. The first set contains the vertices already included in the MST,
and the other set contains the vertices not yet included. 
At every step, it considers all the edges that connect the two sets and picks the minimum weight edge from these edges. 
After picking the edge, it moves the other endpoint of the edge to the set containing MST. 

algorithm:



'''
import heapq

class Graph:

    def __init__(self, v) -> None:
        self.graph = [[] for _ in range(v)]
        self.V = v
    
    def addEdge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))
    
    def prim(self, src):
        mst = set()

        dist = [float('inf')] * self.V
        dist[src] = 0
        
        queue = []

        heapq.heappush(queue, (0, src, -1))

        res = []
        parent = [None] * self.V

        while queue:
            cur = heapq.heappop(queue)
            n= cur[1]
            if n not in mst:
                res.append(cur)
                mst.add(n)
            for node, weight in self.graph[n]:
                if node not in mst:
                    if dist[node] > weight:
                        dist[node] = weight
                        parent[node] = n
                        heapq.heappush(queue, (dist[node], node, n))
        
        for i in range(len(parent)):
            print("from ", parent[i], 'to ', i)
        tot = 0
        for i in res:
            tot += i[0]
        print(res)
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
graph.prim(0)

'''
time complexity: o(E * logV)
space complexity: o(V + E)

The concept of MST allows weights of an arbitrary sign. 
The two most popular algorithms for finding MST (Kruskal's and Prim's) work fine with negative edges.

Actually, you can just add a big positive constant to all the edges of your graph, making all the edges positive. 
The MST (as a subset of edges) will remain the same.

'''