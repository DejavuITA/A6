from math import *			# da math importo tutto # non devo utilizzare il namespace (es: np per numpy)

from matplotlib import *		# da matplotlib importo tutto # non devo utilizzare il namespace (es: np per numpy)
import matplotlib.pyplot as plt
import numpy as np			# importo numpy come np

from scipy.optimize import curve_fit

data = np.genfromtxt("../dati/dati.csv", delimiter=',', names=True)
ml = data['millilitri']
s = data['conducibilita']


# Metodo dei minimi quadrati su una funziona lineare del tipo
# y = ax + b che diventa un'equazione matriciale
# Y = CX doce C è un vettore (a, b), mentre X è una matrice
# con sulla prima colonna x e sulla seconda tutti 1 (così torna l'eq. non matriciale)
# Y è un vettore

Y1 = s[0:12]
X1 = ml[0:12]

f = lambda x, a, b: a*x + b

(a1, b1), cov = curve_fit(f, X1, Y1)


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
f1 = plt.figure(figsize=(9, 6), dpi=65)
# Titolo del grafico
f1.suptitle("Conducibilità della soluzione elettrolitica",
    y=0.97, fontsize=17)

# GRAFICO 1
ax1 = f1.add_subplot(1, 1, 1)

# crea plot con le barre d'errore (o anche senza)
m1 = -0.22187
q1 = 10.849
m2 = 1.0473
q2 = 3.6451


#linea1 = ax1.errorbar(x=[i for i in range(0,30)], y=[m1*i+q1 for i in range(0,30)],
#    fmt='-', c='red', linewidth=2)
#linea2 = ax1.errorbar(x=[i for i in range(0,30)], y=[m2*i+q2 for i in range(0,30)],
#    fmt='-', c="green", linewidth=2)

lim_x = np.array((-1.5, 26.5))

dots = ax1.errorbar(x=ml, y=s,
    yerr=dy_corr, #xerr=dx,
    fmt='o', c='gray', linewidth=2,
    markersize=7, markeredgewidth=1, zorder=2)

line1 = ax1.errorbar(x=lim_x, y=a1*lim_x + b1,
    #yerr=dy_corr, #xerr=dx,
    fmt='-', c='gray', linewidth=2, zorder=1)

    
ax1.set_ylabel(u'Conducibilità [μS]',
    labelpad=10, fontsize=16)
ax1.set_xlabel(u'Volume di soluzione titolante [ml]',
    labelpad=10, fontsize=16)


ax1.grid(True)
#ax1.set_xscale('log')
ax1.set_ylim(( 7, 32))
ax1.set_xlim(lim_x)

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
