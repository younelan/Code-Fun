dodebug=[3]
debugstrs=[]
def debug(mystr,color="OKCYAN"):
	global debugstrs
	debugstrs.append([mystr,color])

def findFirstWrong(array,outliar):
	idx=0
 
	while outliar>=array[idx] :
		debug("%i < %i  (%i)" %(outliar, array[idx],idx))
		idx+=1

		
	dupetest=array[idx]
	if idx<len(array)-1 and array[idx+1]==dupetest:
		debug("Looking for dupe")
		while idx<len(array)-1 and array[idx]==dupetest:
			idx+=1


	debug("findFirstWrong %i - returns %i" %(outliar,idx))

	return idx
	#for idx in range(len(array),0,-1):

def subarraySort(array):
	if len(array)<2:
		return [-1,-1]
	if len(array)==2 and array[0]>array[1]:
		return [0,1]
	is_sorted = True
	prev = array[0]
	first_wrong=None
	last_wrong=None

	for idx in range(len(array)-1):

		current_val = array[idx]
		next_idx = idx + 1
		next_val = array[next_idx]

		debug("***** idx %i val %i next %i *****" %(idx,current_val,next_val),color="FAIL")
		if not is_sorted:
			debug("***** 1stwrong %i min_wrong_val %i last_wrong %i max_wrong_val %i *****" %(first_wrong,min_wrong_val,last_wrong,max_wrong_val),color="OKGREEN")

		if is_sorted:
			if current_val>next_val:
				debug("Array not sorted %i < %i" %(current_val,next_val))
				first_wrong = findFirstWrong(array,next_val)
				last_wrong = next_idx
				min_wrong_val = next_val
				max_wrong_val = next_val
				is_sorted = False
		else:
			if next_val<current_val:
				debug("Setting last wrong to %i " %next_idx)
				last_wrong=next_idx


				tmpmax = max( array[first_wrong:next_idx])
				debug("***** findmax first_wrong %i next_idx %i tmp_max %i *****" %(first_wrong,next_idx,tmpmax),color="FAIL")
			
				if tmpmax>max_wrong_val:
					max_wrong_val = tmpmax
			
				if next_val>max_wrong_val:
					max_wrong_val = next_val
					last_wrong = next_idx

			if next_val<min_wrong_val:
				first_wrong = findFirstWrong(array,min_wrong_val)
				min_wrong_val = next_val
				last_wrong = next_idx
		# if not is_sorted and next_val>max_wrong_val:
		# 	max_wrong_val = next_val
		# 	last_wrong = next_idx
	
	if is_sorted == True:
		return [-1,-1]
	else:
		return [first_wrong,last_wrong]





def subarraySort2(array):
	retval = []
	isSorted = True
	prev=array[0]
	firstwrong=float("inf")
	for idx in range(1,len(array)):
		debug("***** idx %i *****" %(idx),color="FAIL")

		if array[idx]<prev and isSorted==True:
			isSorted=False
			count=0
			firstwrong=idx
			lastwrong=idx

			minWrongVal=array[idx]
			maxWrongVal=array[idx]
			debug("Array not sorted, %i < %i (firstwrong: %i lastwrong: %i" % (array[idx],prev,firstwrong,lastwrong))

		elif  array[idx]<prev:
			lastwrong=idx
			debug("Hello")

			if array[firstwrong:idx]:
				maxWrongVal = max(array[firstwrong:idx])
				debug("maxWrongVal %i " %(maxWrongVal))

			firstwrong = findFirstWrong(array,maxWrongVal)


			# debug( arrayToStr(array[firstwrong:lastwrong]) )
			# if not isSorted and array[firstwrong:lastwrong]:
			# 	print("world")
			# 	firstwrong = findFirstWrong(array,min(array[firstwrong:lastwrong]))


		# if not isSorted and array[idx]<=maxWrongVal:
		# 	maxwrong=idx

		prev = array [ idx ]

	if isSorted:
		return [-1,-1]
	else:
		if array[firstwrong:lastwrong]:
			firstWrong = findFirstWrong(array,min(array[firstwrong:lastwrong]))
		return [firstwrong,lastwrong]

def arrayToStr(array):
	arr= [str(i) for i in array]
	return "[ " + ", ".join(arr) + ' ]'


def OldsubarraySort(array):
	retval=[]
	isSorted=True
	prev=array[0]
	#positions={}
	firstwrong=0
	lastwrong = len(array)
	count=1
	for idx in range(1,len(array)):

		count+=1
		if array[idx]<prev:
			if isSorted==True:
				firstwrong=idx
				maxWrongVal=array[idx]
			#debug("Array not sorted, %i < %i" % (array[idx],prev))
			isSorted=False
			count=0

		if array[nex_idx]<array[firstwrong]:
			firstWrong = findFirstWrong(array,array[nexidx])
			maxWrongVal = max(array[firstwrong:idx])
			#debug("Max Wrong Val %i "%maxWrongVal)
			lastwrong=idx
			#debug("lastwrong set to %i " %(idx))
		if isSorted==False:
			#debug("--- maxWrongVal, %i < %i" % (array[idx],maxWrongVal))
			if array[idx]<maxWrongVal:
				#debug("Oops %i" % idx)
				lastwrong=idx

		prev = array[idx]
	

	maxval = len(array)

	if isSorted:
		return [-1,-1]
	else:
		firstWrong = findFirstWrong(array,min(array[firstwrong:lastwrong]))
		return [firstwrong,lastwrong]


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
def printcolor(str,color="OKBLUE"):
	print(bcolors[color]),
	print("      " + str)
	print(bcolors["ENDC"]),
def debugout():
	global debugstrs
	for out in debugstrs:
		printcolor(out[0],color=out[1])

	debugstrs=None
	debugstrs=[]

tests = [
{
  "array": [1, 2],
  "expect": [-1,-1]
},
{
  "array": [2, 1],
  "expect": [0,1]
},
{
  "array": [1, 2, 4, 7, 10, 11, 7, 12, 7, 7, 16, 18, 19],
  "expect": [4,9]
},
{
  "array": [1, 2, 4, 7, 10, 11, 7, 12, 13, 14, 16, 18, 19],
  "expect": [4,6]
},

{
  "array": [1, 2, 8, 4, 5],
  "expect": [2,4]
},
{
  "array": [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19],
  "expect": [3,9]
},
{
  "array": [1, 2, 3, 4, 5, 6, 18, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19],
  "expect": [6,16]
},
	{
  		"array": [4, 8, 7, 12, 11, 9, -1, 3, 9, 16, -15, 51, 7],
		"expect": [0,12]
	},

]

idx=0
print(bcolors["BOLD"]),
print("""
+++++++++++++++++++++++++++++++++
Largest subarray needing sorting
+++++++++++++++++++++++++++++++++

""")
print(bcolors["ENDC"])
for case in tests:
	idx+=1
	print ("\n%s test %i %s \n" % ("*"*30 , idx, "*"*30))
	val=subarraySort(case["array"])
	print("-- Expected: "),
	if val[0]==case["expect"][0] and val[1]==case["expect"][1]:
		print(bcolors["OKGREEN"]),
	else:
		print(bcolors["FAIL"]),
	print(case["expect"]), 
	print(bcolors["ENDC"]),
	print("-- Output: "),
	if val[0]==case["expect"][0] and val[1]==case["expect"][1]:
		print(bcolors["OKGREEN"]),
	else:
		print(bcolors["FAIL"]),
	print(val),
	print(bcolors["ENDC"]),
	print("  -- Input: "),
	fmtstring=bcolors["ENDC"]  + "%i" + bcolors["FAIL"]+ ">" + bcolors["HEADER"] +"%i " + bcolors["ENDC"]
	casearray=[ fmtstring % (x,y) for x,y in enumerate(case["array"])]
	printcolor(arrayToStr(casearray),color="BOLD")

	if idx in dodebug:
		print("-- Debug: ")
		debugout()
	debugstrs=[]