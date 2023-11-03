# Topological Sort

'''
The topological sort algorithm takes a directe graph and returns an array of nodes 
where each nodes appear before all the nodes it points to.

    The ordering of the nodes in the array is called a topological ordering

    cyclic graphs do not have valid topological orderings

Implementation:
    - identify a node with no incoming edges
    - add that node to the ordering
    - remove it from the graph
    - repeat

If there are some nodes left and they all have incoming edges. It means the graph
has a cycle, and no topological ordering exists.

Time complexity: o(m+n)
    - determine indegree for each node: o(m) where m is the number of edges
    - find nodes with no incoming edges: o(n) where n is the number of nodes
    - add nodes until we run out of nodes with no incoming edges: o(m) decrement by each edge
    - check if we include all nodes or found a cycle: o(1)

Space complexity: o(n)
    - indegree: one entry for each node: o(n)
    - node with no incoming edges: o(n)
    - topological ordering: o(n)

Usage: the most common use for topological sort is ordering steps of a process where
some steps depend on each other.
'''

from collections import defaultdict
import heapq


class BFSGraph:


    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
    
    def add_edge(self, u, v):
        self.graph[u-1].append(v-1)
    
    def topological_sort(self):
        indegree = [0] * self.V
        visited = [0] * self.V
        for i in self.graph:
            for j in self.graph[i]:
                indegree[j] += 1
        top_order = []
        queue = []
        for i in range(self.V):
            if indegree[i] == 0:
                heapq.heappush(queue, i)
        
        while queue:
            u = heapq.heappop(queue)
            if not visited[u]:
                top_order.append(u+1)
                for i in self.graph[u]: 
                    indegree[i] -= 1
                    if indegree[i] == 0:
                        heapq.heappush(queue, i)
                visited[u] = 1
        return top_order

# ## Driver code  
# A = 6
# B = [[6, 3], [6, 1], [5, 1], [5, 2], [3, 4], [4, 2]]
# graph = BFSGraph(A)
# for u, v in B:
#     graph.add_edge(u, v)
#         
# res = graph.topological_sort()
# print(res) # [5, 6, 1, 3, 4, 2]

'''
DFS itself ensures that you don't leave a node until its children have already been processed, 
so if you add each node to a list when DFS finishes with it, 
they will be added in (reverse) topological order.
'''
class DFSGraph:

    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
    
    def add_edge(self, u, v):
        self.graph[u-1].append(v-1)
    
    def helper(self, u, visited, res):
        visited[u] = True
        for i in self.graph[u]:
            if visited[i] == False:
                self.helper(i, visited, res)
        res.insert(0, u+1)
    
    def topological_sort(self):
        visited = [False] * self.V
        res = []
        for i in reversed(range(self.V)): #lexicographically the smallest one 
            if visited[i] == False:
                self.helper(i, visited, res)
        return res

# ## Driver code
# A = 6
# B = [[6, 3], [6, 1], [5, 1], [5, 2], [3, 4], [4, 2]]
# graph = DFSGraph(A)
# for u, v in B:
#     graph.add_edge(u, v)
#         
# res = graph.topological_sort()
# print(res) # [5, 6, 1, 3, 4, 2]

'''
useful links: 
https://www.interviewcake.com/concept/java/topological-sort#:~:text=The%20topological%20sort%20algorithm%20takes,is%20called%20a%20topological%20ordering.

https://python.plainenglish.io/topological-sort-python-119f2c012b52

'''
