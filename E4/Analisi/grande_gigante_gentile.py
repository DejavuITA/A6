mpl = False
try:
    import matplotlib
    from matplotlib import pyplot as plt
    mpl = True
except:
    print "installati matplotlib!"

N = (1, 2, 3, 4, 5, 5.2, 5.4, 5.6, 5.8, 6, 7, 8, 9)

Q = (
    1.3980e-04,
    1.3821e-04,
    1.6286e-04,
    3.0668e-04,
    1.0383e-03,
    1.3067e-03,
    1.8431e-03,
    2.6026e-03,
    4.3632e-03,
    9.6295e-03,
    6.5170e-02,
    4.1163e-01,
    2.9884e+00
)

dQ = (
      1.8617e-06,
      1.9620e-06,
      2.2002e-06,
      2.7229e-06,
      1.3016e-05,
      8.3042e-06,
      1.1322e-05,
      1.6312e-05,
      2.6838e-05,
      1.2289e-04,
      5.5883e-04,
      5.6583e-03,
      6.7334e-02
)

if mpl:
    f = plt.figure(figsize=(10, 7.5))
    f.suptitle("Flusso in funzione del numero di giri",
        y=0.96, fontsize=16)

    ax = f.add_subplot(1, 1, 1)
    ax.set_yscale('log')

    ax.errorbar(x=N, y=Q, yerr=dQ,
        fmt="o", c="black")

    ax.set_ylabel(r'Flusso $Q_{valve}$ [$Pa \, m^3 s^{-1}$]',
        labelpad=6, fontsize=14)
    ax.set_xlabel(u'Apertura del micrometro [giri]',
        labelpad=6, fontsize=14)
    
    ax.set_xlim((0, 10))
    ax.grid(True)

    f.subplots_adjust(left=0.10, right=0.95,
        top=0.90, bottom=0.10, hspace=0.1)

    plt.show()
