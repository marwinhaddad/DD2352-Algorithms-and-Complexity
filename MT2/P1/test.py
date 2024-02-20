import sys
from itertools import combinations

def VertexCover(V, edges, k):
    for subset in combinations(range(V), k):
        seen = set()
        for this in subset:
            for edge in edges:
                if this in edge:
                    seen.add(edge[this is edge[0]])
        if len(seen) == V:
            return True
    return False

def Flobbler(n, m, k, tasks):
    for fired in combinations(range(1, m + 1), k):
        newTasks = []
        for i in range(n):
            keptEmployees = []
            for employee in tasks[i]:
                if employee not in fired:
                    keptEmployees.append(employee)
            newTasks.append(keptEmployees)

        count = 0
        for task in newTasks:
            if len(task) >= 3:
                count += 1

        if count == n:
            print(fired)
            return True
    return False

def VC2F(V, E, kv, edges):

    if V <= kv or E <= kv:
        n = 1
        m = 4
        k = 1
        tasks = [[1, 2, 3, 4]]

    else:
        n = E
        m = V + 2
        k = V - kv

        tasks = []
        for e in edges:
            tasks.append([i for i in e])

        for task in tasks:
            for i in range(V + 1, m + 1):
                task.append(i)

    return n, m, k, tasks


def main():

    V = int(sys.stdin.readline())
    E = int(sys.stdin.readline())
    k = int(sys.stdin.readline())
    edges = []
    for _ in range(E):
        a, b = (int(i) for i in sys.stdin.readline().split())
        edges.append([a, b])

    print()
    print('Vertex Cover:', VertexCover(V, edges, k))

    flobblerInput = VC2F(V, E, k, edges)
    print(flobblerInput)

    print('Flobbler:', Flobbler(*flobblerInput))


if __name__ == '__main__':
    main()


