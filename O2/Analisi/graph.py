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

entrata = (
   0.54527,
   0.58061,
   0.61421,
   0.64126,
   0.66715,
   0.67617,
   0.69304,
   0.71108,
   0.72853,
   0.75471,
   0.78991,
   0.81623,
   0.84198,
   0.86932,
   0.88546,
   0.91252,
   0.93797,
   0.96400,
   0.99033,
   1.01651,
   1.06014,
   1.10334,
   1.14726
)

entrata = [a * 180 / 3.1415 for a in entrata]

uscita = (
   0.85754,
   0.79791,
   0.76155,
   0.74060,
   0.73013,
   0.72053,
   0.71239,
   0.72286,
   0.69959,
   0.69260,
   0.68679,
   0.68271,
   0.68097,
   0.68097,
   0.68126,
   0.68301,
   0.68504,
   0.68911,
   0.69464,
   0.69988,
   0.71122,
   0.72518,
   0.74206
)

uscita = [a * 180 / pi for a in uscita]

previsione = (
   0.86335,
   0.80077,
   0.76375,
   0.74212,
   0.72599,
   0.72121,
   0.71325,
   0.70599,
   0.70007,
   0.69294,
   0.68623,
   0.68310,
   0.68141,
   0.68099,
   0.68137,
   0.68297,
   0.68554,
   0.68919,
   0.69389,
   0.69954,
   0.71107,
   0.72504,
   0.74179
)

previsione = [a * 180 / pi for a in previsione]

dom_prev = [float(i)/10.0 for i in range(300, 711)]
alpha = 60.0 / 180 * pi
n = 1.5210
prev = [(th_i/180*pi + asin(n * sin(alpha - asin(sin(th_i/180*pi) / n))) - alpha) for th_i in dom_prev]
prev = [a * 180 / pi for a in prev]

if mpl:
    f1 = plt.figure(figsize=(10, 7))
    f1.suptitle("Angolo di deviazione in funzione dell'angolo di incidenza",
        y=0.96, fontsize=15)

    ax = f1.add_subplot(1, 1, 1)
    
    dots = ax.errorbar(x=entrata, y=uscita,
        #yerr=4.1138e-04*180/pi,
        fmt='o', c='black')
    teo = ax.errorbar(x=dom_prev, y=prev,
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

    ax.set_xlabel(u'Angolo di incidenza [gradi]',
        labelpad=12, fontsize=14)
    ax.set_ylabel(u'Angolo di deviazione [gradi]',
        labelpad=6, fontsize=14)
    ax.grid(True)
    ax.set_xlim((30, 70))
    
    ax.annotate('Misure errate', ((40.8, 41.7)), xytext=(-20, 80), 
            textcoords='offset points', arrowprops=dict(arrowstyle='-|>', connectionstyle="arc3,rad=0.2"))        
    ax.annotate('', ((38.4, 42)), xytext=(30, 70), 
            textcoords='offset points', arrowprops=dict(arrowstyle='-|>', connectionstyle="arc3,rad=-0.2"))

    ax.legend((dots, teo), ("Punti misurati", "Predizione teorica"), 'upper right',
        prop={'size': 12})

    f1.subplots_adjust(left=0.1, right=0.95,
        top=0.90, bottom=0.10, hspace=0.1)

    plt.show()
else:
    print "Cazzo, istallati matplolib, coglione! Digita:\nSudo apt-get install python-matplotlib"
