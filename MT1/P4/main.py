

def BFS(G, F, source, sink, N):
    q = [source]
    visited = [1] + [0] * (N-1)
    while q:
        u = q.pop(0)
        for i in range(N):
            if visited[i] == 0 and G[u][i] > 0:
                q.append(i)
                visited[i] = 1
                F[i] = u
                if i == sink:
                    return True
    return False


def EdmondsKarp(G, source, sink):
    N = len(G)
    F = [0] * N
    f_max = 0

    while BFS(G, F, source, sink, N):
        f_path = float("inf")
        s = sink
        while s != source:
            f_path = min(f_path, G[F[s]][s])
            s = F[s]

        f_max += f_path
        v = sink
        while v != source:
            u = F[v]
            G[u][v] -= f_path
            G[v][u] += f_path
            v = u

    return f_max


def d(this, that):
    return ((this[0] - that[0]) ** 2 + (this[1] - that[1]) ** 2) ** 0.5


def CreateAM(n, p, l, m, c, r, d_max):
    G = [[0] * (n + m + 2) for _ in range(n + m + 2)]

    for i in range(n):
        G[0][i + 1] = p[i]
        for j in range(m):
            if d(l[i], r[j]) <= d_max:
                G[i + 1][n + 1 + j] = p[i]
            G[n + 1 + j][n + m + 1] = c[j]

    return G


def CanGetLunch(n, p, l, m, c, r, d_max):
    G = CreateAM(n, p, l, m, c, r, d_max)
    source = 0
    sink = n+m+1
    p_tot = sum(p)
    f_max = EdmondsKarp(G, source, sink)
    print(p_tot, f_max)
    return p_tot == f_max


D = 100
N = 4
P = [42, 20, 11, 7]
L = [(0, -1), (0, 0), (0, 1), (0, 2)]
M = 2
C = [42, 42]
R = [(2, -1), (2, 1)]

print(CanGetLunch(N, P, L, M, C, R, D))


