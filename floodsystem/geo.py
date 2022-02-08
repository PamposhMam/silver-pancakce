# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
#!pip install haversine
from .utils import sorted_by_key  # noqa
from operator import itemgetter
def stations_by_distance(stations, p):
    """This function returns a sorted list of stations a distance 'x' from a given co-ordinate, 'p'"""
    stationname=[]
    from haversine import haversine, Unit
    stationdist=[]
    for station in stations:
        stationdist.append(haversine(station.coord, p))
        stationname.append(station.name)
    stations=list(zip(stationname, stationdist))
    stations.sort(key=lambda x: x[1])
    return stations

def stations_within_radius(stations, centre, r):
    """This function returns a list of all stations within a radius 'r' of a geographic co-ordinate 'x'"""
    from haversine import haversine, Unit
    inrange = []
    for station in stations:
        if haversine(station.coord, centre)<=r:
           inrange.append(station.name)
    return inrange

def rivers_with_station(stations):
    """This function returns a list of rivers with a monitoring station"""
    rivers= []
    for station in stations:
        river=station.river
        if river not in rivers:
            rivers.append[river]
    return rivers
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

    rivers = stations_by_river(stations)
    riversWithNumber = []

    for r in rivers:
        riversWithNumber.append((r, len(rivers[r])))

    riversWithNumber.sort(key = itemgetter(1), reverse = True)

    while riversWithNumber[N-1][1] == riversWithNumber[N][1]:
        N += 1

    return riversWithNumber[:N]
