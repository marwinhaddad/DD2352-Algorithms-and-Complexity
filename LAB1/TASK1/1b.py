import timeit as timeit
import sys
sys.setrecursionlimit(99999999)

n = 79
a = 5
b = 6
c = 7

def coins(x):
    if n < 0:
        return float("inf")
    elif n == 0:
        return 0
    return min(x, 1 + coins(x-a), 1 + coins(x-b), 1 + coins(x-c))


def main(x):
    t = []
    k = []
    for _ in range(1):
        start = timeit.default_timer()
        coins(x)
        t.append(timeit.default_timer()-start)
        k.append(x)
        print(x, t)
        x += 1

    print(t)
    print(k)

if __name__ == '__main__':
    main(n)
