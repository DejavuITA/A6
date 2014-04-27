from math import *
import numpy as np
from uncertainties import ufloat

def chi2_retta(m, q, x, y, error):
    y = np.array(y)
    error = np.array(error)

    y_exp = m*np.array(x) + q

    return chi2(y, y_exp, error)

def chi2(obs, exp, error):
    return sum([((o - e) / err)**2 for o, e, err in zip(obs, exp, error)])

def fit(x, y, err):
    x = np.array(x)
    y = np.array(y)

    w =  np.array(err)**-2
    N = len(x);
    
    m1 = sum(w);
    m2 = sum(w * x);
    m4 = sum(w * x**2);
    
    M = np.matrix([[m1, m2], [m2, m4]])
    
    n1 = sum(w * y);
    n2 = sum(w * x * y);
    
    Noto = np.matrix([[n1], [n2]])
    
    R = M.I * Noto;
    
    q = R[0][0,0];
    m = R[1][0,0];
    
    dq = sqrt(sum((x**2) * w) / np.linalg.det(M));
    dm = sqrt(sum(w) / np.linalg.det(M));

    return m, dm, q, dq
