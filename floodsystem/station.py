# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


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
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistent(self):
        """Return True if the data is consistent and False if 
        the data is inconsistent or unavailable."""

        # inconsistent if data is unavailable
        if self.typical_range == None:
            return False
        # inconsistent if low range is higher than high range
        elif self.typical_range[0] > self.typical_range[1]:
            return False
        # else consistent
        else:
            return True

    def relative_water_level(self):
        """Returns the latest water level as a fraction of the typical range.
        Returns None if data is not available or is inconsistent"""

        # Return None if data is not available or is inconsistent

        # Return latest water level as a fraction of the typical range


def inconsistent_typical_range_stations(stations):
    """Returns a list of stations that have inconsistent data. The input 
    is stations, which is a list of MonitoringStation objects."""

    # return list of stations with inconsistent data ranges
    return [station.name for station in stations if station.typical_range_consistent() == False]