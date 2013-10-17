import sys
import os

mpl = False
try:
    import matplotlib
    from matplotlib import pyplot as plt
    mpl = True
except:
    print "installati matplotlib!"

sys.argv.remove("zzz.py")
if "zzz.py" in sys.argv[1:]:
    sys.argv.remove("zzz.py")

ids = {
    "giro1.csv": 0,
    "giro2.csv": 1,
    "giro3.csv": 2,
    "giro4.csv": 3,
    "giro5.0.csv": 4,
    "giro5.2.csv": 5,
    "giro5.4.csv": 6,
    "giro5.6.csv": 7,
    "giro5.8.csv": 8,   
    "giro6.csv": 9,
    "giro7.csv": 10,
    "giro8.csv": 11,
    "giro9.csv": 12
}

B = (
   2.4883e-04,
   2.4859e-04,
   2.8773e-04,
   5.3026e-04,
   1.7640e-03,
   2.2166e-03,
   3.1212e-03,
   4.4019e-03,
   7.3709e-03,
   1.6252e-02,
   1.0991e-01,
   6.9417e-01,
   5.0394e+00
)

A = (
   2.4353e-04,
   3.8919e-04,
   1.3883e-03,
   2.4470e-03,
   4.5435e-03,
   3.2996e-03,
   1.6282e-03,
   4.1931e-03,
   6.2662e-03,
   5.6986e-02,
   1.0377e-01,
   1.8318e+00,
   6.3450e+00
)

if mpl:
    times = []
    values = []
    
    for i in range(len(sys.argv)):
        times.append([])
        values.append([])
        with open(sys.argv[i]) as f:

            for n, l in enumerate(f):
                t, v = l.split(",")
                #times[i].append(float(t.strip()))
                times[i].append(n)
                values[i].append(float(v.strip()))

    f = plt.figure(figsize=(8, 6))
    f.suptitle(sys.argv[0].replace("-", " ").replace(".txt", "").lower().capitalize(), y=0.96, fontsize=15)

    ax = f.add_subplot(1, 1, 1)

    d = []
    fs = []
    for i in range(len(sys.argv)):
        d.append(ax.errorbar(x=times[i], y=values[i], fmt="."))

        if sys.argv[i] in ids:
            n = ids[sys.argv[i]]
            fs.append(ax.errorbar(x=(0, len(values[i])), y=(A[n], A[n] + B[n]*len(values[i]))))

    ax.set_ylabel(u'Pressione [Pa]', labelpad=6, fontsize=14)
    ax.set_xlabel(u'Tempo [s]', labelpad=6, fontsize=14)
    ax.grid(True)

    f.subplots_adjust(left=0.1, right=0.95, top=0.90, bottom=0.10, hspace=0.1)

    plt.show()
