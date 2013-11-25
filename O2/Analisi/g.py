# -*- encoding: utf-8 -*-

import csv
from math import *

mpl = False
try:
    import matplotlib
    from matplotlib import pyplot as plt
    mpl = True
except:
    print "installa: sudo apt-get install python-matplotlib"

#entrata = []
#uscita = []

#with open('../Dati/deviazione.csv') as csvfile:
#    data = csv.reader(csvfile)
#
#    for n, row in enumerate(data):
#        if n != 0:
#            entrata.append(float(row[0]) + float(row[1]) / 60.0)
#            uscita.append(float(row[2]) + float(row[3]) / 60.0)

wavelengths = (
   643,
   635,
   610,
   508,
   480,
   467
)

index = (
    1.5149,
    1.5153,
    1.5159,
    1.5210,
    1.5229,
    1.5238
)

dindex = 0.0003

if mpl:
    f1 = plt.figure(figsize=(10, 7))
    f1.suptitle("Indice di rifrazione in funzione della lunghezza d'onda",
        y=0.96, fontsize=15)

    ax = f1.add_subplot(1, 1, 1)
    
    dots = ax.errorbar(x=wavelengths, y=index,
        yerr=dindex,
        fmt='o', c='black')
    teo = ax.errorbar(x=[i/10.0 for i in range(4500, 6500)], y=[1.5045 + 4205/(i/10.0)**2 + 1253108/(i/10.0)**4 for i in range(4500, 6500)],
        #yerr=sp,
        fmt='-', c='#555555')
    #fit = ax.errorbar(x=range(300, 365), y=[p0 * exp( - DH / (R * t)) for t in range(300, 365)],
        #xerr=sigma_res_p, yerr=sigma_res_l,
    #    fmt='-', c='#555555')

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

    ax.set_xlabel(u'Lunghezza d\'onda [nm]',
        labelpad=12, fontsize=14)
    ax.set_ylabel(u'Indice di rifrazione',
        labelpad=6, fontsize=14)
    ax.grid(True)
    #ax.set_xlim((30, 70))

    ax.legend((dots, teo), ("Punti misurati", "Predizione teorica"), 'upper right',
        prop={'size': 12})

    f1.subplots_adjust(left=0.1, right=0.95,
        top=0.90, bottom=0.10, hspace=0.1)

    plt.show()
else:
    print "Cazzo, istallati matplolib, coglione! Digita:\nSudo apt-get install python-matplotlib"
