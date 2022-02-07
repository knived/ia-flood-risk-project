from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    """Requirements for Task 1C"""

    # Built list of stations 
    # Set radius to 10km and centre coordinate to Cambridge city centre
    centre = (52.2053, 0.1218)
    stations = build_station_list()
    
    # List of stations within circle centred at coordinate
    stations = stations_within_radius(stations, centre, 10)
    print(stations) 
    

if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()