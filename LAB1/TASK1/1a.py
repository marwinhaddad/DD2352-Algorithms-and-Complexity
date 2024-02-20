import timeit as timeit
import sys
import numpy as np
import matplotlib.pyplot as plt

sys.setrecursionlimit(99999999)

x = 80

def coins(n):
    if n < 0:
        return float("inf")
    elif n == 0:
        return 0
    return min(n, 1 + coins(n-5), 1 + coins(n-6), 1 + coins(n-7))

"""n_vec = []
t_vec = []
for _ in range(2):
    start = timeit.default_timer()
    coins(x)
    end = timeit.default_timer()
    t_vec.append(end - start)
    n_vec.append(x)
    print(x, end - start)
    x *= 2

print(n_vec)
print(t_vec)"""

n_vec = [79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
t_vec = [0.98332792097221, 1.080018762999316, 1.2977185549989372, 1.564921945999231, 2.428835321999941, 2.2690574539992667, 3.235794035001163, 3.274765975998889, 4.459927488000176, 5.255119604000356, 6.224047101999531, 7.819212739999784, 8.897382233999451, 10.703813312999046, 12.590732779000973, 15.017842504001237, 18.056706276000114, 21.67122731999916, 26.26180232900151, 31.129698972999904, 37.6281046740005]

plt.figure(2)
plt.plot(n_vec, np.log(t_vec), "-o")
plt.xlabel("Number of coins n")
plt.ylabel("Log Time in seconds s")
plt.title("Log Runtime as function of number of coins")

regreg = np.polyfit(n_vec, np.log(t_vec), 1)
print(regreg)

plt.figure(1)
# plt.plot(n_vec, t_vec, "-o", label="Measured runtime")
x_vec = [i*79 for i in range(2, 12, 2)]
print(x_vec)
plt.plot(x_vec, [(np.e ** regreg[0]) ** (i - 79) for i in x_vec], label="Calculated runtime")
plt.xlabel("Number of coins n")
plt.ylabel("Time in seconds s")
plt.title("Runtime as function of number of coins")
plt.legend()
plt.show()






