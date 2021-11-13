def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
	retval=[]
	min_diff = float('inf')
	for i in range(0,len(arrayOne),1):
		for j in range(0,len(arrayTwo),1):
			#print (min_diff,i,j,arrayOne[i],arrayTwo[j],arrayOne[i]-arrayTwo[j])
			if abs(arrayOne[i]-arrayTwo[j])<min_diff:
				#print ("hello",(arrayOne[i]-arrayTwo[j]))
				min_diff=abs(arrayOne[i]-arrayTwo[j])
				#print(min_diff)
				retval=[arrayOne[i],arrayTwo[j]]
			if abs(arrayTwo[j]-arrayOne[i])<min_diff:
				min_diff=abs(arrayTwo[j]-arrayOne[i])
				retval=[arrayTwo[j],arrayOne[i]]


	return retval

tests = [
	{
	  "arrayOne": [-1, 5, 10, 20, 28, 3],
	  "arrayTwo": [26, 134, 135, 15, 17]
	}

]

testid=0
retval = smallestDifference(tests[testid]["arrayOne"],tests[testid]["arrayTwo"])

print(tests[testid]["arrayOne"],tests[testid]["arrayTwo"])
print ("retval",)
print (retval)