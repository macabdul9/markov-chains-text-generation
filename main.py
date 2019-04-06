"""
 @author    : macab (macab@debian)
 @file      : main
 @created   : Saturday Apr 06, 2019 19:47:44 IST
"""

import numpy
import freqtable as f
import convertToProb as cp

def sampleNext(model, input_str):
    X = input_str[-3:]
    if X in model:
        outcomes = list( model[X].keys() )
        probs = list( model[X].values() )
        return numpy.random.choice(outcomes, p=probs)
    else:
        return " "


seq = "hello hello world world world world hello"
table = f.freqtable(seq, 3)
model = cp.convertToProb(table)
print(sampleNext(model, "hel"))
