"""This module contains functions that plot data"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.dates import date2num

from .analysis import polyfit

def plot_water_level_with_fit(station, dates, levels, p):
    """This function plots the water level data and best-fit polynomial with degree p of a station"""

    poly, d0 = polyfit(dates, levels, p)

    # plot real data
    plt.plot(dates, levels, '.', label='data')

    # plot polynomial fit
    plt.plot(dates, poly(date2num(dates)-d0), label='polynomial')

    # plot typical range low/high
    plt.plot(dates, [station.typical_range[0]]*len(dates), '--', color='red', label='typical range low')
    plt.plot(dates, [station.typical_range[1]]*len(dates), '--', color='green', label='typical range high')

    # make graph prettier
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45)
    plt.title('Station: {}'.format(station.name))
    plt.tight_layout()
    plt.legend()

    plt.show()
