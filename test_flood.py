"""Unit test for flood module"""

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def test_stations_level_over_threshold():
    """ Test returning a sorted list of (station, relative water level) tuples"""
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # List of tuples from stations_level_over_threshold with tol = 0.8
    stationsover = stations_level_over_threshold(stations, 0.8)

    # checks
    assert stationsover[0][1] > stationsover [1][1]
    assert stationsover[-1][1] < stationsover [-2][1]
    assert stationsover[-1][1] > 0.8


def test_stations_highest_rel_level():
    """Test returning a sorted list of the N stations at which the relative water 
    level is highest"""

    # complete