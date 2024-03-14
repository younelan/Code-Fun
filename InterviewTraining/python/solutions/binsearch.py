dodebug=[5,6]
dodebug=[0]
debugstrs=[]
def log(mystr,color="OKCYAN"):
	global debugstrs
	debugstrs.append([mystr,color])
def binarySearch(array, target):
	low_bound,high_bound=0,len(array)
	idx=0
	while high_bound-low_bound>0 and idx<20:
		idx+=1
		median = low_bound+(high_bound - low_bound)  //2
		log("high %i low %i median %i " % (high_bound,low_bound,median)),
		if array[median] == target:
			return median
		if array[median]>target:
			log("Median (%i->%i) > target (%i) " % (median,array[median],target))
			high_bound=median
		elif array[median]<target:
			log("Median (%i->%i) < target (%i) " % (median,array[median],target))
			low_bound=median+1
		else:
			if median<len(array) and array[median+1] == target:
				return median+1
				log("Jackpot idx+1")
			log("NEITHER: Median (%i->%i) neither < nor > than target (%i) " % (median,array[median],target))
			return -1

	return -1

def show_log():
	global debugstrs
	for out in debugstrs:
		debug.print_color(out[0],color=out[1])

	debugstrs=None
	debugstrs=[]



from AlgoHelper import console,testing	
script_name = "binSearch"
tests = testing.load_tests(script_name)

console.script_header("BINARY SEARCH")
idx=0
for test in tests:
	idx+=1
	console.test_header("Test %s" % idx)

	array,target = test["array"],test["target"]

	vars={}
	vars["Array"]=array
	console.print_variables(vars)

	vars={"Target": idx} 
	retval = binarySearch(array,target)

	if "expect" in test:
		color = "OKGREEN" if test["expect"]==retval else "FAIL"
		vars["Returned"]=console.get_color_str(retval,color)
		vars["Expect"]=retval
	else:
		vars["Returned"]=retval
	console.print_variables(vars)
	if idx in dodebug:
		print("-- Debug: ")
		show_log()
	else:
		debugstrs=[]
	debugstrs=[]