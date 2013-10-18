mpl = False
try:
    import matplotlib
    from matplotlib import pyplot as plt
    mpl = True
except:
    print "installati matplotlib!"

N = (1, 2, 3, 4, 5, 5.2, 5.4, 5.6, 5.8, 6, 7, 8, 9)

Q = (
   1.3980e-06,
   1.3966e-06,
   1.6286e-06,
   3.0668e-06,
   1.0383e-05,
   1.3067e-05,
   1.8431e-05,
   2.6026e-05,
   4.3632e-05,
   9.6295e-05,
   6.5170e-04,
   4.1163e-03,
   2.9884e-02
)

dQ = (
   1.8617e-08,
   1.8197e-08,
   2.2002e-08,
   2.7229e-08,
   1.3016e-07,
   8.3042e-08,
   1.1322e-07,
   1.6312e-07,
   2.6838e-07,
   1.2289e-06,
   5.5883e-06,
   5.6583e-05,
   6.7334e-04
)

if mpl:
    f = plt.figure(figsize=(10, 7.5))
    f.suptitle("Portata in funzione del numero di giri",
        y=0.96, fontsize=16)

    ax = f.add_subplot(1, 1, 1)
    ax.set_yscale('log')

    ax.errorbar(x=N, y=Q, yerr=dQ,
        fmt="o", c="black")

    ax.set_ylabel(r'Portata Q [$Pa \, m^3 s^{-1}$]',
        labelpad=6, fontsize=14)
    ax.set_xlabel(u'Apertura del micrometro [giri]',
        labelpad=6, fontsize=14)
    
    ax.set_xlim((0, 10))
    ax.grid(True)

    f.subplots_adjust(left=0.10, right=0.95,
        top=0.90, bottom=0.10, hspace=0.1)

    plt.show()
