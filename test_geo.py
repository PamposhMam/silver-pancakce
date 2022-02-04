"""Unit test for geo.py module"""

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_river, rivers_by_station_number
import random

def test_stations_by_river():
    """1D part 2: Test function that returns stations associated with each river"""

    stations = build_station_list()

    # test for output
    output = stations_by_river(stations)
    assert len(output) > 0
    assert type(output) == dict

    # test whether the stations associated with a river is empty 
    stationsOnRiverThames = output['River Thames']
    assert len(stationsOnRiverThames) > 0

def test_rivers_by_station_number():
    """1E: Test function that determines the N rivers with the most monitoring stations"""

    stations = build_station_list()

    # test output length
    N = random.randint(2, 20)
    output = rivers_by_station_number(stations, N)
    assert len(output) >= N

    # test order of output (descending)
    for i in range(len(output) - 1):
        assert output[i][1] >= output[i+1][1]
