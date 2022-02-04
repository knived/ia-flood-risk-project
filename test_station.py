# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""

import floodsystem.station
import floodsystem.stationdata

def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = floodsystem.station.MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town


def test_inconsistent_typical_range_stations():
    """Test returning a list of stations that have inconsistent data"""

    # Build list of stations
    stations = floodsystem.stationdata.build_station_list() 

    # Build list of stations with inconsistent typical data range
    inconsistent_stations = floodsystem.station.inconsistent_typical_range_stations(stations)

    # count the number of inconsistent stations
    counter1 = 0
    counter2 = 0

    for station in stations:
        for name in inconsistent_stations:
            if station.name == name:
                if station.typical_range == None:
                    counter1 += 1
                elif station.typical_range[0] > station.typical_range[1]:
                    counter1 += 1

    assert len(inconsistent_stations) == counter1