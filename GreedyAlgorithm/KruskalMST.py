#  Kruskal's Minimum Spanning Tree (MST)

'''
Kruskal’s Algorithm

In Kruskal’s algorithm, sort all edges of the given graph in increasing order. 
Then it keeps on adding new edges and nodes in the MST if the newly added edge does not form a cycle. 
It picks the minimum weighted edge at first and the maximum weighted edge at last.

'''


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
    
    # add edge to the graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # utility function to find set of an element i
    # path compression technique
    def find(self, parent,i):
        if parent[i] != i:
            return self.find(parent, parent[i])
        return parent[i]

    # a function that does union of two sets of x and y
    # use union by rank
    def union(self, parent, rank, x, y):

        # attach smaller rank tree under the root of
        # high rank tree
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x

        # if ranks are the same, make one as root
        # and increment its rank by one
        else:
            parent[y] = x
            rank[x] += 1
    

    def KruskalMST(self):
        # store resultant MST
        result = []

        # idx for sorted edges
        i = 0

        # idx for result
        e = 0

        # sort all edges in non-decreasing order of their weight
        self.graph = sorted(self.graph, key = lambda x : x[2])

        parent = []
        rank = []

        # create v subsets with single elements
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        
        # the number of edges to be taken is less than v-1
        while e < self.V - 1:
            
            # pick the smallest edge and increment 
            # the index for next iteration
            u,v,w = self.graph[i]
            i  = i+1
            x = self.find(parent, u)
            y = self.find(parent, v)

            # if including the edge does not cause cycle, 
            # include it in result.
            if x != y:
                e = e + 1
                result.append([u,v,w])
                self.union(parent, rank, x, y)
        
        minCost = 0
        print("Edges in the constructed MST")
        for u, v, w in result:
            minCost += w
            print("%d -- %d == %d"%(u, v, w))
        print("Minimum Spanning Tree ", minCost)

if __name__ == '__main__':
    g = Graph(4)
    g.addEdge(0, 1, 10)
    g.addEdge(0, 2, 6)
    g.addEdge(0, 3, 5)
    g.addEdge(1, 3, 15)
    g.addEdge(2, 3, 4)

    g.KruskalMST()

import heapq

class MSTGraph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.parent = []
        for i in range(self.V):
            self.parent.append(i)
        self.rank = [0] * self.V
    
    def addEdge(self, u, v, w):
        heapq.heappush(self.graph, (w, u, v))
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        x = self.find(u)
        y = self.find(v)
        
        if self.rank[x] > self.rank[y]: 
            self.parent[x] = y
        elif self.rank[x] < self.rank[y]:
            self.parent[y] = x
        else:
            self.parent[y] = x
            self.rank[x] += 1
    
    def MST(self):
        result = []
        e = 0
        
        while e < self.V - 1:
            w, u, v = heapq.heappop(self.graph)
            print("e ", w, u, v)
            
            x = self.find(u)
            y = self.find(v)
            
            if x != y:
                self.union(x, y)
                result.append([w, u, v])
                e += 1
        
        weights = 0

        for i in result:
            weights += i[0]
            print("%d - %d == %d"%(i[1], i[2], i[0]))
        print("weight: ", weights)
        return weights

if __name__ == '__main__':
    g = MSTGraph(4)
    g.addEdge(0, 1, 10)
    g.addEdge(0, 2, 6)
    g.addEdge(0, 3, 5)
    g.addEdge(1, 3, 15)
    g.addEdge(2, 3, 4)

    g.MST()


'''
The heapq functions do not keep your list sorted, but only guarantee that the heap property is maintained:

heap[k] <= heap[2*k+1]
heap[k] <= heap[2*k+2]
Consequently, heap[0] is always the smallest item.

When you want to iterate over the items in order of priority, 
you cannot simply iterate over the heap but need to pop() items off until the queue is empty. 
heappop() will take the first item, then reorganize the list to fulfil the heap invariant.


time complexity:
    sorting the edges: O(E * logE)
    union-find algorithm: O(logV)
        The time complexity of the union-find algorithm is less than O(log n) and is often constant. 
        The time complexity of normal union find algorithm is O(N), 
        but when optimised using the path compression and disjoint set, the time complexity is greatly reduced.
    So overall complexity is O(E * logE + E * logV) time.

space complexity:
    o(V+E)
'''
            

