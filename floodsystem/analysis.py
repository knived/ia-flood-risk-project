"""This module contains a collection of functions related to
analysing data.

"""

import datetime
from matplotlib.dates import date2num 
import numpy as np
from floodsystem.datafetcher import fetch_measure_levels

def polyfit(dates, levels, p):
    """Returns a tuple of the polynomial object and any shift 
    of the time axis for a least-squares fit of a polynomial 
    of degree p to water level data"""
    # convert dates to floats
    dates = date2num(dates)

    # find coefficients of best-fit polynomial of degree p
    p_coeff = np.polyfit((dates - dates[0]), levels, p)

    # return tuple of polynomial and shift in time axis
    return (p_coeff, dates[0])