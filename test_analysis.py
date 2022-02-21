"""Unit test for analysis module"""

import datetime
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.dates import date2num 
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
from floodsystem.flood import stations_highest_rel_level

def test_polyfit():
    """Test returning a tuple of the polynomial object and any shift 
    of the time axis for a least-squares fit of a polynomial to water level data"""
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # List of stations_highest_rel_level with N = 1
    station = stations_highest_rel_level(stations, 1)[0]

    # fetch dates and levels for past 2 days
    dt = 2
    dates, levels = fetch_measure_levels(
        station.measure_id, dt=datetime.timedelta(days=dt))

    # Calculate best-fit polynomial of degree 4
    poly, d0 = polyfit(dates, levels, 4)

    # checks
    assert len(poly) == 5
    assert d0 > 0
