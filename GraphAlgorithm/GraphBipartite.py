# GraphBipartite


def addEdge(adj, u, v):
    adj[u].append(v)
    adj[v].append(u)

def isBipartite(adj, v, visited, color):
    for u in adj[v]:
        if not visited[u]:
            visited[u] = True
            color[u] = not color[v]
            
            if not isBipartite(adj, u, visited, color):
                return False
        else:
            if color[u] == color[v]:
                return False
    return True

if __name__ == "__main__":

    N = 6

    # to maintain the adjacency list of graph
    adj = [[] for i in range(N+1)]
    
    visited = [0 for i in range(N+1)] 

    color = [0 for i in range(N+1)]

    addEdge(adj, 1, 2)
    addEdge(adj, 2, 3)
    addEdge(adj, 3, 4)
    addEdge(adj, 4, 5)
    addEdge(adj, 5, 6)
    addEdge(adj, 6, 1)

    visited[1] = True
    
    color[1] = 0

    if isBipartite(adj, 1, visited, color):
        print("the graph is bipartite")
    else:
        print("the graph is not bipartite")


    