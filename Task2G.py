import datetime
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level
from floodsystem.analysis import polyfit
import numpy as np

def run():
    """Requirements for Task 2G"""

    # Build a list of stations
    stations = build_station_list()

    # Update water levels 
    update_water_levels(stations)

    # 100 stations with highest level 
    stations = stations_highest_rel_level(stations, 100)
    
    # empty lists for severity classes
    low=[]
    moderate=[]
    high=[]
    severe=[]

 
    dt = 10
    
    for station in stations:
        # List for dates and levels and use polyfit for predictions 
        # ignore stations with errors
        try:
            dates, levels = fetch_measure_levels(station.measure_id, dt=datetime.timedelta(days=dt))
            poly, time_shift = polyfit(dates, levels, 4)
            poly = np.poly1d(poly)
        except:
            print("There is an error with {}".format(station.name))
            continue
        
        # use predictions to calculate risks
        if station.typical_range == None:
            print("{} has no water level range".format(station.name))
            continue
        water_level_range = station.typical_range[1] - station.typical_range[0]
        level_day_after = poly(1)
        rel_level_day_after = (level_day_after - station.typical_range[0])/water_level_range

        # Rate the risk at ‘severe’, ‘high’, ‘moderate’ or ‘low’
        if rel_level_day_after <= 0.5:
            low.append(station.name)
        elif rel_level_day_after <= 1.0:
            moderate.append(station.name)
        elif rel_level_day_after <= 2.0:
            high.append(station.name)
        else:
            severe.append(station.name)

    # print list of stations at severe risk and the number of stations in each category
    print(severe)
    print("The number of stations at low risk are {}".format(len(low)))
    print("The number of stations at moderate risk are {}".format(len(moderate)))
    print("The number of stations at high risk are {}".format(len(high)))
    print("The number of stations at severe risk are {}".format(len(severe)))
    
        


if __name__ == "__main__":
    print("*** Task 2G: CUED Part IA Flood Warning System ***")
    run()