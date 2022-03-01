"""This module contains functions related to flooding and water levels

"""

from floodsystem.station import MonitoringStation
from floodsystem.stationdata import update_water_levels

import operator

#it says to do this in the submodule "flood"... I can't find that
def stations_level_over_threshold(stations, tol):
    """return a list of tuples with 1) a station (object) and 2) the station's relative water level. Note, this should only work if the level is> a given tolerance."""
    """Also sorted in descending order!"""
    statnames= []
    statlevels= []
    for station in stations:
        if MonitoringStation.relative_water_level>tol:
            statlevel= MonitoringStation.relative_water_level 
            statlevels[statlevel].append(MonitoringStation)
    statlevel.sort(reverse=True)
    for station in statlevel:
        statname= MonitoringStation.name
        statnames[statname].append(MonitoringStation)
    stattuple=list(zip(statnames,statlevels))
    stattuple.sort(reverse=True)

def stations_level_over_threshold1(stations, tol):
    highRiskStations = [(station, MonitoringStation.relative_water_level(station)) for station in stations if MonitoringStation.relative_water_level(station) and MonitoringStation.relative_water_level(station) > tol]
    highRiskStations.sort(key=operator.itemgetter(1), reverse=True)
    return highRiskStations

def stations_highest_rel_level(stations, N):
    """This function returns a list of N stations at which the relative water level is the highest"""

    stations = [(station, MonitoringStation.relative_water_level(station)) for station in stations if MonitoringStation.typical_range_consistent(station) and MonitoringStation.relative_water_level(station)]
    stations.sort(key = operator.itemgetter(1), reverse = True)

    return [s[0] for s in stations[:N]]

def towns_by_rel_levels(stations):
    """2G: For each town, determine highest relative water level of any river in that town. Sort towns into descending order of risk"""

    # create dictionary that associates each town with the highest relative water level
    # dictionary entry looks like {town: [rel level, pred level change]}
    # we do a predicted change only for towns with levels higher than 0.8 to save time

    stations = stations_level_over_threshold1(stations, 0.7)

    towns = {}

    for station in stations:
        s = station[0]
        revLevel = station[1]

        predictedChange = MonitoringStation.predicted_level_change(s)

        if s.town not in towns:
            towns[s.town] = [revLevel, predictedChange]
        else:
            if revLevel > towns[s.town][0]:
                towns[s.town] = [revLevel, predictedChange]

    # sort dictionary by relative water levels - no need to sort now
    sortedTowns = []
    # sortedLevels = sorted(towns.values(), reverse=True)

    # for i in range(len(sortedLevels)):
    #     for town in towns:
    #         if town:
    #             if towns[town][0] == sortedLevels[i][0]:
    #                 sortedTowns.append((town, sortedLevels[i]))
    
    for town in towns:
        sortedTowns.append([town, towns[town][0], towns[town][1]])

    # return list of towns in descending order of risk [[town, rev level, predicted change]]
    return sortedTowns


