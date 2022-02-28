"""Unit test for flood module"""

from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_highest_rel_level
from floodsystem.station import MonitoringStation

def test_stations_highest_rel_level():
    
    stations = build_station_list()

    highLevelStations = stations_highest_rel_level(stations, 5)

    assert len(highLevelStations) == 5

    for i in range(4):
        assert MonitoringStation.relative_water_level(stations[i]) >= MonitoringStation.relative_water_level(stations[i+1])