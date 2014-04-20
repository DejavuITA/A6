import numpy as np

from uncertainties import ufloat

def chi2_retta(m, q, x, y, error):
    y_exp = m*np.array(x) + q

    return chi2(y, y_exp, error)

def chi2(obs, exp, error):
    return sum([((o - e) / err)**2 for o, e, err in zip(obs, exp, error)])
