"""Unit test for geo module"""

import floodsystem.geo
import floodsystem.stationdata
from floodsystem.utils import sorted_by_key

def test_stations_by_distance():
    """Test returning a list of stations sorted by distance"""

    # Build list of stations
    stations = floodsystem.stationdata.build_station_list()

    # Set coordinate to Cambridge city centre
    p = (52.2053, 0.1218)

    # List of tuples of station, distance
    s_d = floodsystem.geo.stations_by_distance(stations, p)

    assert len(s_d) > 0
    assert s_d[0][1] < s_d[1][1]
    assert s_d[-2][1] < s_d[-1][1]
    assert len(s_d[0]) == 2


def test_stations_within_radius():
    """Test returning a list of stations within a specific radius"""

    #build list of stations and centre
    stations = floodsystem.stationdata.build_station_list()
    centre = (52.2053, 0.1218)

    #test radius in function
    station_void = floodsystem.geo.stations_within_radius(stations, centre, 0)
    assert len(station_void) == 0


def test_rivers_with_station():
    """Test returning a set of rivers with a monitoring station"""

    # Build list of stations 
    stations = floodsystem.stationdata.build_station_list()

    # List of rivers with a monitoring station
    rivers = floodsystem.geo.rivers_with_station(stations)

    assert len(rivers) > 0
    assert type(rivers) == set


def test_stations_by_river():
    """Test returning a dictionary of rivers with a list of station objects on each river"""

    # Build list of stations 
    stations = floodsystem.stationdata.build_station_list()

    # List of rivers with a monitoring station
    rivers = floodsystem.geo.rivers_with_station(stations)

    # Dictionary of rivers with a list of station objects on each river
    river_stations = floodsystem.geo.stations_by_river(stations)

    # count the number of stations at River Cam
    counter = 0
    for station in stations:
        if station.river == 'River Cam':
            counter += 1
    
    assert counter == len(river_stations['River Cam'])
    assert len(rivers) == len(river_stations)


def test_rivers_by_station_number():
    """Test if list is sorted"""
    stations = floodsystem.stationdata.build_station_list()
    N = 9
    assert floodsystem.geo.rivers_by_station_number(stations, N) == sorted(floodsystem.geo.rivers_by_station_number(stations, N), key = lambda x: x[1], reverse = True)
    