# Graph BFS


from collections import defaultdict, deque

class Graph:

    def __init__(self) -> None:
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def BFS(self, s):
        visited = [False] * (max(self.graph) + 1)
        queue = deque()
        queue.append(s)
        
        while queue:
            cur = queue.popleft()
            visited[cur] = True
            print(cur)
            for next in self.graph[cur]:
                if not visited[next]:
                    queue.append(next)

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

    g.BFS(2)

'''
applications of bfs
    1. shortest path and minimum spanning tree for unweighted graph
    2. minimum spanning tree for weighted graph
    3. peer-to-peer networks
    4. crawlers in search engines
    5. social networking
    6. recommendation system
'''