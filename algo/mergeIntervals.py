def mergeOverlappingIntervals(intervals):
	retval=[]
	while intervals:
		range1 = intervals.pop(0)
		minval,maxval =range1
		rangemodified=False
		merged_ranges=[]

		for idx in range(len(intervals)):
			range2=intervals[idx]
			if ( 
				 (range1[0]>=range2[0] and range1[0]<=range2[1]) or 
			     (range1[1]<=range2[0] and range1[1]>=range2[1]) or
				 (range2[0]>=range1[0] and range2[0]<=range1[1]) or 
			     (range2[1]<=range1[0] and range2[1]>=range1[1])
			   ):

				merged_ranges.append(idx)

				range1=[
						  min( range1[0],range2[0] ) ,
						  max( range1[1],range2[1] )
						 ]
				rangemodified=True

		if merged_ranges:
				for idx in reversed(merged_ranges):
					intervals.pop(idx)
				intervals.append(range1)
		else:
			retval.append(range1)
	return retval
			
from AlgoHelper import testing,tree,debug

script_name = "mergeIntervals"
tests = testing.load_tests(script_name)

debug.script_header("MERGE INTERVALS")
idx=0
for case in tests:
	idx+=1
	debug.test_header("Test %s" % idx)

	intervals = case["intervals"][:]
	vars={"Intervals":case["intervals"],"Return":mergeOverlappingIntervals(intervals)}
	debug.print_variables(vars,row_size=1)