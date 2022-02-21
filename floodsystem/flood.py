"""This module contains a collection of functions related to
flood data.

"""

from .utils import sorted_by_key  # noqa

def stations_level_over_threshold(stations, tol):
    """Returns a sorted list of (station, relative water level) tuples for
    stations with relative water level over tol in descending order where
    stations is a list of MonitoringStation objects."""

    # empty list
    list = []

    # loop through stations and build a list of tuples
    for station in stations:
        if station.relative_water_level() == None:
            pass
        # ignoring the anomolous entry (Letcombe Basset)
        elif station.name == 'Letcombe Bassett':
            pass
        elif station.relative_water_level() > tol:
            list.append((station, station.relative_water_level()))

    # sort list by key
    list = sorted_by_key(list, 1, reverse = True)

    # return list
    return list


def stations_highest_rel_level(stations, N):
    """Returns a sorted list of the N stations at which the relative water 
    level is highest in descending order where stations is a list of 
    MonitoringStation objects."""

    # empty list
    list = []

    # list of sorted stations over threshold
    stationsover = stations_level_over_threshold(stations, -100)

    # append the N highest stations to list
    for i in range(N):
        list.append(stationsover[i][0])

    # return sorted list
    return list