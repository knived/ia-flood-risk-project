from floodsystem.plot import plot_water_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level

def run():
    """Requirements for Task 2E"""
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # List of stations_highest_rel_level with N = 5
    Nstations = stations_highest_rel_level(stations, 5)

    # Plots water levels for stations over the past 10 days
    plot_water_levels(Nstations, 10)


if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    run()