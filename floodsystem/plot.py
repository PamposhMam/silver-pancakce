"""This module contains functions that plot data"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.dates import date2num

<<<<<<< HEAD
from .analysis import polyfit
=======
from floodsystem.analysis import polyfit
from floodsystem.stationdata import MonitoringStation
>>>>>>> 744843efcb88f8f2c80012a7d0d5debd0e9db502

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

#2E
from datetime import datetime, timedelta
from floodsystem.stationdata import build_station_list
station= "Cam"
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.station import MonitoringStation
def plot_water_levels(station, dates, levels):
    dt= 7
    stations = build_station_list()
    station_name = station
    station_cam = None
    for station in stations:
        if station.name == station_name:
            station_cam = station
            break
    dates, levels = fetch_measure_levels(
            station_cam.measure_id, dt=datetime.timedelta(days=dt))
    plt.plot(dates, levels)
    plt.plot (station_name.__repr__.typical_range[1])
    plt.plot (station_name.__repr__.typical_range[0])

        # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title('{1}, {2}'.format ("station", station_name))

        # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()
