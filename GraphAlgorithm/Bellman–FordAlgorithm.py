# Bellman–Ford Algorithm

'''
Bellman-Ford is a single source shortest path algorithm that determines the shortest path 
between a given source vertex and every other vertex in a graph.

Although Bellman-Ford is slower than Dijkstra's algorithm, 
it is capable of handling graphs with negative edge weights

The shortest path cannot be found if there exists a negative cycle in the graph. 
As a result, Bellman-Ford is also capable of detecting negative cycles, which is an important feature.

Principle of Relaxation of Edges for Bellman-Ford:
“Principle of Relaxation" 

    - It states that for the graph having N vertices, all the edges should be relaxed N-1 times to 
    compute the single source shortest path.
    - In order to detect whether a negative cycle exists or not, relax all the edge one more time 
    and if the shortest distance for any node reduces then we can say that a negative cycle exists. 
    In short if we relax the edges N times, and there is any change in the shortest distance of any node 
    between the N-1th and Nth relaxation than a negative cycle exists, otherwise not exist.

Algorithm: 
    - Initialize distance array dist[] for each vertex 'v' as dist[v] = INFINITY.
    - Assume any vertex (let's say '0') as source and assign dist = 0.
    - Relax all the edges(u,v,weight) N-1 times as per the below condition:
        dist[v] = minimum(dist[v], distance[u] + weight)
    - Now, Relax all the edges one more time i.e. the Nth time and based on the below two cases we can detect 
        the negative cycle:
        Case 1 (Negative cycle exists): For any edge(u, v, weight), if dist[u] + weight < dist[v]
        Case 2 (No Negative cycle) : case 1 fails for all the edges.
'''


class Graph:


    def __init__(self, v) -> None:
        self.graph = []
        self.V = v
    
    def addEdge(self, u, v, w):
        self.graph.append((u, v, w))
    
    def printArr(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))
    
    def BellmanFord(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0
        
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        
        for u, v, w in self.graph:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                print("the graph contains negative cycle.")
                return
        self.printArr(dist)

# Driver's code
if __name__ == '__main__':
    g = Graph(5)
    g.addEdge(0, 1, -1)
    g.addEdge(0, 2, 4)
    g.addEdge(1, 2, 3)
    g.addEdge(1, 3, 2)
    g.addEdge(1, 4, 2)
    g.addEdge(3, 2, 5)
    g.addEdge(3, 1, 1)
    g.addEdge(4, 3, -3)
 
    # function call
    g.BellmanFord(0)


'''
time complexity: O(V*E)
space complexity: O(E*(V^2))

applications:
    1. networking routing
    2. gps navigation
    3. transportation and logistics

'''