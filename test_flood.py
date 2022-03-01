"""Unit test for flood module"""

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.station import MonitoringStation
from test_station import create_sample_stations

def test_stations_highest_rel_level():
    
    # test with real data
    stations = build_station_list()
    update_water_levels(stations)

    highLevelStations = stations_highest_rel_level(stations, 5)

    assert len(highLevelStations) == 5
    print(highLevelStations)

    for i in range(4):
        assert MonitoringStation.relative_water_level(highLevelStations[i]) >= MonitoringStation.relative_water_level(highLevelStations[i+1])

    # test with sample data
    # data is a sample of 10 stations named 1 to 10, in increasing order of levels
    sampleStations = create_sample_stations()

    highLevelSampleStations = stations_highest_rel_level(sampleStations, 5)

    for i in range(5):
        assert highLevelSampleStations[i].name == str(10-i)