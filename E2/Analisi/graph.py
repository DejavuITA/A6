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

pressione_atm = 719 * 133.322
R = 8.3144

pressione = []
temperatura = []
sp =  671.26

A =  25.802
B = -5278.0
sA =  0.23529
sB =  82.333
chi_square =  10.000
p0 =  1.6055e+11
sp0 =  3.7775e+10
DH =  4.3883e+04
sDH =  684.55
T_ebb =  95.135
s_T_ebb =  8.3407

with open('../Dati/pressioni_vapore.csv') as csvfile:
    data = csv.reader(csvfile)

    for n, row in enumerate(data):
        if n != 0:
            pressione.append(pressione_atm + float(row[0]))
            temperatura.append(273.15 + float(row[1]))

if mpl:
    f1 = plt.figure(figsize=(11, 11))
    f1.suptitle("Pressione di vapore in funzione della temperatura", y=0.96, fontsize=15)

    gs = matplotlib.gridspec.GridSpec(2, 1, height_ratios=(3, 1))

    ax = f1.add_subplot(gs[0])
    
    dots = ax.errorbar(x=temperatura, y=pressione,
        #yerr=sp,
        fmt='o', c='black')
    fit = ax.errorbar(x=range(300, 365), y=[p0 * exp( - DH / (R * t)) for t in range(300, 365)],
        #xerr=sigma_res_p, yerr=sigma_res_l,
        fmt='-', c='#555555')

    #fit = ax.errorbar(x=range(300, 365), y=[(p0 + sp0) * exp( - (DH - sDH) / (R * t)) for t in range(300, 365)],
        #xerr=sigma_res_p, yerr=sigma_res_l,
    #    fmt='-')
    #fit = ax.errorbar(x=range(300, 365), y=[(p0 - sp0) * exp( - (DH + sDH) / (R * t)) for t in range(300, 365)],
        #xerr=sigma_res_p, yerr=sigma_res_l,
    #    fmt='-')

    #fit1 = ax.errorbar(x=(0, 1.4), y=(0, b*1.4))
    #fit2 = ax.errorbar(x=(0, 1.4), y=(0, 1.4/k0_s))
    #ax.errorbar(x=(0, 1.4), y=(0, (b-sigma_b)*1.4))
    #ax.errorbar(x=(0, 1.4), y=(0, (b+sigma_b)*1.4))

    #ax.set_xlabel(u'Temperatura [°C]', labelpad=12, fontsize=14)
    ax.set_ylabel(u'Pressione [kPa]', labelpad=6, fontsize=14)
    ax.grid(True)

    ax.set_xlim(303.15, 363.15)
    ax.set_xticks([t + 0.15 for t in range(303, 373, 10)])
    ax.get_xaxis().set_ticklabels([30, 40, 50, 60, 70, 80, 90])

    ax.set_ylim(0, 80000)
    ax.set_yticks(range(0, 90000, 10000))
    ax.get_yaxis().set_ticklabels(["", 10, 20, 30, 40, 50, 60, 70, 80])

    #ax.text(-0.03, -0.005, "0")

    #for n, l in enumerate(ax.get_ymajorticklabels()):
    #    print l.get_text()#.set_text(str(n*10))

    ax.legend((dots, fit), ("Punti misurati", "Regressione"), 'upper left',
        prop={'size': 12})

    ax2 = f1.add_subplot(gs[1])

    res = ax2.errorbar(x=temperatura, y=[(p - p0 * exp( - DH / (R * t))) / sp for p, t in zip(pressione, temperatura)],
            fmt='.', c='black')
    zero = ax2.errorbar(x=(300, 365), y=(0, 0),
            c="#555555")

    for p, t in zip(pressione, temperatura):
        plt.plot([t, t], [0, (p - p0 * exp( - DH / (R * t))) / sp], c="black")

    ax2.set_xlabel(u'Temperatura [°C]', labelpad=12, fontsize=14)
    ax2.set_ylabel(u'Residuo [σ]', labelpad=6, fontsize=14)
    ax2.grid(True)

    ax2.set_xlim(303.15, 363.15)
    ax2.set_xticks([t + 0.15 for t in range(303, 373, 10)])
    ax2.get_xaxis().set_ticklabels([30, 40, 50, 60, 70, 80, 90])

    ax2.set_yticks((-2, -1, 0, 1))

    f1.subplots_adjust(left=0.1, right=0.95, top=0.90, bottom=0.10, hspace=0.1)

    plt.show()
else:
    print "Cazzo, istallati matplolib, coglione! Digita:\nSudo apt-get install python-matplotlib"
