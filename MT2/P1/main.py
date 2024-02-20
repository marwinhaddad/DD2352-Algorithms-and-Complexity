from flobblerFile import checkFlobbler
from graphColor import checkColor
from itertools import combinations
import sys

'''
### REDUCTION FROM THE M GRAPH DECISION PROBLEM  ###

How can we represent the Flobbler input as a graph...

    n tasks     <=>     V vertices
    m workers   <=>     E edges
    m-k workers <=>     m colors
    N lists     <=>     E edges 
    
If a worker is shared between two tasks (vertices) add an edge between them.
'''

if __name__ == '__main__':

    # Read input
    V = int(sys.stdin.readline())
    E = int(sys.stdin.readline())
    m = int(sys.stdin.readline())
    edges = []
    G = [[0 for _ in range(V)] for _ in range(V)]
    for i in range(E):
        a, b = (int(x) for x in sys.stdin.readline().split())
        edges.append([a, b])
        G[a - 1][b - 1] = G[b - 1][a - 1] = 1
    colors = m

    if V <= m or E == 0 or m == 0:
        output = '1\n' \
                 '3\n' \
                 '0\n' \
                 '1 2 3'
        n = 1
        m = 3
        k = 0
        tasks = [[1, 2, 3]]

    else:
        n = V + 1
        m = E + 3
        k = V
        tasks = [[] for _ in range(n)]

        for i in range(1, n + 1):
            for j, e in enumerate(edges):
                if i in e:
                    tasks[i-1].append(j + 1)

        j = 1
        for task in tasks:
            for i in range(E + 1 + j, E + 1 + j + 3):
                task.append(i)
            j += 3

    print(n)
    print(m)
    print(k)
    for t in tasks:
        print(*t)

    print('Graph Color', checkColor(G, colors))
    print('Flobbler', checkFlobbler(n, m, k, tasks))
