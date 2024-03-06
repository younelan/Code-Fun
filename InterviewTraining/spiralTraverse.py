import sys
def spiralTraverse(array):
		min_x,min_y,max_x, max_y = 0,0 , len(array[0])-1 ,  len(array)-1
		retval=[]
		while min_x<=max_x and min_y<=max_y :
			print( "min_x %i, min_y %i max_x %i max_y %i " 
						% (min_x,min_y,max_x,max_y) )
		
			retval += array[min_y][min_x:max_x+1]

			for row in range(min_y+1,max_y+1):
				retval.append(array[row][max_x])
			#print(retval)
			#sys.exit()
			if max_y > min_y:
				retval += list(reversed(array[max_y][min_x:max_x]))
			if max_x > min_x:
				for row in range(max_y-1,min_y,-1):
					retval.append(array[row][min_x])
			
			max_x -= 1
			min_x += 1
			min_y += 1
			max_y -= 1
		
		return retval
 
def oldspiralTraverse(array):
    # Write your code here.
	visited = [ 0 * len(array[0]) ] * len(array)
	retval = []
	x = 0 
	y = 0
	min_x,min_y,max_x, max_y = 0,0 , len(array[0]) ,  len(array)
	UP,LEFT,RIGHT,DOWN=range(4)
	directions=["UP","LEFT","RIGHT","DOWN"]
	direction=RIGHT
	while min_x<=max_x and min_y<=max_y :
		console.log( "x %i y %i min_x %i, min_y %i max_x %i max_y %i array[y][x] %i dir: %s " 
						% (x,y,min_x,min_y,max_x,max_y,array[y][x],directions[direction]) )
		
		retval.append(array[y][x])
		if direction==RIGHT:
			if x<max_x-1:
				x+=1
			else:
				direction=DOWN
				y+=1
				min_x+=1
		elif direction==DOWN:
			if y<max_y-1:
				y+=1
			else:
				direction=LEFT
				x-=1
				min_y+=1
		elif direction==LEFT:
			if x>=min_x:
				x-=1
			else:
				direction=UP
				y-=1
				max_x-=1
		elif direction==UP:
			if y>min_y:
				y-=1
			else:
				direction=RIGHT
				x+=1
				max_y -= 1

	return retval

from AlgoHelper import console,testing,graphs

script_name = "spiralTraverse"
tests = testing.load_tests(script_name)

details=[3]
console.script_header(script_name)
idx=0
for case in tests:
	idx+=1

	console.test_header("test %i" % ( idx))

	input_array,expect=case["array"],case["expect"]

	retval = spiralTraverse(input_array)
	print("INPUT:")
	for line in input_array:
		line = "          [ %s ]" % ", ".join(["%2i" %val for val in line]) 
		print(line)
	print("Expected: %s" % console.get_color_str(expect,"BOLD") )
	print("Returned: %s" % console.get_color_str(retval,"BOLD") )
	
	# console.print_variables(vars)
	if idx in details:
	     console.debug_out()
	else:
	     console.flush()




