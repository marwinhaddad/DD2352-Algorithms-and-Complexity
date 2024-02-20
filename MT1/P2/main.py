n = 4
d = [10, 15, 16, 11]
r = [8, 10, 4, 11]


def sorting(A, B):
    A.sort()
    B.sort(reverse=True)

    min_sum = float("inf")
    max_sum = -float("inf")

    for i in range(n):
        temp = A[i] + B[i]
        if temp > max_sum:
            max_sum = temp
        if temp < min_sum:
            min_sum = temp

    print(max_sum - min_sum)





