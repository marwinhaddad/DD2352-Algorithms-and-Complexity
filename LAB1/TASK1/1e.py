import sys
import timeit
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline
sys.setrecursionlimit(2147483647)

cache = {}

def coins(n):
    if n in cache:
        return cache[n]
    if n < 0:
        return float("inf")
    elif n == 0:
        return 0
    cache[n] = min(n, 1 + coins(n-5), 1 + coins(n-6), 1 + coins(n-7))
    return cache[n]


def main():
    global cache
    """n = 1500000

    t = []
    x = []
    for _ in range(500):
        start = timeit.default_timer()
        coins(n)
        t.append(timeit.default_timer() - start)
        x.append(n)
        print(x[-1], t[-1])
        n += 1
        cache.clear()

    print(x)
    print(t)"""

    x = range(1500000, 1500000+500)
    t = [1.0611541999996916, 0.9902007000000594, 1.0218420990004233, 0.9856249000004027, 1.0033366009993188, 0.9836089000000356, 0.998984701000154, 1.179613001000689, 1.3291074019998632, 0.9827029999996739, 0.9952790010001991, 0.9837148019996675, 1.518625704000442, 1.0150010030001795, 1.1022679019997668, 0.9846123019997322, 1.2547351029998026, 1.2232010040006571, 1.0115384029995766, 0.9912071030003062, 0.99010870300026, 1.5006753050001862, 1.0110876030003055, 0.9873017030004121, 0.9833989030003067, 1.225628205999783, 1.2644097089996649, 0.9903563059997396, 1.0041785059993344, 0.9884712069997477, 1.5075881100001425, 0.9806290070000614, 0.9940827130003527, 0.999504221999814, 1.2344998280004802, 1.2985976290001418, 1.0351842230002148, 1.0011344220001774, 1.006754221999472, 1.4893107990001226, 1.009345024999675, 1.0129519239999354, 1.0163222260007387, 1.3219470620006177, 1.2043042479999713, 1.0560837299999548, 1.0071994099998847, 1.0537306030000764, 1.4235331050003879, 0.9848315030003505, 1.0102923029999147, 1.0004258030003257, 1.4015954040005454, 1.075435607000145, 1.016768208999565, 0.9883459089996904, 1.0540438099997118, 1.4076733129995773, 0.9946368089995303, 1.0819689100007963, 0.9875007090004146, 1.400803910999457, 1.068710407999788, 0.9788560079996387, 0.9748143070000879, 1.0238057079995997, 1.4402767120000135, 0.9709297919998789, 0.9797643599995354, 0.9753534599994964, 0.970004660000086, 1.190977749999547, 1.2906884470003206, 0.9898697589997028, 0.9704286600008345, 0.9713203969995448, 0.9787988020007106, 0.9740297029993599, 0.9970453019996057, 0.9704734019996977, 1.4992855039999995, 0.9755345020003006, 0.979283905999182, 0.9779834109995136, 1.1699999139991633, 1.3033819160000348, 0.9889787120000619, 0.9699544109998897, 0.9752329120001377, 0.9771808120003698, 0.9671509170002537, 1.174328821999552, 1.341075025000464, 0.9915515189995858, 0.975402218000454, 0.9702967180000996, 1.3640903250006886, 1.077394443999765, 0.9749185589998888, 0.9903694639997411, 0.9733493590001672, 1.4758805920000668, 0.9616682280002351, 0.9700580099997751, 0.9929541129995414, 0.963335016000201, 0.9730218149998109, 0.9633818150005027, 1.4925132239995946, 0.9645105159997911, 0.967131115000484, 0.9602432150004461, 0.9806059180000375, 0.993954518999999, 0.965138818000014, 1.3764055259998713, 1.13342282099984, 0.9827514190001239, 0.9678178180001851, 1.01821512800052, 1.4005420599996796, 0.976945841000088, 0.9580844410002101, 0.9551201410004069, 1.2741208549996372, 1.1852332500002376, 0.9977024789995994, 0.9587071729993113, 0.9655641749995993, 1.4717661659997248, 0.9830115780005144, 0.9692822749993866, 0.964021574999606, 1.0017724809995343, 0.9773628500006453, 0.9979445079998186, 0.9747387080005865, 1.2692249100000481, 1.166612609999902, 0.9693106080003417, 0.9542569080003886, 0.9541231080002035, 0.9973295100007817, 1.3966333150001446, 1.0944126119993598, 0.9985521110002082, 0.9621626100006324, 0.9633084110000709, 1.4770944089996192, 0.9963217690001329, 0.9740011699996103, 0.9593074699996578, 1.1417492649998167, 1.2701710609999282, 0.9996568690003187, 0.9668670700002622, 0.9598726919994078, 0.9595554049992643, 0.9803320049995818, 0.9511729050000213, 0.9541731050003364, 1.4416030080001292, 0.9913739059993532, 0.9624831049995919, 0.9623077070000363, 0.9892034069998772, 0.9656458079998629, 0.9596493070002907, 0.9850733069997659, 0.9716093079996426, 0.962599307000346, 0.9799988069999017, 1.4353443169993625, 1.1002356130002227, 0.9843274120003116, 0.9797209119997206, 1.0554301120000673, 1.3540609159999804, 0.9737025109998285, 0.9627337140000236, 0.9665225139997347, 0.9571642139999312, 0.9543112139999721, 1.0123667150000983, 0.957851613999992, 0.9558034140000018, 1.1866373180000664, 1.2367967210002462, 0.9926928160002717, 0.9656434160006029, 0.9641847160000907, 1.4015667229996325, 1.0231576170008339, 0.9522373159998097, 0.9652334150005117, 1.0033609149995755, 1.4324191219993736, 0.9771693150005376, 0.9529366149999987, 0.9586432149999382, 0.9903651160002482, 1.1387502179995863, 1.3689043229996969, 0.9582702160005283, 0.962032716000067, 0.9621841160005715, 1.2841282210001737, 1.137226918000124, 0.969944315000248, 0.9572754689997964, 0.9552164689994243, 1.0026188679994448, 1.03503156700026, 1.0665155650003726, 1.0808660650000093, 1.0492574660001992, 1.057964573999925, 1.0763586919993031, 1.0671762919992034, 1.0584195910005292, 1.2876715900001727, 1.21437879000041, 1.087488191000375, 1.112400795999747, 1.2429285039997922, 1.0363152039999477, 1.0585475039997618, 1.3156693049995738, 1.1281440040002053, 1.028304303999903, 1.034797408000486, 1.0199929160007741, 1.0451965169995674, 1.0139170160000504, 1.0192008159992838, 1.0274752160003118, 1.0114185160000488, 1.0278430159996788, 1.0602826160002223, 1.0750476169996546, 1.0110349159995167, 1.0051975160004076, 1.0033681149998301, 1.0022084149995862, 1.0094685160001973, 0.99878601599994, 0.9999270409998644, 0.993532241000139, 1.0203510290002669, 0.9884701439996206, 1.0009980699996959, 0.9913779110001997, 0.9857547100000374, 0.9889325109998026, 0.9827689100002317, 1.0168470099997649, 0.9901678100004574, 0.9825260100005835, 0.9797885099997075, 0.9833120110006348, 1.003758210000342, 0.9749098120000781, 0.9710719240001708, 1.00685702499959, 1.2649837320004735, 0.9981711250002263, 0.9777673239996147, 0.985522425000454, 1.0547088260000237, 0.9880447209998238, 1.076166918999661, 1.0914680190007857, 0.9843753170007403, 1.0396042180000222, 0.9896227170002021, 0.977090216999386, 1.026460718000635, 0.9877433169995129, 0.9866596159999972, 0.9968083159992602, 0.9878524160003508, 1.0161524169998302, 0.9858743160002632, 0.9952097169998524, 0.9872143160000633, 0.9846884100006719, 1.0000462099997094, 0.9788076100003309, 0.9870323089999147, 0.9922063089998119, 0.9809662090001439, 0.9978232099992965, 0.9715971099994931, 0.9702590699998836, 1.2602169589999903, 0.9934139679999134, 0.9771624680006425, 1.041123166000034, 0.9861488669994287, 0.985922567999296, 0.978390171000683, 0.9955826789991988, 0.9812534789998608, 0.9773485790001359, 0.9780651789997137, 0.9768663790000573, 1.045955977999256, 0.9802002790002007, 0.9843530779999128, 0.987450976999753, 0.9758217769995099, 1.0101468769998974, 0.9871387769999274, 0.9891441769996163, 0.9861602770006357, 0.9892000760000883, 1.0070693819998269, 0.976037290000022, 0.9827211910005644, 0.9844896900003732, 0.9768306899995878, 1.01333029000034, 0.9801091910003379, 0.9853816900003949, 0.9842825949999678, 0.9806831999994756, 1.2025460009999733, 1.119039700999565, 0.9909281010004634, 0.978035600000112, 0.9867494009995426, 0.986371001000407, 0.9971147940004812, 1.026157193000472, 0.9846052930006408, 1.0345902929993827, 0.9857733929993628, 0.9938712930006659, 0.9919365929999913, 0.9840605930003221, 0.9784585969991895, 0.9710300979995736, 1.0010644980002326, 0.9719140970000808, 0.9739849979996507, 0.9845326979993843, 0.9747034970005188, 1.0111111980004353, 0.9822006989998044, 0.9924787999998443, 0.9787416999997731, 0.98970799899962, 0.9822866999993494, 0.98407109999971, 1.017603799000426, 1.2616977550005686, 1.054639615999804, 1.0028706249995594, 1.0045465250004781, 0.9863413290004246, 0.9880724279992137, 0.9972257800000079, 0.9886779889993704, 1.016829148999932, 0.9919141269992906, 0.9825824409999768, 0.9856068580002102, 0.9797567870000421, 0.9855501870006265, 0.9759062869998161, 1.000776887000029, 0.9763712940002733, 0.9803238009999404, 0.9783032019995517, 0.9781306009999753, 0.9979289009997956, 0.971084601000257, 0.9733019010000135, 0.9688355010002851, 0.9712809769998785, 1.1856741990004593, 1.0817655290002222, 0.998519772999316, 0.9842882630000531, 0.9877155650001441, 0.9818547790000594, 1.0623172850000628, 1.0275184870006342, 0.9925496880005085, 0.9852600869999151, 0.977262786999745, 1.0133786870001131, 0.9770984870001485, 0.9695973880006932, 1.008551787000215, 0.9718022540000675, 1.007958860999679, 0.9793606590001218, 0.9922122589996434, 1.2800078770005712, 1.148832369000047, 0.9569641569996747, 0.956215641000199, 0.9798341129999244, 0.9558426129997315, 0.959660014000292, 0.9906922140007737, 0.983960212999591, 0.9830241130002833, 0.9840236130003177, 0.983220913999503, 1.1151537189998635, 1.1081772190000265, 0.9876504170006228, 0.9656490170000325, 1.0219417169992084, 0.9959373170004255, 0.9718809169999076, 0.9838185649996376, 0.9782822940005644, 1.3518863299996156, 1.1898150139995778, 1.0135772980002002, 0.9608723930004999, 0.9856684950000272, 1.4387149929998486, 0.9621333260001848, 0.9518194259999291, 0.9499629259998983, 0.9875865270005306, 1.0061172279993116, 1.4273362390003967, 0.9540754280005785, 0.9533075829995141, 0.9572741840001981, 0.952559382999425, 1.084654693999255, 1.4396270259994708, 0.9651110840004549, 0.9673276840003382, 0.9853000560005967, 0.9857146249996731, 1.00728642499962, 1.0368930249996993, 1.0306229249999888, 0.986438525000267, 0.9872955239998191, 0.9819476239999858, 0.9779454090003128, 1.0067739000005531, 0.9766799000008177, 0.9958232999997563, 0.9806244000001243, 0.9750567999999475, 0.9939809999996214, 0.9672482000005402, 0.9729202899998199, 0.9915805830005411, 0.9639473839997663, 0.9675975840000319, 0.9686966839999513, 1.1732289800002036, 1.2506337790000543, 0.9712693840001521, 0.953226292999716, 0.9603213930004131, 1.3818927900001654, 1.0437697919996936, 1.0250014919993191, 0.9741321930005142, 0.9854955930004508, 1.4441144799993708, 1.0176623779998408, 0.9738482829998247, 0.9717902829997911, 1.2990599430004295, 1.1265617640001437, 0.9761905820005268, 0.9514185330008331, 0.9491982939998707, 0.996887094000158, 0.9609293940002317, 0.9536249940001653, 0.995223494000129, 1.0048114940000232, 1.006440694000048, 0.9884206010001435, 1.0019115759996566, 0.9867144789996019, 0.9941553770004248, 0.9906578780000928, 0.9831815799998367, 1.012963772999683, 0.981546680000065, 0.9832710959999531, 1.2168928069995673, 1.0226789059997827, 0.9878131049999865, 0.9898769050005285, 0.9862776059999305]

    # x = [x[i] for i, k in enumerate(t) if k < 1.1]
    # t = [t[i] for i, k in enumerate(t) if k < 1.1]
    plt.figure(0)
    plt.scatter(x, t, label="Measured runtime")
    plt.title("Runtime as function of number of coins")
    plt.xlabel("Number of coins n")
    plt.ylabel("Time in seconds s")
    plt.show()

    """print()

    n = 2500000
    k = n // 2
    t = []
    x = []
    for _ in range(3):
        start = timeit.default_timer()
        g(n)
        t.append(timeit.default_timer() - start)
        x.append(n)
        print(x[-1], t[-1])
        n *= 2
        k = n // 2
        cache.clear()

    print(x)
    print(t)"""

    """reg = CubicSpline(x, t)

    plt.figure(1)
    plt.plot(x, t, "-o", label="Measured runtime")
    plt.plot(np.linspace(x[0], x[-1], 100000), reg(np.linspace(x[0], x[-1], 100000)), label="Interpolated runtime")
    plt.title("Runtime as function of number of coins")
    plt.xlabel("Number of coins n")
    plt.ylabel("Time in seconds s")
    plt.legend()

    plt.figure(2)
    plt.plot(x, np.log(t), "-o", label="Measured runtime")
    plt.plot(np.linspace(x[0], x[-1], 100000), np.log(reg(np.linspace(x[0], x[-1], 100000))), label="Interpolated runtime")
    plt.title("Log Runtime as function of number of coins")
    plt.xlabel("Number of coins n")
    plt.ylabel("Log Time in seconds s")
    plt.legend()
    plt.show()"""


if __name__ == '__main__':
    main()