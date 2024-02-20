import sys
import timeit as timeit
import matplotlib.pyplot as plt
import numpy as np
sys.setrecursionlimit(999999999)

"""n = int(sys.stdin.readline())
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())"""

n = 1500000

"""def coins(x):
    if x in cache:
        return cache[x]
    if x < 0:
        return float("inf")
    elif n == 0:
        return 0
    cache[x] = min(n, 1 + coins(x-5), 1 + coins(x-6), 1 + coins(x-7))
    return cache[x]"""

"""n_vec = []
t_vec = []

for _ in range(5):
    cache = {}
    start = timeit.default_timer()
    coins(n)
    end = timeit.default_timer()
    print(n, end - start)
    n_vec.append(n)
    t_vec.append(end - start)
    n *= 2

print(n_vec)
print(t_vec)"""

n_vec = [1500000, 1500001, 1500002, 1500003, 1500004, 1500005, 1500006, 1500007, 1500008, 1500009, 1500010, 1500011, 1500012, 1500013, 1500014, 1500015, 1500016, 1500017, 1500018, 1500019, 1500020, 1500021, 1500022, 1500023, 1500024, 1500025, 1500026, 1500027, 1500028, 1500029, 1500030, 1500031, 1500032, 1500033, 1500034, 1500035, 1500036, 1500037, 1500038, 1500039, 1500040, 1500041, 1500042, 1500043, 1500044, 1500045, 1500046, 1500047, 1500048, 1500049, 1500050, 1500051, 1500052, 1500053, 1500054, 1500055, 1500056, 1500057, 1500058, 1500059, 1500060, 1500061, 1500062, 1500063, 1500064, 1500065, 1500066, 1500067, 1500068, 1500069, 1500070, 1500071, 1500072, 1500073, 1500074, 1500075, 1500076, 1500077, 1500078, 1500079, 1500080, 1500081, 1500082, 1500083, 1500084, 1500085, 1500086, 1500087, 1500088, 1500089, 1500090, 1500091, 1500092, 1500093, 1500094, 1500095, 1500096, 1500097, 1500098, 1500099]
t_vec = [1.0756335019996186, 0.9986475019995851, 1.0228385020000132, 0.992282802999398, 1.000239701999817, 1.003307302000394, 1.0073778039986792, 1.0058274190014345, 0.9981298189995869, 1.0390811190009117, 1.146298220999597, 1.3583709260001342, 0.9987441190005484, 1.018820819001121, 1.010257025998726, 1.548033924000265, 0.9944881720002741, 0.9882423710005241, 1.0000020749994292, 1.2453517409994674, 1.2765171060000284, 1.0135467830004927, 0.9980115850012226, 1.0037286860006134, 1.0032053860013548, 1.4620563720000064, 1.0752480999999534, 1.011316688000079, 1.0324053050007933, 1.0224862129998655, 0.9948796150001726, 1.5306867680010328, 1.0265377120013, 1.0361905119989387, 0.9934169150001253, 1.0046891559995856, 1.1747939260003477, 1.3849735310013784, 0.9951021220003895, 1.0210085229991819, 0.9917716230011138, 1.5349577350007166, 1.0426226170002337, 1.0122008130001632, 0.9937520139992557, 1.2622062169994024, 1.3037151170010475, 1.0108875129990338, 0.9924695139998221, 0.9955447160009498, 1.510883234001085, 1.0365673239994067, 1.0252453230004903, 1.023346722999122, 1.340087130000029, 1.1857808269996895, 1.0005912270007684, 0.9985474309996789, 1.011539430999619, 1.5165615459991386, 1.0179163299999345, 0.9886688300011883, 1.001656730999457, 1.355496549000236, 1.1398897500002931, 1.0314106459991308, 1.0275219449995348, 1.064025646999653, 1.0341589460003888, 1.0510955459994875, 1.1279817520007782, 1.0759381699990627, 1.0357776669989107, 1.0943120709998766, 1.033192066999618, 1.040788166999846, 1.0163169659990672, 1.0367126670007565, 1.1271434379996208, 1.0399638140006573, 1.0281709139999293, 1.0265700130003097, 1.0296213130004617, 1.0241866139986087, 1.0272357140001986, 1.0214681130000827, 1.020067517998541, 1.0245223189995158, 1.0932511200007866, 1.038594120000198, 1.0148641189989576, 1.0344831189995602, 1.1018327210003918, 1.0411114179987635, 1.0194485150004766, 1.0403592149996257, 1.0924920160014153, 1.038425714999903, 1.0105494139988878, 1.0432610150000983]

#n_vec = [1500000, 3000000, 6000000, 12000000, 24000000]
#t_vec = [1.0094568240019726, 2.012617587002751, 4.506957867000892, 8.576520111993887, 18.448722625995288]

plt.figure(2)
plt.plot(n_vec, np.log(t_vec), "-o")
plt.xlabel("Number of coins n")
plt.ylabel("Log Time in seconds s")
plt.title("Log Runtime as function of number of coins")

regreg = np.polyfit(n_vec, np.log(t_vec), 1)
print(regreg)

plt.figure(1)
plt.plot(n_vec, t_vec, "-o", label="Measured runtime")
plt.xlabel("Number of coins n")
plt.ylabel("Time in seconds s")
plt.title("Runtime as function of number of coins")
plt.legend()
plt.show()


