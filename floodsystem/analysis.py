"""This module contains a collection of functions related to
analysing data.

"""

def polyfit(dates, levels, p):
    """Returns a tuple of the polynomial object and any shift 
    of the time axis for a least-squares fit of a polynomial 
    of degree p to water level data"""

    # complete