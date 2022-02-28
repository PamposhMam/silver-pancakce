"""This module contains functions related to flooding and water levels

"""
#it says to do this in the submodule "flood"... I can't find that
def stations_level_over_threshold(stations, tol):
    """return a list of tuples with 1) a station (object) and 2) the station's relative water level. Note, this should only work if the level is> a given tolerance."""
    """Also sorted in descending order!"""
    statnames= {}
    statlevels= {}
    for station in stations:
        if relative_water_level>tol:
            statlevel= MonitoringStation.relative_water_level 
            statlevels[statlevel].append(MonitoringStation)
    statlevel.sort(reverse=True)
    for station in statlevel:
        statname= MonitoringStation.name
        statnames[statname].append(MonitoringStation)
    stattuple=list(zip(statnames,statlevels))
    stattuple.sort(reverse=True)
