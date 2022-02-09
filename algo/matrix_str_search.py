#!/usr/bin/env python
import sys

"""
Given a string and a rectangular matrix of characters,
determine whether the string occurs in the matrix in a straight line horizontally, vertically, or diagonally
(in these 8 possible directions: N, NE, E, SE, S, SW, W, NW).
The function/method should take as input a matrix and a string,
and return a boolean indicating whether the string is present in the matrix.

Sample inputs:
M = ["ABCDE",
     "FGHIJ",
     "KLMAB"]
S = "ABC" => Find(M, S) should return True (the string S occurs in the east direction)
    "GHI" =>                          True (east)
    "IHG" =>                          True (west)
    "DIA" =>                          True (south)
    "IA" =>                           True (south)
    "DI" =>                           True (south)
    "FL" =>                           True (south-east)
    "AGM" =>                          True (south-east)
    "GM" =>                           True (south-east)
    "BHA" =>                          True (south-east)
    "AHB" =>                          True (north-west)
    "AL" =>                           False (not contiguous)
    "ABG" =>                          False (not a straight line)
    "IJF" =>                          False (no wrapping around allowed)


The inputs may be empty.
Assume that all the rows of the matrix have the same length.
15:52pm start coding
"""


def matrix_search(M,S):
    width,height=len(M[0]), len(M)
    for x in range(width):
        for y in range(height):
            if M[y][x]==S[0]:
                retval,direction=full_word_search(M,x,y,S)
                if retval:
                    return True,direction
    return False,""
def full_word_search(M,start_x,start_y,target):
    width,height=len(M[0]), len(M)
    search_params=[(1,1,"south-east"),(-1,-1,"south-west"),(1,0,"south"),(0,1,"east"),(0,-1,"west"),(-1,0,"north")]
    
    for increment in search_params:
        idx=0
        col,row,t_length = start_x,start_y,len(target)
        tmp=""
        while row>=0 and col>=0 and col<width and row<height and col<width and M[row][col]==target[idx]:
            tmp+= M[row][col]
            idx+=1
            row+=increment[0]
            col+=increment[1]
            if idx==t_length:
                return (True,increment[2])

    return (False,""   ) 
 
tests = [
    {
    "arr":[ "ABCDE",
            "FGHIJ",
            "KLMAB"
        ],
    "inputs" : [
        ["ABC", True ,"east"],
        ["GHI", True , "east"],
        ["IHG",True,"west"],
        ["DIA",True,"south"],
        ["IA", True,"south"],
        ["DI", True,"south"],
        ["AGM", True,"south-east"],
        ["GM", True,"south-east"],
        ["BHA", True,"south-east"],
        ["AHB", True,"north-west"],
        ["AL", False,"not contiguous"],
        ["AL", False,"not a straight line"],
        ["AL", False,"no wrapping around allowed"],
    ]
    }
]


for test in tests:
    print "*"*20
    for line in test["arr"]:
        print line
    for parameters in test["inputs"]:
        input_str,expect_val,expect_direction=parameters
        retval,retdir = matrix_search(test["arr"],input_str)
        print("Test Input: %s | Returned %s (%s) | Expected: %s (%s) " % (input_str,retval, retdir,expect_val,expect_direction ))

sys.exit()

""""
def find_string(M,S):
  if not M: 
    return False
  
  #horizontal
  for line in M:
    if line.find(S) >=0 :
      return True
    
    if line[::-1].find(s)>=0:
      return True
  #vertical 
  width = len(M[0])
  height = len(M)
  for col in range(width):
    #while row<height-range(len(S)):
    #  match=True
     tmp_str=""
     for i in range(len(M)):
        tmp_str+=M[i][col]
     if tmp_str.find(S)>=0:
        return True
     if tmp_str[::-1].find(S)>=0:
        return True
 
  #diagonal
  return False
"""

"""
if M[row][col]==S[0]:
for i range(len(S)):
    if M[row+i][col] != S[i]:
    match=False
    break

if match == True:
    return True

if row+len(S)-1<height and M[row+len(S)-1][col]==S[-1]:
for i in range(height):
    array_row = height - idx
    if M[height-row+i][col] != S[i]:
    match=False
    break
"""
# 16:29pm end coding
