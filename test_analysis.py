"""Unit test for analysis.py module"""

from datetime import datetime
import numpy as np
from matplotlib.dates import date2num
from floodsystem.analysis import polyfit

def test_polyfit():

    def f(x):
        return x**3 - 2*x**2 + 10*x + 4

    dates = [datetime(2016, 12, 30), datetime(2016, 12, 31), datetime(2017, 1, 1),
     datetime(2017, 1, 2), datetime(2017, 1, 3), datetime(2017, 1, 4),
     datetime(2017, 1, 5)]

    t = date2num(dates)

    # create simple polynomial and see if function gives the same polynomial
    y = [f(n-t[0]) for n in t]
    f, x0 = polyfit(dates, y, 3)

    assert round(f.coefficients[0]) == 1
    assert round(f.coefficients[1]) == -2
    assert round(f.coefficients[2]) == 10
    assert round(f.coefficients[3]) == 4

    assert x0 == t[0]

    