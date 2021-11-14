def isMonotonic(array):
	if len(array)<3:
		return True

	prev_element = array[0]
	prev_direction = 0

	for el in range(1,len(array)):
		cur_element=array[el]
		if cur_element>prev_element:
			cur_direction=1
			#print("  prev_direction: %s cur_direction %s" % (prev_direction,cur_direction))
			if prev_direction==-1:
				#print("    Exiting, direction change")
				return False
			#print("%s>%s "%(cur_element,prev_element))
		elif cur_element==prev_element:
			cur_direction=0
			#print("  prev_direction: %s cur_direction %s" % (prev_direction,cur_direction))
		else:
			cur_direction=-1
			#print("  prev_direction: %s cur_direction %s" % (prev_direction,cur_direction))
			if prev_direction==1:
				#print("    Exiting, direction change")
				return False			
			#print("  %s<%s "%(cur_element,prev_element))
		prev_element=cur_element
		if not prev_direction:
			prev_direction = cur_direction
	return True

tests = [
{
  "array": [-1, -5, -10, -1100, -900, -1101, -1102, -9001],
  "expect": False
},
{
  "array": [-1, -5, -10, -1100, -1100, -1101, -1102, -9001],
  "expect": False
},
{
  "array": [1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 7, 9, 10, 11],
  "expect": False
},
{
  "array": [-1, -1, -2, -3, -4, -5, -5, -5, -6, -7, -8, -7, -9, -10, -11],
  "expect": False

}

]

testid=0
for case in tests:
	retval = isMonotonic(tests[testid]["array"])
	print("*"*10)
	print(tests[testid])
	print ("  == retval"),
	print (retval)