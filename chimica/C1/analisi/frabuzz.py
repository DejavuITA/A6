from math import *			# da math importo tutto # non devo utilizzare il namespace (es: np per numpy)

from matplotlib import *		# da matplotlib importo tutto # non devo utilizzare il namespace (es: np per numpy)
import matplotlib.pyplot as plt
import numpy as np			# importo numpy come np

from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA

data = np.genfromtxt("../dati/dati.csv", delimiter=',', names=True)
ml = data['millilitri']
s = data['conducibilita']

dy_corr = (
   0.010000,
   0.010000,
   0.010000,
   0.010000,
   0.010000,
   0.010000,
   0.010000,
   0.010000,
   0.010000,
   0.010000,
   0.010000,
   0.010000,
   0.010000,
   0.30000,
   0.30000,
   0.30000,
   0.30000,
   0.30000,
   0.30000,
   0.30000,
   0.30000,
   0.30000,
   0.30000,
   0.30000,
   0.30000,
   0.30000,
   0.30000,
   0.30000,
   0.30000,
   0.30000,
   0.30000,
   0.30000,
   0.30000,
   0.30000,
   0.30000,
   0.30000,
   0.30000,
   0.30000,
   0.30000,
   0.30000,
   0.30000,
   0.30000,
   0.30000,
   0.30000,
   0.30000,
   0.30000,
   0.30000,
   0.30000,
   0.30000,
   0.30000,
   0.30000)




rcParams['font.size'] = 15
### PASSA-BASSO
# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(12, 7), dpi=65)
# Titolo del grafico
f1.suptitle("Conducibilità della soluzione elettrolitica",
    y=0.97, fontsize=17)

# GRAFICO 1
ax1 = host_subplot(111, axes_class=AA.Axes)
#ax1 = f1.add_subplot(1, 1, 1)

# crea plot con le barre d'errore (o anche senza)
m1 = -0.22187
q1 = 10.849
m2 = 1.0473
q2 = 3.6451
linea1 = ax1.errorbar(x=[i for i in range(0,30)], y=[m1*i+q1 for i in range(0,30)],
    fmt='-', c='red', linewidth=2)
linea2 = ax1.errorbar(x=[i for i in range(0,30)], y=[m2*i+q2 for i in range(0,30)],
    fmt='-', c="green", linewidth=2)

dots = ax1.errorbar(x=ml, y=s,
#    yerr=0.01/sqrt(12), xerr=0.1/sqrt(12),
    yerr=dy_corr, #xerr=dx,
    fmt='.', c='black', linewidth=2,
    markersize=7, markeredgewidth=1)

intersec = ax1.axvline(x=5.676, linewidth=2, color='gray')
    
ax1.set_ylabel(u'Conducibilità Λ [μS]',
    labelpad=8, fontsize=14)
ax1.set_xlabel(u'Volume di soluzione titolante [ml]',
    labelpad=8, fontsize=14)

ax1.grid(True)
#ax1.set_xscale('log')
ax1.set_ylim(( 8, 31))
ax1.set_xlim((-0.7, 25.7))

# toglie labels
#for label in ax1.get_xaxis().get_majorticklabels():
#  label.set_visible(False)

# ax2 is responsible for "top" axis and "right" axis
ax2 = ax1.twin()
ax2.set_xticks((5.676,))
#ax2.set_xticklabels(["$0$", r"$\frac{1}{2}\pi$",r"$\pi$", r"$\frac{3}{2}\pi$", r"$2\pi$"])
ax2.axis["right"].major_ticklabels.set_visible(False)

# Setta i custom ticks
#ax1.xaxis.set_ticks((0,5,5.676,10,15,20,25))
# Setta labels
#ax1.set_yticklabels(("", -25, -20, -15, -10, -5, 0))

# questo produce una legenda
ax1.legend((dots, linea1, linea2, intersec ), ("dati sperimentali", "fit dati in discesa", "fit dati in salita", "intersezione"), 'lower right', prop={'size': 12})

# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.07, right=0.98,
    top=0.90, bottom=0.09, hspace=0.08, wspace=0)

# mostra grafico
plt.show() 
