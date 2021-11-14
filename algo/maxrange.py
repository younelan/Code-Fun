def largestRange(array):
	arr=sorted(array)
	if len(array)==1:
		return [array[0],array[0]]
	if len(array)==2:
		return sorted(array)
	first = arr.pop(0)
	print("First",first,arr)
	prev,last = first,first
	minval,maxval = first,first
	count=0
	while arr:
		cur = arr.pop(0)
		if cur==prev:
			continue
		if prev+1==cur:
			count+=1
			last=cur
			if last-first > maxval-minval:
				minval = first
				maxval = last

		print(cur,minval,maxval,first,last,"---",arr)
		if not arr:
			print("End of array, returning %i-%i" % (minval,maxval))
			return [minval,maxval]
		elif prev+1!=cur:
			first = cur
			count = 1

		prev=cur

	print("End of function, returning %i-%i" %(minval,maxval))
	return [minval,maxval]

tests = [
{
  "array": [1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6],
  "expect": [0,7]
},
{
  "array": [4, 2, 1, 3, 6],
  "expect": [1,4]
},
{
  "array": [0, 9, 19, -1, 18, 17, 2, 10, 3, 12, 5, 16, 4, 11, 8, 7, 6, 15, 12, 12, 2, 1, 6, 13, 14],
  "expect": [-1,19]
}

]

idx=0
for case in tests:
    idx+=1
    print ("\n%s test %i *********" % ("*"*20 , idx))
    print("-- Input ")
    print(case["array"])
    print("-- Output ")
    val=largestRange(case["array"])
    print(val)
    print("-- Expected ")
    print(case["expect"])
