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
        self.predicted_level_change = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistent(self):
        """This method checks the typical high/low range data for consistency"""

        if self.typical_range:
            return self.typical_range[0] <= self.typical_range[1]
        else:
            return False

    def add_predicted_level_change(self):
        """2G: This method adds the predicted_level_change attribbute to a station object"""

        dates, levels = fetch_measure_levels(self.measure_id, datetime.timedelta(days=5))
        poly, d0 = polyfit(dates, levels, 5)
        change = forecast(poly, d0)

        self.predicted_level_change = change

def inconsistent_typical_range_stations(stations):
    """This function returns a list of stations that have inconsistent data"""

    return [station for station in stations if not MonitoringStation.typical_range_consistent(station)]

def relative_water_level(self, station, update_water_levels):
    #add the real code for this later
        """This method returns a water level relative to a typical range"""
        relativewater= {}
        for self in station:    
            if self== "None":
                relativewater[relwat]= "None"
            else:
                relwat=(update_water_levels(station)-self.typical_range[0])/(self.typical_range[1]-self.typical_range[0])
            relativewater[relwat].append(station)

       
    
        
