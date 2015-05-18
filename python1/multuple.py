#!/usr/local/bin/python3

multuple=((1, 1), (2, 2), (12, 13), (4, 4), (99, 98))

for curTuple in multuple:
    total=curTuple[1]*curTuple[0]
    print("{0:5d} = {1:2d} x {2:2d}" .format(total,curTuple[0],curTuple[1]) )