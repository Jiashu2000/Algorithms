# Floyd Warshall Algorithm

'''
This algorithm is highly efficient and can handle graphs with both positive and negative edge weights
can handle both posiitve and negative edges

But, it does not work for the graphs with negative cycles (where the sum of the edges in a cycle is negative).


Pseudo Code
    for k = 0 to n-1:
    for i = 0 to n-1:
    for j = 0 to n-1:
        distance[i, j] = min(distance[i,k] + distance[k, j], distance[i, j])
'''

V = 4

INF = 999

def floydWarshall(graph):

    dist = list(map(lambda i : list(map(lambda j: j, i)), graph))

    for k in range(V):

        for i in range(V):

            for j in range(V):

                dist[i][j] = min(dist[i][k] + dist[k][j], dist[i][j])
    
    printSolution(dist)

def printSolution(dist):
    print("Following matrix shows the shortest distances\
 between every pair of vertices")
    for i in range(V):
        for j in range(V):
            if(dist[i][j] == INF):
                print("%7s" % ("INF"), end=" ")
            else:
                print("%7d\t" % (dist[i][j]), end=' ')
            if j == V-1:
                print()
 
# Driver's code
if __name__ == "__main__":
    """
                10
           (0)------->(3)
            |         /|\
          5 |          |
            |          | 1
           \|/         |
           (1)------->(2)
                3           """
    graph = [[0, 5, INF, 10],
             [INF, 0, 3, INF],
             [INF, INF, 0,   1],
             [INF, INF, INF, 0]
             ]
    # Function call
    floydWarshall(graph)

'''
time complexity: o(v^3)
space complexity: o(v^2)
'''