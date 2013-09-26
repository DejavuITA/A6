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

A = -0.0049373
B = 8.7446e+04
Pl = 9498

with open('../Dati/dati.csv') as csvfile:
    data = csv.reader(csvfile)

    for n, row in enumerate(data):
        if n != 0:
            pompate.append(float(row[0]))
            pressioni.append((730 - float(row[1])) * 133.322)

if mpl:
    f1 = plt.figure(figsize=(9, 6))
    f1.suptitle("Pressione in funzione del numero di pompaggi", y=0.93, fontsize=15)

    ax = f1.add_subplot(1, 1, 1)
    
    dots = ax.errorbar(x=pompate, y=pressioni,
        #xerr=sigma_res_p, yerr=sigma_res_l,
        fmt='o')
    fit = ax.errorbar(x=range(0, 1001), y=[Pl + B*exp(A*n) for n in range(0, 1001)],
        #xerr=sigma_res_p, yerr=sigma_res_l,
        fmt='-')

    #fit1 = ax.errorbar(x=(0, 1.4), y=(0, b*1.4))
    #fit2 = ax.errorbar(x=(0, 1.4), y=(0, 1.4/k0_s))
    #ax.errorbar(x=(0, 1.4), y=(0, (b-sigma_b)*1.4))
    #ax.errorbar(x=(0, 1.4), y=(0, (b+sigma_b)*1.4))

    ax.set_xlabel(u'Numero pompaggi', labelpad=12, fontsize=14)
    ax.set_ylabel(u'Pressione [Pa]', labelpad=6, fontsize=14)
    ax.grid(True)
    #ax.set_xticks((0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4))
    ax.set_yticks(range(10000, 110000, 10000))
    ax.set_ylim(5000, 105000)
    #ax.text(-0.03, -0.005, "0")

    #ax.legend((dots, fit1), ("Dati misurati", "Retta di fit"), 'upper left',
    #    prop={'size': 12})

    f1.subplots_adjust(left=0.13, right=0.93, top=0.85, bottom=0.13)

    plt.show()
else:
    print "Cazzo, istallati matplolib, coglione! Digita:\nSudo apt-get install python-matplotlib"
