#!/usr/bin/env/python

#Given n by n matrix, where all 1 come before 0s
#return longest non zero row

arr=[
     [1,1,1,0,0],
     [1,1,1,1,1],
     [1,1,0,0,0],
     [1,1,1,1,0],
    ]

def longest_row_idx(arr):
    max_len=0
    max_idx=0
    for idx,row in enumerate(arr):
        count=0
        for val in row:
            if not val:
                break
            count += 1
        if max_len<count:
            max_len=count
            max_idx=idx

    return max_idx

print longest_row_idx(arr)
