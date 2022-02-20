from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    """Requirements for Task 2B"""
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # List of tuples from stations_level_over_threshold with tol = 0.8
    stationsover = stations_level_over_threshold(stations, 0.8)

    # Print station.name and relative level
    for station in stationsover:
        print(station[0].name, station[1])


if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()