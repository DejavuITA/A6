# -*- encoding: utf-8 -*-

import uncertainties
from uncertainties import ufloat
from uncertainties.umath import *
from uncertainties import unumpy

import matplotlib
from matplotlib import pyplot as plt

import numpy as np

### ANALISI DATI ######################################################
dati = np.genfromtxt('../dati/dati.csv', delimiter=",")
v = dati[:,0]
pH = dati[:,1]
dpHdv = dati[1:,2]

ka = 1.622e-5
kw = 1e-14
c0 = 0.01015
c1 = 0.1
v0 = 100

def g(x):
    return ka/(10**-x + ka) + 1/c0*(kw/10**-x - 10**-x)

tpH = np.linspace(3, 11, 100)
gv = np.vectorize(g)
tv = gv(tpH) * c0 * v0 / c1

def h(x):
    return (ka/(10**-x + ka) + 1/c0*(kw/10**-x - 10**-x)) / (c1 / (c0*v0) - 1 / (c0*v0) * (kw/10**-x - 10**-x))

hv = np.vectorize(h)
hv = hv(tpH)

dh = [(p2-p1)/(v2-v1) for p1, p2, v1, v2 in zip(tpH[:-1], tpH[1:], hv[:-1], hv[1:])]

### GRAFICI ##########################################################

# Creo grafico
f1 = plt.figure(figsize=(9, 8), dpi=80)
# Titolo del grafico
f1.suptitle(u"Curva di titolazione",
    y=0.97, fontsize=15)

gs = matplotlib.gridspec.GridSpec(2, 1, height_ratios=[7.5, 2.5]) 
ax1 = plt.subplot(gs[0])
ax12 = plt.subplot(gs[1])

# crea plot con le barre d'errore (o anche senza)
punti = ax1.errorbar(x=v, y=pH,
        fmt='o--', c='black', linewidth=1)

curva_t = ax1.errorbar(x=tv, y=tpH,
    fmt='-', c='#13AC3F', linewidth=2, zorder=-1)

curva_h = ax1.errorbar(x=hv, y=tpH,
    fmt='-', c='#2683C1', linewidth=2, zorder=-1)

derivata = ax12.errorbar(x=v[1:], y=dpHdv,
    fmt='-', c='black', linewidth=2)

d_curva = ax12.errorbar(x=hv[1:], y=dh,
    fmt='-', c='#2683C1', linewidth=2, zorder=-1)

ax1.set_ylabel(u'Assorbanza',
    labelpad=12, fontsize=14)

ax1.grid(True)
ax12.grid(True)
#ax1.set_xscale('log')

ax1.set_ylim((3, 11))
ax1.set_xlim((0, 12))

ax12.set_ylim((0, 25))
ax12.set_xlim((0, 12))

#for label in ax1.get_xaxis().get_majorticklabels():
#  label.set_fontsize(14)
#for label in ax1.get_yaxis().get_majorticklabels():
#  label.set_fontsize(14)

#ax1.set_xticklabels((-50, -40, -30, -20, -10, ""))

#ax1.legend((line16, line32, line48, line64),
#        ("0.016 mmol/l", "0.032 mmol/l", "0.048 mmol/l", "0.064 mmol/l"),
#        'upper left', prop={'size': 15})

f1.subplots_adjust(left=0.1, right=0.97,
    top=0.92, bottom=0.1, hspace=0.1, wspace=0)

# mostra grafico
plt.show()
