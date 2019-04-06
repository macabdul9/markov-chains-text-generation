"""
 @author    : macab (macab@debian)
 @file      : main
 @created   : Saturday Apr 06, 2019 19:45:21 IST
"""

import numpy

def convertToProb(table):
    for key in table:
        total = sum(table[key].values())
        for each in table[key]:
            table[key][each] /= total
    return table



