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

c = (
    0,
   20,
   25,
   30,
   35,
   40,
   50,
   60,
   70
)

I = (
   111.6,
    53.6,
    45.7,
    41.7,
    31.0,
    26.7,
    16.4,
    11.1,
     7.3
)

K =  0.036018
a =  111.988

#with open('../Dati/dati.csv') as csvfile:
#    data = csv.reader(csvfile)
#
#    for n, row in enumerate(data):
#        if n != 0:
#            pompate.append(float(row[0]))
#            pressioni.append((730 - float(row[1])) * 133.322)

if mpl:
    f1 = plt.figure(figsize=(10, 7))
    f1.suptitle("Intensità in funzione della concentrazione", y=0.95, fontsize=15)

    ax = f1.add_subplot(1, 1, 1)
    
    dots = ax.errorbar(x=c, y=I,
        yerr=0, fmt='o')
    fit = ax.errorbar(x=[x/10 for x in range(-20, 721)], y=[a * exp(-K*x/10) for x in range(-20, 721)], fmt='-')

    ax.set_xlabel(u'Concentrazioni [mol/l]', labelpad=12, fontsize=14)
    ax.set_ylabel(u"Intensità [$picodentotricotteri^\\frac{11}{7.5}$]", labelpad=6, fontsize=14)
    ax.grid(True)

    #ax.set_yticks(range(10000, 110000, 10000))
    #ax.set_ylim(5000, 105000)

    ax.set_xlim(-2, 72)
    #ax.set_xticks((0.2, 0.4, 0.6, 0.8, 1.0))

    ax.legend((dots, fit), ("Punti sperimentali", "Regressione"), 'upper right',
        prop={'size': 12})

    f1.subplots_adjust(left=0.1, right=0.95, top=0.88, bottom=0.13)

    plt.show()
else:
    print("Cazzo, istallati matplolib, coglione! Digita:\nSudo apt-get install python-matplotlib")
