# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

import random


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

    return s

def test_typical_range_consistent():
    """1F (part 1): test method that determines consistency of high/low range data of a station"""

    testStation = test_create_monitoring_station()
    
    # normal range should return true
    assert MonitoringStation.typical_range_consistent(testStation) == True

    # lower range higher than upper range should return False
    testStation.typical_range = (5, 3)
    assert MonitoringStation.typical_range_consistent(testStation) == False

    # none should return false
    testStation.typical_range = None
    assert MonitoringStation.typical_range_consistent(testStation) == False

def test_inconsistent_typical_range_stations():
    """1F (Part 2): test function that returns list of stations with inconsistent data"""

    stations = build_station_list()

    inconsistentStations = inconsistent_typical_range_stations(stations)

    # prevent index out of range error of there are no inconsistent stations
    if inconsistentStations:

        # test if stations on the list actually have inconsisdent data
        assert MonitoringStation.typical_range_consistent(inconsistentStations[0]) == False

def create_sample_stations():
    """Creates list of 10 stations objects for testing range and water levels"""
    
    stations = [MonitoringStation("test-s-id", "test-s-id", str(i+1), (0, 0), (random.random(), 1+random.random()), "river", "town") for i in range(10)]
    for s in stations:
        s.latest_level = random.random() + random.randrange(0, 1)

    return stations
