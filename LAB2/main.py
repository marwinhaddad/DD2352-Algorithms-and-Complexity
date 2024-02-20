import sys

V = int(sys.stdin.readline())
E = int(sys.stdin.readline())
m = int(sys.stdin.readline())

if V <= m or E == 0:
    output = '3\n' \
             '2\n' \
             '3\n' \
             '1 1\n' \
             '1 2\n' \
             '1 3\n' \
             '2 1 3\n' \
             '2 2 3'
else:
    edges = []
    for _ in range(E):
        a, b = (int(i) for i in sys.stdin.readline().split())
        edges.append((a, b))

    n = V + 2
    s = E + V + 1
    k = m + 2

    output = f'{n}\n{s}\n{k}\n1 1\n1 2'

    for _ in range(V):
        output += f'\n{m}'
        for i in range(3, k + 1):
            output += f' {i}'

    output += f'\n2 1 3\n2 2 3'

    for e in edges:
        output += f'\n2 {e[0]+2} {e[1]+2}'

    for i in range(4, n + 1):
        output += f'\n2 2 {i}'

print(output)

"""
def verifyColor(edges, colors):
    for edge in edges:
        if colors[edge[0]] == colors[edge[1]]:
            return False
    return True


print(verifyColor(edges, {1: 1, 2: 2, 3: 1, 4: 2}))"""
