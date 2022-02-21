from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    """Requirements for Task 2C"""
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # List of stations_highest_rel_level with N = 10
    Nstations = stations_highest_rel_level(stations, 10)

    # Print station.name and relative level for list
    for station in Nstations:
        print(station.name, station.relative_water_level())


if __name__ == "__main__":
    print("*** Task 2C: CUED Part IA Flood Warning System ***")
    run()