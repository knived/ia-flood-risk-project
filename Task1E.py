from distutils.command.build import build
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def run():
    """Requirements for Task 1E"""

    # Build list of stations 
    stations = build_station_list()
    
    # Print the list of (river, number of stations) tuples for N rivers with the most stations
    print(rivers_by_station_number(stations, 9))

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()