from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    """Requirements for Task 1B"""

    # Build list of stations
    stations = build_station_list()

    # Set coordinate to Cambridge city centre
    p = (52.2053, 0.1218)

    # List of tuples of station, distance
    s_d = stations_by_distance(stations, p)

    # Insert town to middle of list of tuples
    for station in stations:
        for i in range(len(s_d)):
            if s_d[i][0] is station.name:
                s_d[i] = (s_d[i][0], station.town, s_d[i][1])

    # Print the ten closest stations 
    print(f'Ten closest stations: {s_d[:10]}')

    # Print the ten furthest stations
    print(f'Ten furthest stations: {s_d[-10:]}')
    

if __name__ == "__main__":
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()