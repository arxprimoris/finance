# -*- coding: utf-8 -*-
"""
Finance helper functions
"""

"""
    Returns future value given current value and other parameters.
"""    
def futureValue(value, rate, periods = 1, payment = 0):
    total = value * ((1 + rate) ** periods)
    for curPeriod in range(0, periods):
        total = total + (payment * ((1 + rate) ** curPeriod))
        
    return total
    
"""
    Returns present value given current value and other parameters.
"""
def presentValue(value, rate, periods = 1, payment = 0):
    total = value / ((1 + rate) ** periods)
    for curPeriod in range(0, periods):
        total = total + (payment / ((1 + rate) ** curPeriod))
        
    return total