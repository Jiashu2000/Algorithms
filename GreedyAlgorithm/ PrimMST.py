# PrimMST

'''
Prim's algorithm is also a greedy algorithm

    1. create a set mstset that keeps track of vertices already included in MST
    2. assign a key value to all vertices in the input graph. Initialize all key values as infinite.
        assign the key value as 0 for the first vertex so that it is picked first.
    3. while mstSet does not include all vertices:
        - pick a vertex u that is not there in mstSet and has a minimum key value
        - include u in the mstSet
        - update the key value of all adjacent vertices of u. To update the key values, iterate through all adjacent vertices.
        for every adjacent vertex v, if the weight of edge u-v is less than the previous key value of v, update the key value
        as the weight of u-v.
'''
import collections
import heapq

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * self.V for _ in range(self.V)]
    
    def printMST(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])
    
    # utility function to find the vertex with minimum distance value,
    # from the set of vertices not yet include in the shortest path tree

    def minKey(self, key, mstSet):
        min = float("inf")

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_idx = v
        return min_idx
    
    def primMST(self):

        # key values used to pick minimum weight edge in cut
        key = [float("inf")] * self.V
        parent = [None] * self.V 

        key[0] = 0
        mstSet = [False] * self.V

        parent[0] = -1

        for cout in range(self.V):

            # pick the minimum distance vertex from set the vertex not yet processed.
            u = self.minKey(key, mstSet)

            mstSet[u] = True

            for v in range(self.V):
                
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u 

        self.printMST(parent)  

if __name__ == '__main__':
    g = Graph(5)
    g.graph = [[0, 2, 0, 6, 0],
               [2, 0, 3, 8, 5],
               [0, 3, 0, 0, 7],
               [6, 8, 0, 0, 9],
               [0, 5, 7, 9, 0]]
 
    g.primMST()

'''
time complexity:
    o(v^2)

space complexity:
    o(v)
'''


class Graph2:
    
    def __init__(self, vertices):
        self.V = vertices
        self.adj = [[] for _ in range(self.V)]
        self.visited = [False] * self.V
        self.pq = []
    
    def MST(self):
        
        self.pq.append([0, -1, 0])
        parent = [None] * self.V
        res = []

        while self.pq:
            cur = heapq.heappop(self.pq)
            if self.visited[cur[2]]:
                continue 
            res.append(cur)
            self.visited[cur[2]] = True
            parent[cur[2]] = cur[1]

            for i in self.adj[cur[2]]:
                nxt = i[0] 
                w = i[1]
                if self.visited[nxt] == False:
                    heapq.heappush(self.pq, [w, cur[2], nxt])
        
        print(parent)
        weight =  0
        for i in res:
            weight += i[0]
        print("total weight", weight)
    
    def addEdge(self, u, v, w):
        self.adj[u].append([v,w])
        self.adj[v].append([u,w])

    

    def tree(V, E, edges):
        # create a adjacent list representation of the graph
        adj = [[] for _ in range(V)]
        # fill in the adjacency list with edges and their weights
        for i in range(E):
            u, v, wt = edges[i]
            adj[u].append([v, wt])
            adj[v].append([u, wt])
        
        # create a priority queue to stroe edges with their weights
        pq = []

        # create a visited array to keep track of visited verrtices
        visited = [False] * V

        # variable to store the result
        res = 0

        # start with vertex 0
        heapq.heappush(pq, (0, 0))

        while pq:

            wt, u = heapq.heappop(pq)
            if visited[u]:
                continue
            
            res += wt
            visited[u] = True

            for v, weight in adj[u]:
                if not visited[v]:
                    heapq.heappush(pq, (weight, v))
        
        return res

# if __name__ == "__main__":
#     graph = [[0, 1, 5],
#              [1, 2, 3],
#              [0, 2, 1]]
#     # Function call
#     print(Graph2.tree(3, 3, graph))
    '''
    time complexity:
        o(E * logE)
    
    space complexity:
        o(v^2)

    '''



if __name__ == '__main__':
    g = Graph2(5)
    g.addEdge(0, 1, 2)
    g.addEdge(1, 2, 3)
    g.addEdge(0, 3, 6)
    g.addEdge(2, 4, 7)
    g.addEdge(1, 3, 8)
    g.addEdge(3, 4, 9)
    g.addEdge(1, 4, 5)
 
    g.MST()
