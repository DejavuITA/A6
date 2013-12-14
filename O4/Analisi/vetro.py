# -*- encoding: utf-8 -*-

import csv
from math import *
import matplotlib
from matplotlib import pyplot as plt

# Qui vanno i dati
# Angolo in radianti x
# Ia serie di conteggi
# IIa serie di conteggi

x = (
   0.017453292519943,
   0.034906585039887,
   0.052359877559830,
   0.069813170079773,
   0.087266462599716,
   0.104719755119660,
   0.122173047639603,
   0.139626340159546,
   0.157079632679490,
   0.174532925199433,
   0.191986217719376,
   0.209439510239320,
   0.226892802759263,
   0.244346095279206,
   0.261799387799149,
   0.279252680319093,
   0.296705972839036
)

y1 = (
   1.44984657079230,
   1.44969067131206,
   1.52565301436950,
   1.51280904030451,
   1.53113218009714,
   1.52403896181593,
   1.68677540140417,
   1.63559992571309,
   1.61536568471065,
   1.59052664644962,
   1.57435936896236,
   1.56346007712527,
   1.55588358523933,
   1.55999581928016,
   1.55802013357649,
   1.57263658613026,
   1.55622475382253
)

y2 = (
   1.44984657079230,
   1.53605260407964,
   1.48656460620855,
   1.51280904030451,
   1.56077924486781,
   1.54431020929403,
   1.69583155794910,
   1.63559992571309,
   1.63048842759440,
   1.59840508762739,
   1.59688627594641,
   1.61786113122443,
   1.62054718562792,
   1.61159866704016,
   1.60087761986471,
   1.59536460896196,
   1.58792541789783
)

# Creo un grafico, la dimensione è in pollici
f1 = plt.figure(figsize=(10, 7))
# Titolo del grafico
f1.suptitle("Indice di rifrazione in funzione dell'angolo di inclinazione del vetro",
    y=0.96, fontsize=16)

# GRAFICO 1
ax1 = f1.add_subplot(1, 1, 1)
# crea plot con le barre d'errore (o anche senza)
dots1 = ax1.errorbar(x=x, y=y2,
    #yerr=dy, #xerr=,
    fmt='+', c='red')
dots2 = ax1.errorbar(x=x, y=y1,
    #yerr=dy, #xerr=,
    fmt='x', c='black')
    
ax1.set_xlabel(u'Angolo [gradi]',
    labelpad=12, fontsize=14)
ax1.set_ylabel(u'Indice di rifrazione',
    labelpad=18, fontsize=14)

ax1.grid(True)
#ax1.set_ylim((1, 1.00022))
ax1.set_xlim((0, 0.32))

ax1.get_xaxis().set_ticklabels(["0", "0.05", "0.10", "0.15", "0.20", "0.25", "0.30"])
ax1.set_yticks([1.45, 1.50, 1.55, 1.60, 1.65, 1.70])

# questo produce una legenda
ax1.legend((dots1, dots2), ("Ia serie di punti", "IIa serie di punti"), 'upper left',
    prop={'size': 12})

# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.13, right=0.97,
    top=0.88, bottom=0.12, hspace=0, wspace=0.1)

labels = ax1.get_yticklabels()
for label in labels:
    label.set_rotation(0)
    
# mostra grafico
plt.show()  
