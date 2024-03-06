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
        ["ABC", True ,"east"],["GHI", True , "east"],
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
