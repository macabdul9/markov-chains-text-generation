"""
 @author    : macab (macab@debian)
 @file      : freqtable
 @created   : Saturday Apr 06, 2019 19:44:13 IST
"""


def freqtable(seq, k):
    table = {}
    l = len(seq)
    for i in range(l - k):
        chunk = seq[i:i + k]
        nextchar = seq[i + k]
        if chunk in table:
            if nextchar in chunk:
                table[chunk][nextchar] += 1
            else:
                table[chunk][nextchar] = 1
        else:
            table[chunk] = {
                nextchar : 1
            }

    return table
