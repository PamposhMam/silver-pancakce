"""This module contains functions that analyse water level data"""

from matplotlib.dates import date2num
import numpy as np

def polyfit(dates, levels, p):
    """This function computes a least-squares fit of a polynomial of degree p to water level data"""

    x = date2num(dates)
    p_coeff = np.polyfit(x-x[0], levels, p)

    return np.poly1d(p_coeff), x[0]

