# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine

def stations_by_distance(stations, p):
    """Returns a list, sorted by distance, of (station, distance) tuples, where distance 
    is the distance of the station from coordinate p. The inputs are stations, which is 
    a list of MonitoringStation objects and p, which is a coordinate represented by a 
    tuple of floats."""

    # empty list
    list = []

    # populate list with tuples of station name and distance to p
    for station in stations:
        list.append((station.name, haversine(station.coord, p)))

    # return sorted list
    return sorted_by_key(list, 1)


def stations_within_radius(stations, centre, r):
    """Returns a list of all the stations within the radius of a geogprahic coordinate. 
    The inputs are stations, which is a list of MonitoringStation objects, centre, which 
    is the geographic coordinate and r, which is the radius."""

    # complete


def rivers_with_station(stations):
    """Returns a set of rivers with a monitoring station. The input is stations, which 
    is a list of MonitoringStation objects."""

    # complete


def stations_by_river(stations):
    """Returns a dictionary of rivers with a list of station objects on each river. 
    The input is stations, which is a list of MonitoringStation objects."""

    # complete


def rivers_by_station_number(stations, N):
    """Return a list of N rivers, sorted by number of stations, of (river name, number of stations) 
    tuples. If there are more rivers with the same number of stations as the Nth entry, include 
    these rivers in the list. The inputs are stations, which is a list of MonitoringStation objects 
    and N, which is the number of rivers with the greatest number of stations."""

    # complete