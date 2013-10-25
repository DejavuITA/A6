## -*- encoding: utf-8 -*-

import csv
from math import *

mpl = False
try:
    import matplotlib
    from matplotlib import pyplot as plt
    from scipy.misc import imread
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
    1.3980e-04,
    1.3821e-04,
    1.6286e-04,
    3.0668e-04,
    1.0383e-03,
    1.3067e-03,
    1.8431e-03,
    2.6026e-03,
    4.3632e-03,
    9.6295e-03,
    6.5170e-02,
    4.1163e-01,
    2.9884e+00
)

dQ = (
      1.8617e-06,
      1.9620e-06,
      2.2002e-06,
      2.7229e-06,
      1.3016e-05,
      8.3042e-06,
      1.1322e-05,
      1.6312e-05,
      2.6838e-05,
      1.2289e-04,
      5.5883e-04,
      5.6583e-03,
      6.7334e-02
)

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
dS = [sqrt((dq/p)**2 + (q*p*0.1/p**2)**2) for p, q, dq in zip(P2, Q[3:], dQ[3:])]
S_turbo = [Q[n]/p for n, p in enumerate(P_turbo)]
dS_turbo = [sqrt((dq/p)**2 + (q*p*0.1/p**2)**2) for p, q, dq in zip(P_turbo, Q[:10], dQ[:10])]

print Q
print
print "\n".join(map(str, P))
print 
print "\n".join(map(str, P2))
print
print "\n".join([str(s*3600) + "   " + str(sd * 3600) for s, sd in zip(S, dS)])
print
print "\n".join([str(s*1000) + "   " + str(sd * 1000) for s, sd in zip(S_turbo, dS_turbo)])

if mpl:
    f = plt.figure(figsize=(10, 7.5))
    f.suptitle("Pressione in funzione del tempo",
        y=0.96, fontsize=16)

    ax = f.add_subplot(1, 1, 1)
    ax.set_yscale('log')

    ax.errorbar(x=tempo[1500:], y=pressione[1500:],
        fmt="o", c="black")

    ax.set_ylabel(r'Pressione [Pa]',
        labelpad=6, fontsize=14)
    ax.set_xlabel(u'Tempo [s]',
        labelpad=6, fontsize=14)
    
    ax.grid(True)

    f.subplots_adjust(left=0.10, right=0.95,
        top=0.90, bottom=0.10, hspace=0.1)
    

    ### PLOT 2 ##################################################
    f1 = plt.figure(figsize=(10, 7.5))
    f1.suptitle(u"Velocità di pompaggio pompa rotativa",
        y=0.96, fontsize=16)

    ax1 = f1.add_subplot(1, 1, 1)
    ax1.set_xscale('log')
    #ax1.set_yscale('log')

    ax1.errorbar(x=P2, y=[s*1000 for s in S], yerr=[ds*1000 for ds in dS],
        fmt="o", c="black")

    ax1.set_xlabel(u'Pressione [Pa]',
        labelpad=6, fontsize=14)
    ax1.set_ylabel(u'Velocità di pompaggio S [$\\times 10^{-3}\; m^3 s^{-1}$]',
        labelpad=6, fontsize=14)
    
    ax1.set_ylim((0, 2))
    #ax1.set_xticks(("0", "10", "100", "1000", "10000"))
    ax1.grid(True)

    f1.subplots_adjust(left=0.10, right=0.95,
        top=0.90, bottom=0.10, hspace=0.1)

    ### PLOT 2 ##################################################
    f2 = plt.figure(figsize=(10, 7.5))
    f2.suptitle(u"Velocità di pompaggio pompa turbomolecolare",
        y=0.96, fontsize=16)

    ax2 = f2.add_subplot(1, 1, 1)
    ax2.set_xscale('log')
    #ax2.set_yscale('log')

    ax2.errorbar(x=P_turbo, y=[s*1000 for s in S_turbo], yerr=[ds*1000 for ds in dS_turbo],
        fmt="o", c="black")

    ax2.set_xlabel(u'Pressione [Pa]',
        labelpad=6, fontsize=14)
    ax2.set_ylabel(u'Velocità di pompaggio S [$\\times 10^{-3}\; m^3 s^{-1}$]',
        labelpad=6, fontsize=14)

    
    #ax2.set_xlim((1e-3, 0.25));
    #ax2.set_ylim((25, 50));
    ax2.grid(True)

    f2.subplots_adjust(left=0.10, right=0.95,
        top=0.90, bottom=0.10, hspace=0.1)

    plt.show()
