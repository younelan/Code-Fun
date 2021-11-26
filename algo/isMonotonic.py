def isMonotonic(array):
	if len(array)<3:
		return True

	prev_element = array[0]
	prev_direction = 0

	for el in range(1,len(array)):
		cur_element=array[el]
		if cur_element>prev_element:
			cur_direction=1
			debug("  prev_direction: %s cur_direction %s" % (prev_direction,cur_direction))
			if prev_direction==-1:
				#print("    Exiting, direction change")
				return False
			#print("%s>%s "%(cur_element,prev_element))
		elif cur_element==prev_element:
			cur_direction=0
			debug("  prev_direction: %s cur_direction %s" % (prev_direction,cur_direction))
		else:
			cur_direction=-1
			debug("  prev_direction: %s cur_direction %s" % (prev_direction,cur_direction))
			if prev_direction==1:
				#print("    Exiting, direction change")
				return False			
			debug("  %s<%s "%(cur_element,prev_element))
		prev_element=cur_element
		if not prev_direction:
			prev_direction = cur_direction
	return True

from AlgoHelper import testing,tree,console
def debug(str,color=None):
    console.print_color("%s %s" % (color,str),color="OKGREEN")
    console.log(str,color=color)
    
script_name = "isMOnotonic"
tests = testing.load_tests(script_name)

console.script_header("Is Monotonic")
idx=0
for case in tests:
	idx+=1
	console.section_header ("test %i" % (idx))

	retval = isMonotonic(case["array"])
	print("*"*10)
	console.print_color(case["array"])
	print ("  == retval %s" % repr(retval))
	#print (retval)