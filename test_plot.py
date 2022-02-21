"""Unit test for plot module"""

from floodsystem.plot import plot_water_levels, plot_water_level_with_fit
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def test_plot_water_levels():
    """Test plotting the water level data against time for a station"""
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # List of stations_highest_rel_level with N = 1
    Nstations = stations_highest_rel_level(stations, 1)

    # Plots water levels for stations over the past 20 days
    plot_water_levels(Nstations, 20)


def test_plot_water_level_with_fit():   
    """Test plotting the water level data and the best-fit polynomial
    for a station"""
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # List of stations_highest_rel_level with N = 1
    Nstations = stations_highest_rel_level(stations, 1)

    # Plots water levels for stations and best-fit polynomial of degree 4 over the past 2 days
    plot_water_level_with_fit(Nstations, 2, 4)