"""Unit test for geo.py module"""

from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_river

def test_stations_by_river():
    """Test function that returns stations associated with each river"""

    stations = build_station_list()

    # test for output
    output = stations_by_river(stations)
    assert len(output) > 0
    assert type(output) == dict

    # test whether the stations associated with a river is empty 
    stationsOnRiverThames = output['River Thames']
    assert len(stationsOnRiverThames) > 0