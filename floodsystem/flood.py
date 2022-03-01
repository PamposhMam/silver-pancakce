"""This module contains functions related to flooding and water levels

"""
from station import MonitoringStation 

from floodsystem.station import MonitoringStation
from floodsystem.stationdata import update_water_levels

from operator import itemgetter

#it says to do this in the submodule "flood"... I can't find that
def stations_level_over_threshold(stations, tol):
    """return a list of tuples with 1) a station (object) and 2) the station's relative water level. Note, this should only work if the level is> a given tolerance."""
    """Also sorted in descending order!"""
    statnames= {}
    statlevels= {}
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

def stations_highest_rel_level(stations, N):
    """This function returns a list of N stations at which the relative water level is the highest"""

    update_water_levels(stations)

    stations = [(station, MonitoringStation.relative_water_level(station)) for station in stations if MonitoringStation.typical_range_consistent(station)]
    stations.sort(key = itemgetter(1), reverse = True)

    return [s[0] for s in stations[:N]]

def towns_by_rel_levels(stations):
    """2G: For each town, determine highest relative water level of any river in that town. Sort towns into descending order of risk"""

    towns = {}

    # create dictionary that associates each town with the highest relative water level
    # dictionary entry looks like {town: [rel level, pred level change]}
    for station in stations:
        revLevel = MonitoringStation.relative_water_level(station)
        predictedChange = MonitoringStation.predicted_level_change(station)
        if station.town not in towns:
            towns[station.town] = [revLevel, predictedChange]
        else:
            if revLevel > towns[station.town][0]:
                towns[station.town] = [revLevel, predictedChange]

    # sort dictionary by relative water levels
    sortedTowns = []
    sortedLevels = sorted(towns.values())

    for i in range(len(sortedLevels)):
        for k in range(len(sortedLevels)):
            if towns[k] == sortedLevels[i]:
                sortedTowns.append((towns.keys()[k], sortedLevels[i]))
    
    return sortedTowns



