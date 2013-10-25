## -*- encoding: utf-8 -*-

import csv

mpl = False
try:
    import matplotlib
    from matplotlib import pyplot as plt
    mpl = True
except:
    print "installati matplotlib!"

tempo = []
pressione = []

with open('../Dati/rotativa-Pressione.csv') as csvfile:
    data = csv.reader(csvfile)

    for n, row in enumerate(data):
        if n != 0:
            tempo.append(float(row[0]))
            pressione.append(float(row[1]) * 100)

N = (1, 2, 3, 4, 5, 5.2, 5.4, 5.6, 5.8, 6, 7, 8, 9)

Q = (
   1.3980e-06,
   1.3966e-06,
   1.6286e-06,
   3.0668e-06,
   1.0383e-05,
   1.3067e-05,
   1.8431e-05,
   2.6026e-05,
   4.3632e-05,
   9.6295e-05,
   6.5170e-04,
   4.1163e-03,
   2.9884e-02
)

dQ = (
   1.8617e-08,
   1.8197e-08,
   2.2002e-08,
   2.7229e-08,
   1.3016e-07,
   8.3042e-08,
   1.1322e-07,
   1.6312e-07,
   2.6838e-07,
   1.2289e-06,
   5.5883e-06,
   5.6583e-05,
   6.7334e-04
)

   1.3980e-04   1.8617e-06
   1.3821e-04   1.9620e-06
   1.6286e-04   2.2002e-06
   3.0668e-04   2.7229e-06
   1.0383e-03   1.3016e-05
   1.3067e-03   8.3042e-06
   1.8431e-03   1.1322e-05
   2.6026e-03   1.6312e-05
   4.3632e-03   2.6838e-05
   9.6295e-03   1.2289e-04
   6.5170e-02   5.5883e-04
   4.1163e-01   5.6583e-03
   2.9884e+00   6.7334e-02

def limit(da, a):
    return sum(pressione[da:a]) / (a - da);

P = (
    limit(1750, 1925),
    limit(2000, 2250),
    limit(2300, 2625),
    limit(2675, 2925),
    limit(3025, 3325),
    limit(3375, 3575)
)

P2 = (
    limit(4050, 4100),
    limit(4150, 4200),
    limit(4250, 4270),
    limit(4300, 4325),
    limit(4370, 4400),
    limit(4430, 4475),
    limit(4510, 4560),
    limit(4600, 4650),
    limit(4690, 4760),
    limit(4800, 4880)
)

P_turbo = (
    4.8e-3,
    4.8e-3,
    5e-3,
    8.5e-3,
    2.6e-2,
    3.2e-2,
    4.2e-2,
    5.5e-2,
    9e-2,
    2.1e-1
)

S = [Q[3 + n]/p for n, p in enumerate(P2)]

print Q
print
print "\n".join(map(str, P))
print 
print "\n".join(map(str, P2))
print
print "\n".join(map(str, [s for s in S]))

if mpl:
    f = plt.figure(figsize=(10, 7.5))
    f.suptitle("Pressione in funzione del tempo",
        y=0.96, fontsize=16)

    ax = f.add_subplot(1, 1, 1)
    ax.set_yscale('log')

    ax.errorbar(x=tempo[1500:], y=pressione[1500:],
        fmt="o", c="black")

    ax.set_ylabel(r'Pressine [Pa]',
        labelpad=6, fontsize=14)
    ax.set_xlabel(u'Tempo [s]',
        labelpad=6, fontsize=14)
    
    #ax.set_xlim((0, 10))
    ax.grid(True)

    f.subplots_adjust(left=0.10, right=0.95,
        top=0.90, bottom=0.10, hspace=0.1)

    plt.show()
