def threeNumberSum(array, targetSum):
	# Write your code here.
	arrSorted=sorted(array)
	retval = []

	idx1, idx2, idx3=0 , 0, 0
	while idx1 < len(arrSorted)-2:
		val1=arrSorted[idx1]
		idx2 = idx1 + 1
		while idx2 < len(arrSorted)-1:
			val2=arrSorted[idx2] 
			idx3=idx2+1
			while idx3 < len(arrSorted):
				val3=arrSorted[idx3] 
				idx3 += 1
				if val1 + val2 + val3 == targetSum:
					retval.append([val1,val2,val3])
				print(idx1,idx2,idx3)

			idx2 += 1	


			idx1 += 1
			
	return retval

tests = [
	{
  "array": [12, 3, 1, 2, -6, 5, -8, 6],
  "targetSum": 0
	}

]

testid=0
retval = threeNumberSum(tests[testid]["array"],tests[testid]["targetSum"])

print ("retval",retval)