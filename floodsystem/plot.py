"""This module contains a collection of functions related to
plotting data.

"""

import datetime
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.dates import date2num 
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit

def plot_water_levels(stations, dt):
    """Plots the water level data against time for up to 6 stations 
    including the typical low and high levels on each plot where stations
    is a list of MonitoringStation object and dt is the number of
    days back the data should be plotted for."""

    # check length of list
    if len(stations) > 6:
        raise ValueError("Input should be a list of six or less stations")

    # subplot position
    i = 0
    
    # for each station:
    for station in stations:
        # set position of subplot
        i += 1
        # fetch dates and levels
        dates, levels = fetch_measure_levels(
            station.measure_id, dt=datetime.timedelta(days=dt))
        # plot formatted dates and levels on sublpot
        plt.subplot(2, 3, i)
        plt.plot(dates, levels, label = f"Past {dt} Days")
        # add axis and labels to plot
        plt.xlabel('Date')
        plt.ylabel('water Level (m)')
        plt.xticks(rotation=45)
        plt.title(f"{station.name}")
        # plot typical low and high levels on subplot
        plt.axhline(y = station.typical_range[0], color = "g", 
                        label = "Typical Low Level", ls = "--")
        plt.axhline(y = station.typical_range[1], color = "r", 
                        label = "Typical High Level", ls = "--")
        # plot legend
        if i == 1:
            plt.legend()

    # show plot
    plt.tight_layout()
    plt.show()


def plot_water_level_with_fit(stations, dt, p):   
    """Plots the water level data and the best-fit polynomial
    for up to 6 stations where stations is a list of MonitoringStation object,
    dt is the number of days back the data should be plotted for and p is the
    polynomial degree to use for calculating the best-fit polynomial."""

    # check length of list
    if len(stations) > 6:
        raise ValueError("Input should be a list of six or less stations")

    # subplot position
    i = 0
    
    # for each station:
    for station in stations:
        # set position in subplot
        i += 1
        # fetch dates and levels
        dates, levels = fetch_measure_levels(
            station.measure_id, dt=datetime.timedelta(days=dt))
        # plot formatted dates and levels on sublpot
        plt.subplot(2, 3, i)
        plt.plot(dates, levels, label = f"Past {dt} Days")
        # calculate best fit polynomial
        poly, d0 = polyfit(dates, levels, p)
        poly = np.poly1d(poly)
        # convert dates to floats for plotting
        dates = date2num(dates)
        # plot best fit polynomial
        plt.plot(dates, poly(dates - d0), label = "Least-squares Fit")
        # add axis and labels to plot
        plt.xlabel('Date')
        plt.ylabel('water Level (m)')
        plt.xticks(rotation=45)
        plt.title(f"{station.name}")
        # plot typical low and high levels on subplot
        plt.axhline(y = station.typical_range[0], color = "g", 
                        label = "Typical Low Level", ls = "--")
        plt.axhline(y = station.typical_range[1], color = "r", 
                        label = "Typical High Level", ls = "--")
        # plot legend
        if i == 1:
            plt.legend()

    # show plot
    plt.tight_layout()
    plt.show()