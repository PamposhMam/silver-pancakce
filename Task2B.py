from floodsystem.flood import stations_level_over_threshold
from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels


stations= build_station_list()
water_level= update_water_levels(stations)
print(stations_level_over_threshold(stations, 0.8))
station_list= {'a': 2, 'b':3, 'c':5}

def stations_level_over_threshold(stations, tol):
    """return a list of tuples with 1) a station (object) and 2) the station's relative water level. Note, this should only work if the level is> a given tolerance."""
    """Also sorted in descending order!"""
    statnames= {}
    statlevels= {}
    for station in station_list:
        if MonitoringStation.relative_water_level(station_list)>tol:
            statlevel= MonitoringStation.relative_water_level(station_list)
            statlevels[statlevel].append(MonitoringStation)
    statlevel.sort(reverse=True)
    for station in statlevel:
        statname= MonitoringStation.name
        statnames[statname].append(MonitoringStation)
    stattuple=list(zip(statnames,statlevels))
    stattuple.sort(reverse=True)
