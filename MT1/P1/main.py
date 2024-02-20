"""
n = # days
c = kWh consumption per day
p = kWh cost per day if no plan
q = kWh cost per day if one year plan
r = kWh cost per day if two year plan
s = kWg cost per day if five year plan
y = 365; number of days

Must run in O(n^1.8) assuming simple operations take O(1).
"""

import sys
import timeit

import matplotlib.pyplot as plt
import numpy as np

"""5452
0.10254559999999999"""

sys.setrecursionlimit(99999999)

n = 800
c = (2, 2, 3, 2) + n//4 * (2, 2, 3, 2)
p = (2, 5, 8, 10) + n//4 * (2, 5, 8, 10)
q = (4, 3, 4, 4) + n//4 * (4, 3, 4, 4)
r = (10, 9, 8, 7) + n//4 * (10, 9, 8, 7)
s = (10, 10, 10, 10) + n//4 * (10, 10, 10, 10)

cache = {}

"""def costs(i=0, x=0):
    if i >= n:
        return x

    xp = x + c[i] * p[i]
    xq = x + sum([c[k] * q[i] for k in range(i, min(n, i + 365))])
    xr = x + sum([c[k] * r[i] for k in range(i, min(n, i + 730))])
    xs = x + sum([c[k] * s[i] for k in range(i, min(n, i + 1825))])

    return min(costs(i + 1, xp), costs(i + 365, xq), costs(i + 730, xr), costs(i + 1825, xs))"""


def costs(i=0):
    if i in cache:
        return cache[i]
    if i >= n:
        return 0

    xp = c[i] * p[i]
    xq = sum([c[k] * q[i] for k in range(i, min(n, i + 365))])
    xr = sum([c[k] * r[i] for k in range(i, min(n, i + 730))])
    xs = sum([c[k] * s[i] for k in range(i, min(n, i + 1825))])

    cache[i] = min(xp + costs(i + 1), xq + costs(i + 365), xr + costs(i + 730), xs + costs(i + 1825))

    return cache[i]

"""tt = []
nn = []
n = 50
while n < 4000:
    c = (2, 2, 3, 2) + n//4 * (2, 2, 3, 2)
    p = (2, 5, 8, 10) + n//4 * (2, 5, 8, 10)
    q = (4, 3, 4, 4) + n//4 * (4, 3, 4, 4)
    r = (10, 9, 8, 7) + n//4 * (10, 9, 8, 7)
    s = (10, 10, 10, 10) + n//4 * (10, 10, 10, 10)
    start = timeit.default_timer()
    print(costs(), n)
    end = timeit.default_timer()
    tt.append(end - start)
    nn.append(n)
    n += 50
    cache.clear()

print(tt)
print(nn)

plt.scatter(nn, tt)
plt.scatter(nn, np.log(tt))
plt.show()"""


# exempel
n = 2
# förbukning
c = [2, 2] #, 3, 2]

# prices on different days
p = [2, 5]#, 8, 10] # rörlig
q = [4, 3]#, 4, 4] # bunden, 1 år
r = [10, 9]#, 8, 7] # bunden, 2 år
s = [10, 10]#, 10, 10] # bunden, 5 år

def minimumcost(n, c, p, q, r, s):

    # initialize dp array, n toma listor
    dp = [[0] * n for _ in range(n)]

    # For each day i from 1 to n,
    # we update dp[i][j] for each j as follows:
    for i in range(1, n):
        for j in range(n):

            # rörlig, antar oftast billigast
            min_cost = dp[i-1][j] + c[i]*p[i]

            if j != 0:
                # 1 år
                min_cost = min(min_cost, dp[i-1][j-1] + c[i] * q[i])
            if j > 1:
                # 2 år
                min_cost = min(min_cost, dp[i-1][j-2] + c[i] * r[i])
            if j > 3:
                # 5 år
                min_cost = min(min_cost, dp[i-1][j-3] + c[i] * s[i])

            dp[i][j] = min_cost

    # return minimum of last row of dp array
    print(dp)

print("The minimum cost is:", minimumcost(n, c, p, q, r, s))


