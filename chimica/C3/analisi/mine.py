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

v0 = ufloat(100, 0.3)
veq = ufloat(10.15, 0.02)
c0 = veq * c1 / v0
print c0, c0 * 1.04

kA = 1.74e-5
pHi = ufloat(3.36, 0.003)
cp = (10**(-2*pHi) + kA*10**-pHi) / (kA)
print cp

per = 0.5 / (v0/2.0 - ufloat(5, 0.02)) 
semi = ufloat(pH[10], 0.003) + (ufloat(pH[11], 0.003) - ufloat(pH[10], 0.003)) * per
print semi, 10**-semi

### GRAFICI ##########################################################

# Creo grafico
f1 = plt.figure(figsize=(9, 9), dpi=70)
# Titolo del grafico
f1.suptitle(u"Curva di titolazione",
    y=0.97, fontsize=15)

gs = matplotlib.gridspec.GridSpec(2, 1, height_ratios=[8, 2.5]) 
ax1 = plt.subplot(gs[0])
ax12 = plt.subplot(gs[1])

# crea plot con le barre d'errore (o anche senza)
punti = ax1.errorbar(x=v, y=pH,
        fmt='o--', c='black', linewidth=2, zorder=5)

#curva_t = ax1.errorbar(x=tv, y=tpH,
#    fmt='-', c='#13AC3F', linewidth=2, zorder=-1)

curva_h = ax1.errorbar(x=hv, y=tpH,
    fmt='-', c='#2683C1', linewidth=3, zorder=2)

derivata = ax12.errorbar(x=v[1:], y=dpHdv,
    fmt='-', c='black', linewidth=2, zorder=5)

d_curva = ax12.errorbar(x=hv[1:], y=dh,
    fmt='-', c='#2683C1', linewidth=2, zorder=2)

ax1.set_ylabel(u'pH',
    labelpad=12, fontsize=14)

ax1.set_xlabel(u'Volume di soluzione titolanda versata [ml]',
    labelpad=6, fontsize=14)

ax12.set_ylabel(u'Derivata',
    labelpad=12, fontsize=14)

ax1.minorticks_on()
ax1.grid(b=True, which='major', color='0.7', linestyle='-', zorder=-5)
ax1.grid(b=True, which='minor', color='0.9', linestyle='-', zorder=-5)
ax1.set_axisbelow(True)

ax12.minorticks_on()
ax12.grid(b=True, which='major', color='0.7', linestyle='-', zorder=-5)
ax12.grid(b=True, which='minor', color='0.9', linestyle='-', zorder=-5)
ax12.set_axisbelow(True)
ax12.set_yscale('log')

ax1.set_ylim((3, 11))
ax1.set_xlim((0, 12))

ax12.set_ylim((0.1, 100))
ax12.set_xlim((0, 12))

ax12twin = ax12.twiny()
ax12twin.set_xticks([2*n for n in range(7)])
ax12twin.minorticks_on()

ax12.set_xticklabels([""] * 7)
ax12.set_yticks((0.1, 1, 10, 100))
ax12.set_yticklabels((0.1, 1, 10, 100))

bbox_props = dict(boxstyle="roundtooth,pad=0.5", fc="white", ec="black", lw=1)
ax1.annotate('Punto di\nequivalenza', xy=(10, 8.45),
    xytext=(8.5, 10), bbox=bbox_props, fontsize=13,
    arrowprops=dict(arrowstyle='->', connectionstyle="angle3,angleA=90", facecolor='black'),
    horizontalalignment='center', verticalalignment='top')

bbox_props = dict(boxstyle="roundtooth,pad=0.5", fc="white", ec="black", lw=1)
ax1.annotate('Punto di\nsemiequivalenza', xy=(5, 4.7),
    xytext=(7, 4), bbox=bbox_props, fontsize=13,
    arrowprops=dict(arrowstyle='->', connectionstyle="angle3,angleA=10,angleB=-90", facecolor='black'),
    horizontalalignment='center', verticalalignment='center')

#for label in ax1.get_xaxis().get_majorticklabels():
#  label.set_fontsize(14)
#for label in ax1.get_yaxis().get_majorticklabels():
#  label.set_fontsize(14)

#ax1.set_xticklabels((-50, -40, -30, -20, -10, ""))

ax1.legend((punti, curva_h),
        ("Punti sperimentali", "Andamento teorico"),
        'upper left', prop={'size': 14})

ax12.legend((derivata, d_curva),
        ("Sperimentale", "Teorica"),
        'upper left', prop={'size': 14})

f1.subplots_adjust(left=0.1, right=0.97,
    top=0.92, bottom=0.03, hspace=0.2, wspace=0)

# mostra grafico
plt.show()
