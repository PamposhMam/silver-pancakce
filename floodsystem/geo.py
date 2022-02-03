# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

def stations_by_river(stations):
    """This function returns a dictionary that maps river names to a list of stations on that river"""

    rivers = {}

    for station in stations:
        river = station.river

        if river not in rivers:
            rivers[river] = []
        
        rivers[river].append(station)
    return rivers


def rivers_by_station_number(stations, N):
    """This function returns the N rivers with the greatest number of monitoring stations"""
    return 