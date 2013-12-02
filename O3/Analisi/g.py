# -*- encoding: utf-8 -*-

import csv
from math import *
import matplotlib
from matplotlib import pyplot as plt

# Qui vanno i dati
# Angolo in radianti
x = (   

  -0.59923,
  -0.53378,
  -0.49451,
  -0.45088,
  -0.42906,
  -0.39852,
  -0.36797,
  -0.35925,
  -0.32870,
  -0.30689,
  -0.28507,
  -0.26762,
  -0.24580,
  -0.22835,
  -0.21962,
  -0.20217,
  -0.20217,
  -0.18908,
  -0.18035,
  -0.16726,
  -0.15853,
  -0.14108,
  -0.12799,
  -0.11054,
  -0.07563,
   0.00000,
   0.09890,
   0.14690,
   0.17308,
   0.19926,
   0.22108,
   0.24289,
   0.26034,
   0.27780,
   0.29525,
   0.31707,
   0.33888,
   0.36506,
   0.39124,
   0.41742,
   0.44797,
   0.46978,
   0.50033,
   0.52214,
   0.57014,

)
# Intensità luminosa relativa
y = (
   0.023627,
   0.038984,
   0.053160,
   0.082693,
   0.112227,
   0.172475,
   0.228588,
   0.286474,
   0.350266,
   0.407561,
   0.466037,
   0.524513,
   0.584761,
   0.640874,
   0.673361,
   0.703485,
   0.732428,
   0.760780,
   0.790904,
   0.821028,
   0.851742,
   0.880685,
   0.910219,
   0.939161,
   0.968695,
   1.000000,
   0.939161,
   0.883048,
   0.821028,
   0.760780,
   0.704076,
   0.645009,
   0.584170,
   0.527466,
   0.467218,
   0.407561,
   0.345540,
   0.290608,
   0.230360,
   0.171884,
   0.112640,
   0.083166,
   0.053101,
   0.038748,
   0.023627
   
)
# Errore sull'intensità luminosa relativa
dy = (  
   
   5.9226e-04,
   5.9499e-04,
   5.9868e-04,
   6.0988e-04,
   6.2559e-04,
   6.7023e-04,
   7.2465e-04,
   7.9099e-04,
   8.7330e-04,
   9.5346e-04,
   1.0399e-03,
   1.1299e-03,
   1.2256e-03,
   1.3168e-03,
   1.3704e-03,
   1.4205e-03,
   1.4691e-03,
   1.5169e-03,
   1.5680e-03,
   1.6194e-03,
   1.6720e-03,
   1.7218e-03,
   1.7729e-03,
   1.8231e-03,
   1.8745e-03,
   1.8365e-03,
   1.8231e-03,
   1.7259e-03,
   1.6194e-03,
   1.5169e-03,
   1.4215e-03,
   1.3236e-03,
   1.2247e-03,
   1.1346e-03,
   1.0417e-03,
   9.5346e-04,
   8.6693e-04,
   7.9606e-04,
   7.2654e-04,
   6.6972e-04,
   6.2584e-04,
   6.1009e-04,
   5.9866e-04,
   5.9494e-04,
   5.9226e-04

)

# Creo un grafico la dimensione è in pollici
f1 = plt.figure(figsize=(12, 6))
# Titolo del grafico
f1.suptitle("Intensità in funzione dell'angolo",
    y=0.96, fontsize=15)


# GRAFICO 1
ax1 = f1.add_subplot(1, 2, 1)
# crea plot con le barre d'errore (o anche senza)
dots = ax1.errorbar(x=x, y=y,
    yerr=dy, #xerr=,
    fmt='o-', c='black')
line = ax1.errorbar(x=[-0.8, 0.8], y=[0.05, 0.05],
    #yerr=dy, #xerr=,
    fmt='-', c='grey')
    
ax1.set_xlabel(u'Angolo di incidenza [radianti]',
    labelpad=12, fontsize=14)
ax1.set_ylabel(u'Intensità relativa',
    labelpad=6, fontsize=14)

# creo linee verticali
#ax1.fill(-0.50132, 0.050018, 'b', -0.50132, 0, 'b') scusa pasa ma questo non sono capace di farlo andare
# devi usarlo così: ax1.fill([vertici poligono x], [vertici poligono y])
#ax1.fill([-0.5013177, -0.5013177, 0.5050421, 0.5050421], [0.05, 0, 0, 0.05], 'b')
# comunque secondo me non serve a molto
ax1.plot([-0.5013177, -0.5013177], [0.05, 0], color='black', linestyle='-', linewidth=1)
ax1.plot([0.5050421, 0.5050421], [0.05, 0], color='black', linestyle='-', linewidth=1)

ax1.grid(True)
ax1.set_ylim((0, 1.1))
ax1.set_xlim((-0.65, 0.65))
# questo produce una legenda
ax1.legend((dots, line), ("Punti misurati", "Linea 5%"), 'upper right',
    prop={'size': 12})
    

# GRAFICO 2
ax2 = f1.add_subplot(1, 2, 2)
ax2.set_yscale('log')
# crea plot con le barre d'errore (o anche senza)
dots2 = ax2.errorbar(x=x, y=y,
    yerr=dy, #xerr=,
    fmt='o-', c='black')
line2 = ax2.errorbar(x=[-0.8, 0.8], y=[0.05, 0.05],
    #yerr=dy, #xerr=,
    fmt='-', c='grey')

ax2.set_xlabel(u'Angolo di incidenza [radianti]',
    labelpad=12, fontsize=14)
ax2.set_yticks((0.05, 0.1, 0.5, 1))
ax2.get_yaxis().set_ticklabels(("0.05", "0.1", "0.5", "1"))

# creo linee verticali
ax2.plot([-0.5013177, -0.5013177], [0.05, 0.02], color='black', linestyle='-', linewidth=1)
ax2.plot([0.5050421, 0.5050421], [0.05, 0.02], color='black', linestyle='-', linewidth=1)
# si ma dai fanculo, con me non va un cazzo, sul primo plot va e su questo no, ma si può essere più incompetenti azzo!!!
# devi considerare che stai plottando su di una scala logaritmica, se metti zero (anche in set_ylim devi stare attento)
# esplode tutto!


ax2.grid(True)
ax2.set_ylim((0.02, 1.5))
ax2.set_xlim((-0.65, 0.65))
# questo produce una legenda
ax2.legend((dots2, line2), ("Punti misurati", "Linea 5%"), 'upper right',
    prop={'size': 12})
    
######

# questo imposta i bordi del grafico
f1.subplots_adjust(left=0.07, right=0.97,
    top=0.88, bottom=0.12, hspace=0, wspace=0.1)
# mostra grafico
plt.show()  

