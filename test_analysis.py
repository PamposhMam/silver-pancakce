"""Unit test for analysis.py module"""

import datetime
import numpy as np
from matplotlib.dates import date2num
from floodsystem.analysis import polyfit, forecast

def test_polyfit():

    dates = [datetime.datetime(2016, 12, 30), datetime.datetime(2016, 12, 31), datetime.datetime(2017, 1, 1),
     datetime.datetime(2017, 1, 2), datetime.datetime(2017, 1, 3), datetime.datetime(2017, 1, 4),
     datetime.datetime(2017, 1, 5)]

    t = date2num(dates)

    f = np.poly1d([1, -2, 10, 4])

    # create simple polynomial and see if function gives the same polynomial
    y = [f(n-t[0]) for n in t]
    f, x0 = polyfit(dates, y, 3)

    assert round(f.coefficients[0]) == 1
    assert round(f.coefficients[1]) == -2
    assert round(f.coefficients[2]) == 10
    assert round(f.coefficients[3]) == 4

    assert x0 == t[0]

def test_forecast():

    f = np.poly1d([1, -2, 10, 4])
    now = date2num(datetime.datetime.now())

    change = forecast(f, now)

    # gradient at x=0 should be 10, so change over 0.5 days will bbe 5
    assert round(change) == 5
    