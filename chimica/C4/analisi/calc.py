#! -*- encoding: utf-8 -*-

from math import *
import numpy as np

from uncertainties import ufloat, unumpy

from matplotlib import pyplot as plt

vi = ufloat(10, 0.03)
vf = ufloat(50, 0.3)
ci = ufloat(0.5, 0)

cf = ci * vi / vf
print cf

c1000 = ufloat(1000, 0)

vi100 = ufloat(10, 0.03)
vi10 = ufloat(1, 0.006)
vft = ufloat(100, 0.3)

cf100 = c1000 * vi100 / vft
cf10 = c1000 * vi10 / vft
cf1 = cf100 * vi10 / vft
print cf100, cf10, cf1

ca_latte = ufloat(10.5, 10.5*0.04)
latte = vft * ca_latte / vi10

ca_succo = ufloat(10.6, 10.6*0.04)
succo = ufloat(80, 1) * ca_latte / ufloat(20, 1)

print latte, succo

cs = unumpy.uarray([14.3, 33.4, 460, 14.8, 10.5, 10.6], np.array([14.3, 33.4, 460, 14.8, 10.5, 10.6])*0.04)
f = cs / 4.0
print f
