
def minimumWaitingTime(queries):
    current=0
    sum=0

    if len(queries)<2:
        return 0
    for el in sorted(queries):
        sum=sum+current
        current=current+el

    return sum


from AlgoHelper import testing,tree,console

script_name = "minWaitTime"
tests = testing.load_tests(script_name)

console.script_header("Minimum Wait Time")
idx=0
for case in tests:
    idx+=1
    console.test_header("Test %s" % idx)

    queries = case["queries"][:]
    retval=minimumWaitingTime(queries)
    case["returned"]=retval

    #vars={"Intervals":case["queries"],"Return":retval}
    console.print_variables(case)
    console.debug_out()

# console.script_header("Is Monotonic")
# idx=0
# for case in tests:
# 	idx+=1
# 	console.section_header ("test %i" % (idx))

# 	retval = isMonotonic(case["array"])
# 	case["returned"]=retval
# 	console.print_variables(case)
# 	console.debug_out()