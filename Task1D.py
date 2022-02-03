from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river

def run():
    """Requirements for Task 1D"""

    # Build list of stations 
    stations = build_station_list()

    # List of rivers with a monitoring station
    rivers = rivers_with_station(stations)

    # Print number of rivers
    print(f'Number of rivers: {len(rivers)}')

    # Print the first 10 rivers in a sorted list of rivers with a monitoring station
    rivers = list(rivers)
    rivers.sort()
    print(f'First ten rivers: {rivers[:10]}')

    # Dictionary of rivers with a list of station objects on each river
    river_stations = stations_by_river(stations)

    # Print the names of stations located on 'River Aire'
    print('Stations on River Aire: ', river_stations['River Aire'])

    # Print the names of stations located on 'River Cam'
    print('Stations on River Cam: ', river_stations['River Cam'])

    # Print the names of stations located on 'River Thames'
    print('Stations on River Thames: ', river_stations['River Thames'])


if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()