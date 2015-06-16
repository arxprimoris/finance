# -*- coding: utf-8 -*-
"""
Finance helper functions
"""

"""
    Returns future value given current value and other parameters.
"""
def futureValue(value, rate, periods = 1, payment = 0):
    return value * ((1 + rate) ** periods)

def presentValue(value, rate, periods = 1, payment = 0):
    return value / (((1 + rate) ** periods))