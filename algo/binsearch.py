dodebug=[5,6]
dodebug=[0]
debugstrs=[]
def debug(mystr,color="OKCYAN"):
	global debugstrs
	debugstrs.append([mystr,color])
def binarySearch(array, target):
	low_bound,high_bound=0,len(array)
	idx=0
	while high_bound-low_bound>0 and idx<20:
		idx+=1
		median = low_bound+(high_bound - low_bound)  //2
		debug("high %i low %i median %i " % (high_bound,low_bound,median)),
		if array[median] == target:
			return median
		if array[median]>target:
			debug("Median (%i->%i) > target (%i) " % (median,array[median],target))
			high_bound=median
		elif array[median]<target:
			debug("Median (%i->%i) < target (%i) " % (median,array[median],target))
			low_bound=median+1
		else:
			if median<len(array) and array[median+1] == target:
				return median+1
				debug("Jackpot idx+1")
			debug("NEITHER: Median (%i->%i) neither < nor > than target (%i) " % (median,array[median],target))
			return -1

	return -1
		#print("median %i more thn %i target" % (array[median],target))

bcolors = {
    "HEADER" : '\033[95m',
    "OKBLUE" : '\033[94m',
    "OKCYAN" : '\033[96m',
    "OKGREEN" : '\033[92m',
    "WARNING" : '\033[93m',
    "FAIL" : '\033[91m',
    "ENDC" : '\033[0m',
    "BOLD" : '\033[1m',
    "UNDERLINE" : '\033[4m'

	
}
def printcolor(outstr,color="OKBLUE"):
	print(bcolors[color]),
	if not isinstance(outstr,str):
		outstr=repr(outstr)
	print("      " + outstr)
	print(bcolors["ENDC"]),
def debugout():
	global debugstrs
	for out in debugstrs:
		printcolor(out[0],color=out[1])

	debugstrs=None
	debugstrs=[]

array=[0,2,5,7,20,60,70,103,400]
target=50
tests=[
{
  "array": [0, 1, 21, 33, 45, 45, 61, 71, 72, 73],
  "target": 0,
  "expect": 0
},
{
  "array": [0, 1, 21, 33, 45, 45, 61, 71, 72, 73],
  "target": 33,
  "expect": 3

},
{
  "array": [1, 5, 23, 111],
  "target": 111,
  "expect":3
},
{
  "array": [1, 5, 23, 111],
  "target": 5,
  "expect": 1

},
{
  "array": [0, 1, 21, 33, 45, 45, 61, 71, 72, 73],
  "target": 71,
  "expect":7
},
{
  "array": [0, 1, 21, 33, 45, 45, 61, 71, 72, 73],
  "target": 72,
  "expect": 8
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
	retval = binarySearch(array,target)
	if "expect" in test:
		color = "OKGREEN" if test["expect"]==retval else "FAIL"
		resultstr="%i (Expect: %i)" % (retval,test["expect"])
		printcolor(resultstr,color)
	else:
		print(retval)
	if idx in dodebug:
		print("-- Debug: ")
		debugout()
	debugstrs=[]