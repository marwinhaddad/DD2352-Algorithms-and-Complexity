from itertools import combinations
from math import prod

def canGenerate(x, y):
    if len(x) == 1:
        return x[0] == y
    for i in range(len(x)):
        if (canGenerate(x[:i] + x[i + 1:], y - x[i])
                or canGenerate(x[:i] + x[i + 1:], y // x[i])):
            return True
    return False

def SSP(S, T):
    if T == 0:
        return True
    if not S:
        return False
    if S[0] <= T and SSP(S[1:], T - S[0]):
        return True

    return SSP(S[1:], T)

def reduceSSP2SPN(S, T):
    if sum(S) == T:
        for i in range(S):
            if S[i] < 0:
                S[i] *= -1
                T += S[i]
        return S, T
    
    
    return canGenerate(S, T)

S = [-3, 1, 2]
T = -3

print('Reduction:', reduceSSP2SPN(G, k))


