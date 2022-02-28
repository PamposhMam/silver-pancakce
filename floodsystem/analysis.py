"""This module contains functions that analyse water level data"""

from matplotlib.dates import date2num
import numpy as np
import datetime

def polyfit(dates, levels, p):
    """This function computes a least-squares fit of a polynomial of degree p to water level data"""

    x = date2num(dates)
    p_coeff = np.polyfit(x-x[0], levels, p)

    return np.poly1d(p_coeff), x[0]

def forecast(poly, d0):
    """This function predicts whether the water level at a station is rising or falling
    Returns rate of change of water level, and predicted change in 0.5 days"""
    now = date2num(datetime.datetime.now())

    # use gradient of polynomial to find out if water level is rising or falling
    # positive gradient = rising, negative gradient = falling
    d = poly.deriv()
    grad = d(now - d0)

    # use linear extrapolation to calc change in water level
    change = grad*0.5

    return grad, change

