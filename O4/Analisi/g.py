# -*- encoding: utf-8 -*-

import csv
from math import *
import matplotlib
from matplotlib import pyplot as plt

# Qui vanno i dati
# Angolo in radianti

n = 1.00020044465812

x = (
   90,
   80,
   70,
   60,
   50,
   40,
   30,
   20,
   10
)

y = (
   1.8813e-05,
   4.1808e-05,
   6.1666e-05,
   8.1525e-05,
   1.0243e-04,
   1.1915e-04,
   1.4215e-04,
   1.6096e-04,
   1.7873e-04
)

np = [n - i for i in y]

nA =  2.01207494487750e-04
nB = -2.00002373426031e-09

B = -nB
A = 1

# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(10, 7))
# Titolo del grafico
f1.suptitle("Indice di rifrazione in funzione della pressione",
    y=0.96, fontsize=16)

# GRAFICO 1
ax1 = f1.add_subplot(1, 1, 1)
# crea plot con le barre d'errore (o anche senza)
dots = ax1.errorbar(x=x, y=np,
    #yerr=dy, #xerr=,
    fmt='o', c='black')
fit = ax1.errorbar(x=[i / 10 for i in range(1021)], y=[B * (i * 100) + A for i in range(1021)],
    #yerr=dy, #xerr=,
    fmt='-', c='gray')
    
ax1.set_xlabel(u'Pressione [kPa]',
    labelpad=12, fontsize=14)
ax1.set_ylabel(u'Indice di rifrazione',
    labelpad=18, fontsize=14)

ax1.grid(True)
ax1.set_ylim((1, 1.00022))
ax1.set_xlim((0, 102))

ax1.get_yaxis().set_ticklabels(["1", "1.00005", "1.00010", "1.00015", "1.00020"])

# questo produce una legenda
ax1.legend((dots, fit), ("Punti misurati", "Retta di fit"), 'upper left',
    prop={'size': 12})

# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.13, right=0.97,
    top=0.88, bottom=0.12, hspace=0, wspace=0.1)

labels = ax1.get_yticklabels()
for label in labels:
    label.set_rotation(45)
    
# mostra grafico
plt.show()  
