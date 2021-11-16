def binarySearch(array, target):
	low_bound,high_bound=0,len(array)
	while high_bound-low_bound>0:
		median = (high_bound - low_bound)  //2
		if array[median] == target:
			return median
		if array[median]>target:
			low_bound=median+1
		elif array[median]>target:
			high_bound=median
		else:
			return median

	return -1
		#print("median %i more thn %i target" % (array[median],target))
	#print("smax %i smin %i median %i " % (smax,smin,median))
			
	return -1
array=[0,2,5,7,20,60,70,103,400]
target=50
tests=[{
  "array": [0, 1, 21, 33, 45, 45, 61, 71, 72, 73],
  "target": 33
},
{
  "array": [1, 5, 23, 111],
  "target": 111
},
{
  "array": [1, 5, 23, 111],
  "target": 5
},
{
  "array": [0, 1, 21, 33, 45, 45, 61, 71, 72, 73],
  "target": 0
}
]
idx=0
for test in tests:
	idx+=1
	print ("\n%s test %i %s \n" % ("*"*30 , idx, "*"*30))
	array,target = test["array"],test["target"]
	print("Target %i " % target), 
	print("-- Array "),
	print(array)
	print binarySearch(array,target)