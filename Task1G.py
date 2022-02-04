from floodsystem.stationdata import build_station_list
import plotly.express as px  # noqa

def run():
    """Requirements for Task Extension"""

    # Build list of stations
    stations = build_station_list()

    # list of longitudes
    latitudes = [station.coord[0] for station in stations]

    # list of latitudes
    longitudes = [station.coord[1] for station in stations]

    # list of names
    names = [station.name for station in stations]

    # list of towns
    towns = [station.town for station in stations]

    # list of rivers
    rivers = [station.river for station in stations]

    # Display the location of each station on a map
    fig = px.scatter_mapbox(names, lat=latitudes, lon=longitudes, hover_name=names, 
            hover_data=[towns, rivers], color_discrete_sequence=["royalblue"], zoom=5.2, 
            height=600, labels={"lat": "Latitude", "lon": "Longitude", 
            "hover_data_0": "Town", "hover_data_1": "River"})

    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    fig.show()

if __name__ == "__main__":
    print("*** Task Extension: CUED Part IA Flood Warning System ***")
    run()