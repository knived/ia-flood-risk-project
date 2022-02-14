from numpy import sort
from floodsystem.stationdata import build_station_list
from floodsystem.station import inconsistent_typical_range_stations

def run():
    """Requirements for Task 1F"""

    # Build list of stations
    stations = build_station_list() 

    # Build list of stations with inconsistent typical data range
    inconsistent_stations = inconsistent_typical_range_stations(stations)

    # Print an alphabetically sorted list of station names with inconsistent data
    print(sort(inconsistent_stations))
    

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()