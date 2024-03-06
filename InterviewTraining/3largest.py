#find 3 largest numbers in array
def findThreeLargestNumbers(array):
    retval=[float("-inf")]*3
    for val in array:
        if val>retval[2]:
            retval=[retval[1],retval[2],val]
        elif val>retval[1]:
            retval=[retval[1],val,retval[2]]
        elif val>retval[0]:
            retval=[val,retval[1],retval[2]]
    return retval


from AlgoHelper import testing,tree,console

script_name = "3largest"
tests = testing.load_tests(script_name)

console.script_header("3 largest numbers")
idx=0
for case in tests:
    idx+=1
    console.test_header("Test %s" % idx)

    retval=findThreeLargestNumbers(case["array"])
    case["returned"]=retval

    console.print_variables(case)
    console.debug_out()
