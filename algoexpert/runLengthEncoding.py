def runLengthEncoding(string):
    # Write your code here.
    counter=1
    prevchar=string[0]
    retval=""
    for char in string[1:]:
        if prevchar == char:
            counter += 1
            if counter>9:
                retval += "9" +char
                counter=1
        else:
            retval += str(counter) + prevchar
            prevchar=char
            counter=1
    retval += str(counter) + prevchar
    return retval


tests = [

    {
        "string": "AAAAAAAAAAAAABBCCCCDD",
        "expect":"9A4A2B4C2D"
    },
    {
        "expect":"1a1A",
        "string": "aA"

    },
    {
        "expect":"112233",
        "string": "122333"
    },
    {
        "expect":"9*3*7^6$7%6!9A9A2A",
         "string": "************^^^^^^^$$$$$$%%%%%%%!!!!!!AAAAAAAAAAAAAAAAAAAA"

    }
]
idx=0
for case in tests:
    idx+=1
    print ("\n%s test %i *********" % ("*"*20 , idx))
    print("-- String ")
    print(case["string"])
    print("-- Output ")
    val=runLengthEncoding(case["string"])
    print(val)
    print("-- Expected ")
    print(case["expect"])
