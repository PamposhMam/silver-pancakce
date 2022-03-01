# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""

import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit, forecast

class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}\n".format(self.typical_range)
        d += "   relative water level : {}".format(self.relative_water_level())
        return d

    def typical_range_consistent(self):
        """This method checks the typical high/low range data for consistency"""

        if self.typical_range:
            return self.typical_range[0] <= self.typical_range[1]
        else:
            return False

    def predicted_level_change(self):
        """2G: This method returns the predicted level change attribbute of a station"""

        dates, levels = fetch_measure_levels(self.measure_id, datetime.timedelta(days=2))

        if len(dates) == 0 or len(levels) == 0:
            return 0

        if len(dates) != len(levels):
            return 0

        poly, d0 = polyfit(dates, levels, 5)
        change = forecast(poly, d0)

        return change

    def relative_water_level(self):
        if self.latest_level == None or not MonitoringStation.typical_range_consistent(self):
            return None
        else:
            return (self.latest_level - self.typical_range[0])/(self.typical_range[1]-self.typical_range[0])

def inconsistent_typical_range_stations(stations):
    """This function returns a list of stations that have inconsistent data"""

    return [station for station in stations if not MonitoringStation.typical_range_consistent(station)]

def relative_water_level1(self, station, update_water_levels):
    #add the real code for this later
        """This method returns a water level relative to a typical range"""
        relativewater= {}
        for self in station:    
            if self== "None":
                relativewater[relwat]= "None"
            else:
                relwat=(update_water_levels(station)-self.typical_range[0])/(self.typical_range[1]-self.typical_range[0])
            relativewater[relwat].append(station)

       
    
        
