def spiralTraverse(array):
    # Write your code here.
	visited = [ 0 * len(array[0]) ] * len(array)
	retval = []
	x = 0 
	y = 0
	min_x,min_y,max_x, max_y = 0,0 , len(array[0]) ,  len(array)
	UP,LEFT,RIGHT,DOWN=range(4)
	direction=RIGHT
	while min_x<max_x and min_y<max_y :
		print(x,y,min_x,min_y,max_x,max_y)
		retval.append(array[y][x])
		print("     %i" % array[y][x])
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
			if y>=min_y:
				y-=1
			else:
				direction=RIGHT
				x+=1
				max_y -= 1

	return retval



tests = [
{
  "array": [	
  	[1, 2, 3, 4],
	[12,13,14,5],
	[11,16,15,6],
	[10, 9, 8,7],
	],
  "expect": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
},
{
  "array": [
    [4, 2, 3, 6, 7, 8, 1, 9, 5, 10],
    [12, 19, 15, 16, 20, 18, 13, 17, 11, 14]
  ],
	"expect":[4, 2, 3, 6, 7, 8, 1, 9, 5, 10, 14, 11, 17, 13, 18, 20, 16, 15, 19, 12]

}


]



testid=0
for case in tests:
	retval = spiralTraverse(case["array"])
	print("*"*10)
	print("  Inputs:")
	for key,val in case.items():
		print("   ",key,val)
	print ("\n  == Output"),
	print (retval)