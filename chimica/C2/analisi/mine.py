# -*- encoding: utf-8 -*-

import sys

import uncertainties
from uncertainties import ufloat
from uncertainties.umath import *
from uncertainties import unumpy

import util

import matplotlib
from matplotlib import pyplot as plt

import numpy as np
import scipy.optimize

### FUNZIONI UTILI ####################################################

class Data(object):
    def __init__(self):
        self.l = []
        self.A = []

    def get_max(self):
        max_A = 0
        max_n = 0
        for n, A in enumerate(self.A):
            if A > max_A:
                max_A = A
                max_n = n

        max_l = self.l[max_n]

        return max_l, max_A, max_n

# legge ed estrae i dati necessari
def get_data(filename):
    data = Data()

    started = False
    with open(filename) as f:
        for line in f:
            if line.strip() == "#DATA":
                started = True
                continue
            
            if started:
                l, A = map(float, line.split())
                data.l.append(l)
                data.A.append(A)

    return data

### ANALISI DATI ######################################################

# ora ricaviamo la lunghezza d'onda di picco
m160 = get_data("../dati/16_April_2014_15_30/cuso4.Sample.Raw.asc.txt")
l_max, A_max, n_max = m160.get_max()
print("Lunghezza d'onda di picco:", l_max, " -  Assorbanza:", A_max)

m16 = get_data("../dati/16_April_2014_16_58/0.016M.Sample.Raw.asc.txt")
m32 = get_data("../dati/16_April_2014_16_58/0.032M.Sample.Raw.asc.txt")
m48 = get_data("../dati/16_April_2014_16_58/0.048M.Sample.Raw.asc.txt")
m64 = get_data("../dati/16_April_2014_16_58/0.064M.Sample.Raw.asc.txt")
incognito = get_data("../dati/16_April_2014_16_58/incognito.Sample.Raw.asc.txt")

# Concentrazioni ed errori 
V_madre = ufloat(0.008, 0.00003)
C_madre = ufloat(0.5, 0.5*0.002)
V_figlia = ufloat(0.025, 0.0003)
C_figlia = V_madre * C_madre / V_figlia
print(C_figlia)

# Prova propagazione
#print(sqrt((0.00005*0.5/0.025)**2 + (0.008*0.001/0.025)**2 + (0.008*0.5/0.025**2*0.001)**2))

Vs = unumpy.uarray([0.001, 0.002, 0.003, 0.004], [0.00003, 0.00003, 0.00003, 0.00003])

V = ufloat(0.01, 0.0003)
C = Vs * C_figlia / V
print(C)

# Assorbanze
A = [m16.A[n_max], m32.A[n_max], m48.A[n_max], m64.A[n_max]]

# Fit
def retta(x, m):
    return m*x

print util.fit(unumpy.nominal_values(C), A, 11.6*unumpy.std_devs(C))
m, cov = scipy.optimize.curve_fit(retta, unumpy.nominal_values(C), A, sigma=(11.6*unumpy.std_devs(C))**-2)
print(m, cov)

chi2 = util.chi2_retta(m, 0, unumpy.nominal_values(C), A, 11.6*unumpy.std_devs(C))
print "chi2:", chi2

j = sqrt(chi2 / 3)
print j

old_C = C
u = np.sqrt((11.6*unumpy.std_devs(C)*j)**2 - (11.6*unumpy.std_devs(C))**2)
print u
C = unumpy.uarray( unumpy.nominal_values(C), unumpy.std_devs(C)*j)

m, cov = scipy.optimize.curve_fit(retta, unumpy.nominal_values(C), A, sigma=(11.6*unumpy.std_devs(C))**-2)
print(m, cov)

chi2 = util.chi2_retta(m, 0, unumpy.nominal_values(C), A, 11.6*unumpy.std_devs(C))
print "chi2:", chi2

# Ora ricaviamo la concentrazione dalla retta di fit
m = ufloat(m, 0.4279)
a = incognito.A[n_max]
c = a / m
print(a, c)

### GRAFICI ##########################################################

if len(sys.argv) == 1:
    # Creo grafico
    f1 = plt.figure(figsize=(10, 8), dpi=65)
    # Titolo del grafico
    f1.suptitle(u"Assorbanza del CuSO₄ in soluzione",
        y=0.97, fontsize=18)

    gs = matplotlib.gridspec.GridSpec(2, 1, height_ratios=[9, 1]) 
    ax1 = plt.subplot(gs[0])
    ax12 = plt.subplot(gs[1])

    # crea plot con le barre d'errore (o anche senza)
    line16 = ax1.errorbar(x=m16.l, y=m16.A,
        fmt='-', c='#AC1A13', linewidth=3)
    line32 = ax1.errorbar(x=m32.l, y=m32.A,
        fmt='-', c='#13AC3F', linewidth=3)
    line48 = ax1.errorbar(x=m48.l, y=m48.A,
        fmt='-', c='#2683C1', linewidth=3)
    line64 = ax1.errorbar(x=m64.l, y=m64.A,
        fmt='-', c='#FFC700', linewidth=3)

    ax1.set_ylabel(u'Assorbanza',
        labelpad=12, fontsize=16)

    ax1.grid(True)
    #ax1.set_xscale('log')

    #ax1.set_ylim((-25, 100))
    ax1.set_xlim((450, 950))

    for label in ax1.get_xaxis().get_majorticklabels():
      label.set_fontsize(14)
    for label in ax1.get_yaxis().get_majorticklabels():
      label.set_fontsize(14)

    #ax1.set_xticklabels((-50, -40, -30, -20, -10, ""))

    ax1.plot((825, 825), (0, 0.9), "-", linewidth=2, color="#bbbbbb", zorder=-3)
    ax1.text(x=815, y=0.91, s="825", fontsize=14)

    ax1.legend((line16, line32, line48, line64),
            ("0.016 mmol/l", "0.032 mmol/l", "0.048 mmol/l", "0.064 mmol/l"),
            'upper left', prop={'size': 15})
    
    clist = [
        (0, (0, 0, 1)),
        (0.16, (0, 1, 0)),
        (0.26, (1, 1, 0)),
        (0.32, (1, 0.5, 0)),
        (0.45, (1, 0, 0)),
        (0.6, (0, 0, 0)),
        (1, (0, 0, 0))
    ]
    
    cmap = matplotlib.colors.LinearSegmentedColormap.from_list('light_colors', clist, 256)
    
    g = np.outer(np.ones(10), np.arange(450, 951, 1))
    ax12.imshow(g, aspect='auto', cmap=cmap, origin="lower")
    
    ax12.set_xticks((50, 150, 250, 350, 450))
    ax12.set_yticks(list())
    ax12.set_xticklabels(("",))
    ax12.set_yticklabels(("",))
    
    ax12r = ax12.twiny()
    ax12r.set_xticks((0.1, 0.3, 0.5, 0.7, 0.9))
    ax12r.set_xticklabels(("",))
    
    ax12.text(400, 3.2, "Infrarosso", color="white", fontsize=16)
         
    ax12.set_xlabel(u'Lunghezza d\'onda [nm]',
        labelpad=12, fontsize=16)

    # questo imposta i bordi del grafico
    f1.subplots_adjust(left=0.08, right=0.98,
        top=0.91, bottom=0.07, hspace=0.08, wspace=0)


    # Creo grafico
    f2 = plt.figure(figsize=(10, 8), dpi=65)
    # Titolo del grafico
    f2.suptitle(u"Assorbanza in funzione della concentrazione a λ = 825 nm",
        y=0.97, fontsize=18)

    ax2 = f2.add_subplot(111)

    # crea plot con le barre d'errore (o anche senza)
    punti = ax2.errorbar(x=unumpy.nominal_values(C), y=A,
        xerr=unumpy.std_devs(old_C), yerr=u,
        fmt='o', c='white', ecolor='black', linewidth=1.5,
        markersize=7, markeredgewidth=1.5, capsize=4)
    reg = ax2.errorbar(x=(0, 0.07), y=(0, 0.07*m.nominal_value),
        fmt='-', c='#13AC3F', linewidth=3, zorder= -5)
        
    ax2.set_xlabel(u'Concentrazione [mmol/l]',
        labelpad=15, fontsize=16)

    ax2.set_ylabel(u'Assorbanza',
        labelpad=15, fontsize=16)

    ax2.grid(True)
    #ax1.set_xscale('log')

    ax2.set_ylim((0, 0.8))
    ax2.set_xlim((0, 0.07))

    for label in ax2.get_xaxis().get_majorticklabels():
      label.set_fontsize(14)
    for label in ax2.get_yaxis().get_majorticklabels():
      label.set_fontsize(14)

    ax2.set_yticklabels(("", 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8))
    ax2.set_xticklabels(("0", 10, 20, 30, 40, 50, 60, 70))

    incogn, = ax2.plot((0, c.nominal_value), (a, a), "-", linewidth=2, color="#aaaaaa", zorder=-8)
    ax2.plot((c.nominal_value, c.nominal_value), (a, 0), "-", linewidth=2, color="#aaaaaa", zorder=-8)

    ax2.legend((punti, reg, incogn),
            ("Punti sperimentali", "Regressione", "Soluzione incognita"),
            'upper left', prop={'size': 15})

    # questo imposta i bordi del grafico
    f2.subplots_adjust(left=0.1, right=0.97,
        top=0.9, bottom=0.1, hspace=0, wspace=0)


    # mostra grafico
    plt.show()
