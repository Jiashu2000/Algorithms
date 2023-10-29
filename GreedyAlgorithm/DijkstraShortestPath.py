# Dijkstra Shortest Path

'''
Dijkstra Shortest Path

Create a set sptSet (shortest path tree set) that keeps track of vertices included in the shortest path tree, 
i.e., whose minimum distance from the source is calculated and finalized. Initially, this set is empty. 

Assign a distance value to all vertices in the input graph. Initialize all distance values as INFINITE. 
Assign the distance value as 0 for the source vertex so that it is picked first. 

While sptSet doesn't include all vertices 
    Pick a vertex u that is not there in sptSet and has a minimum distance value. 
    Include u to sptSet. 
    Then update the distance value of all adjacent vertices of u. 
        To update the distance values, iterate through all adjacent vertices. 
        For every adjacent vertex v, if the sum of the distance value of u (from source) and weight of edge u-v, 
        is less than the distance value of v, then update the distance value of v. 

'''

import heapq

class graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for i in range(self.V)]
    
    def addEdge(self, u, v, wt):
        self.graph[u].append([v, wt])
        self.graph[v].append([u, wt])
    
    def dijkstra(self, start): 
        # record to see if the node is already in the path
        visited = [False] * self.V
        # all distances are infinite at the begining
        dist = [float('inf')] * self.V
        
        # initialize start point
        dist[start] = 0

        res = [0] * self.V
        pq = []
        heapq.heappush(pq, ((dist[start], start)))

        while pq:
            d, n = heapq.heappop(pq)
            if visited[n]:
                continue
            visited[n] = True
            res[n] = d

            for e in self.graph[n]:
                i = e[0]
                w = e[1]
                if not visited[i] and dist[i] > dist[n] + w:
                    heapq.heappush(pq, (dist[n] + w , i))
                    dist[i] = dist[n] + w

        print(res)
        return res

if __name__ == "__main__":
    # create the graph given in above figure
    V = 9
    g = graph(V)
 
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

'''
time complexity:
    O(E * logV)

space complexity: 
    O(V + E)

'''