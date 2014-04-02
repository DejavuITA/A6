from math import *			# da math importo tutto # non devo utilizzare il namespace (es: np per numpy)

from matplotlib import *		# da matplotlib importo tutto # non devo utilizzare il namespace (es: np per numpy)
import matplotlib.pyplot as plt
import numpy as np			# importo numpy come np

data = np.genfromtxt("../dati/dati.csv", delimiter=',', names=True)
ml = data['millilitri']
s = data['conducibilita']




rcParams['font.size'] = 15
### PASSA-BASSO
# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(9, 6), dpi=65)
# Titolo del grafico
f1.suptitle("Conducibilità della soluzione elettrolitica",
    y=0.97, fontsize=17)

# GRAFICO 1
ax1 = f1.add_subplot(1, 1, 1)

# crea plot con le barre d'errore (o anche senza)
#linea1 = ax1.errorbar(x=f, y=t_dB_corr,
#    fmt='--', c='black', linewidth=2)
#linea2 = ax1.errorbar(x=b_freq, y=b_dB,
#    fmt='o', c="white", linewidth=2,
#    markersize=7, markeredgewidth=1)

dots = ax1.errorbar(x=ml, y=s,
    yerr=0.01/sqrt(12), xerr=0.1/sqrt(12),
    fmt='.', c='gray', linewidth=2,
    markersize=7, markeredgewidth=1)
    
ax1.set_ylabel(u'Conducibilità Λ [μS]',
    labelpad=10, fontsize=16)
ax1.set_xlabel(u'Volume di soluzione titolante [ml]',
    labelpad=8, fontsize=14)


ax1.grid(True)
#ax1.set_xscale('log')
ax1.set_ylim(( 7, 32))
ax1.set_xlim((-1.5, 26.5))

# toglie labels
#for label in ax1.get_xaxis().get_majorticklabels():
#  label.set_visible(False)

# Setta labels
#ax1.set_yticklabels(("", -25, -20, -15, -10, -5, 0))

# questo produce una legenda
ax1.legend((dots, ), ("dati", ), 'upper left', prop={'size': 12})

# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.10, right=0.95,
    top=0.92, bottom=0.12, hspace=0.08, wspace=0)

# mostra grafico
plt.show() 
