# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine  # noqa

def stations_by_distance(stations, p):
    """Returns a list, sorted by distance, of (station, distance) tuples, where distance 
    is the distance of the station from coordinate p. The inputs are stations, which is 
    a list of MonitoringStation objects and p, which is a coordinate represented by a 
    tuple of floats."""

    # return a sorted list by distance of a list of (station, distance) tuples 
    return sorted_by_key([(station.name, haversine(station.coord, p)) for station in stations], 1)


def stations_within_radius(stations, centre, r):
    """Returns a list of all the stations within the radius of a geogprahic coordinate. 
    The inputs are stations, which is a list of MonitoringStation objects, centre, which 
    is the geographic coordinate and r, which is the radius."""

    # returns all station within radius of specified coordinate
    distances = stations_by_distance(stations, centre)
    stations_radius = []
    for distance in distances:
        if distance[1] < r:
            stations_radius.append(distance[0])
    stations_radius.sort()
    return stations_radius

def rivers_with_station(stations):
    """Returns a set of rivers with a monitoring station. The input is stations, which 
    is a list of MonitoringStation objects."""

    # return a set of rivers with at least one station
    return {station.river for station in stations}


def stations_by_river(stations):
    """Returns a dictionary of rivers with a list of station objects on each river. 
    The input is stations, which is a list of MonitoringStation objects."""

    # list of rivers
    rivers = rivers_with_station(stations)

    # empty dictionary
    river_dict = {}

    # repeat for every river
    for river in rivers:
        # sorted list of stations at each river
        tmp = []

        for station in stations:
            if river == station.river:
                tmp.append(station.name)

        tmp.sort()

        # add river : [sorted stations at river] to dictionary
        river_dict[river] = tmp

    # return dictionary
    return river_dict
    

def rivers_by_station_number(stations, N):
    """Return a list of N rivers, sorted by number of stations, of (river name, number of stations) 
    tuples. If there are more rivers with the same number of stations as the Nth entry, include 
    these rivers in the list. The inputs are stations, which is a list of MonitoringStation objects 
    and N, which is the number of rivers with the greatest number of stations."""

    # complete