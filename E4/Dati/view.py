import sys
import os

mpl = False
try:
    import matplotlib
    from matplotlib import pyplot as plt
    mpl = True
except:
    print "installati matplotlib"

sys.argv.remove("view.py")
if "view.py" in sys.argv[1:]:
    sys.argv.remove("view.py")

if mpl:
    times = []
    values = []
    
    for i in range(len(sys.argv)):
        times.append([])
        values.append([])
        with open(sys.argv[i]) as f:
           for l in f:
               t, v = l.split()
               times[i].append(float(t))
               values[i].append(float(v) * 100)

    f = plt.figure(figsize=(8, 6))
    f.suptitle(sys.argv[1].replace("-", " ").replace(".txt", "").lower().capitalize(), y=0.96, fontsize=15)

    ax = f.add_subplot(1, 1, 1)

    d = []
    for i in range(len(sys.argv)):
        d.append(ax.errorbar(x=times[i], y=values[i], fmt="o"))

    if "pressione" in sys.argv[1].lower():
        ax.set_ylabel(u'Pressione [Pa]', labelpad=6, fontsize=14)
    else: 
        ax.set_ylabel(u'Potenziale [V]', labelpad=6, fontsize=14)

    ax.set_xlabel(u'Tempo [s]', labelpad=6, fontsize=14)
    ax.grid(True)

    f.subplots_adjust(left=0.1, right=0.95, top=0.90, bottom=0.10, hspace=0.1)

    plt.show()
