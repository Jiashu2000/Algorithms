# Graph DFS

from collections import defaultdict

class Graph:

    def __init__(self) -> None:
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def DFSUtil(self, s, visited):
        visited.add(s)
        print(s)

        for nxt in self.graph[s]:
            if nxt not in visited:
                self.DFSUtil(nxt, visited)

    def DFS(self, s):
        visited = set()
        self.DFSUtil(s, visited)

    '''
    time: O(V + E)
    space: o(V)
    '''
        


if __name__ == '__main__':

    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    g.DFS(2)



'''
applications of dfs
    1. detecting cycle in a graph: A graph has a cycle if and only if we see a back edge during DFS. 
    2. path finding: 
    3. topological sorting
    4. test if a graph is bipartite
    5. find strongly connected components
    6. solving puzzles with only one solution
    7. web crawler: explore links on a website.
    8. maze generation
    9. model checking
    10. backtracking

pros of dfs:
    DFS requires less memory since only the nodes on the current path are stored. 
    By chance DFS may find a solution without examining much of the search space at all.

'''
