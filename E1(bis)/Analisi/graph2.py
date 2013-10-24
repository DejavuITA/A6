# -*- encoding: utf-8 -*-

import csv
from math import *

mpl = False
try:
    import matplotlib
    from matplotlib import pyplot as plt
    mpl = True
except:
    pass

pompate = []
pressioni = []
s_pressioni = 30*133.322 / sqrt(12)

A = -0.16396
sA =  7.5305e-04
b =  11.329
sb =  0.0036852
B =  8.7676e+04
sB =  306.53
chi =  827.94
Pl =  3913

with open('../Dati/membrana.csv') as csvfile:
    data = csv.reader(csvfile)

    for n, row in enumerate(data):
		pompate.append(float(row[0]) - 0.333)
		pressioni.append((730 - float(row[1])*2) * 133.322)

if mpl:
    f1 = plt.figure(figsize=(10, 7))
    f1.suptitle("Pressione in funzione del tempo", y=0.93, fontsize=15)

    ax = f1.add_subplot(1, 1, 1)
    
    dots1 = ax.errorbar(y=pressioni, x=pompate, yerr=s_pressioni, fmt='o')
    fit = ax.errorbar(x=[n-1 for n in range(0, 23)],
		y=[Pl + B*exp(A*(n-1)) for n in range(0, 23)],
        #xerr=sigma_res_p, yerr=sigma_res_l,
        fmt='-')

    #fit1 = ax.errorbar(x=(0, 1.4), y=(0, b*1.4))
    #fit2 = ax.errorbar(x=(0, 1.4), y=(0, 1.4/k0_s))
    #ax.errorbar(x=(0, 1.4), y=(0, (b-sigma_b)*1.4))
    #ax.errorbar(x=(0, 1.4), y=(0, (b+sigma_b)*1.4))

    ax.set_xlabel(u'Tempo [s]', labelpad=12, fontsize=14)
    ax.set_ylabel(u'Pressione [Pa]', labelpad=6, fontsize=14)
    ax.grid(True)
    #ax.set_xticks((0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4))
    #ax.set_yticks(range(10000, 110000, 10000))
    ax.set_xlim(-0.5, 21)
    ax.set_ylim(0, 1e5)
    #ax.set_ylabels((10, 20, 30, 40, 50, 60, 70, 80, 90, 100))
    #ax.text(-0.03, -0.005, "0")

    ax.legend((dots1, fit), ("Dati usati per il fit", "Regressione"), 'upper right',
        prop={'size': 12})

    f1.subplots_adjust(left=0.13, right=0.93, top=0.85, bottom=0.13)

    plt.show()
else:
    print "Cazzo, istallati matplolib, coglione! Digita:\nSudo apt-get install python-matplotlib"
