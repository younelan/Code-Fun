def sameBsts(arrayOne, arrayTwo):
	if len(arrayOne)!=len(arrayTwo):
		return False
	if not arrayOne and not arrayTwo:
		return True
	if arrayOne:
		root1 = arrayOne.pop(0)
	else:
		root1 = None
	if arrayTwo:
		root2 = arrayTwo.pop(0)
	else:
		root2 = None
		
	smaller1=[]
	smaller2 =[]
	larger1 =[]
	larger2 =[]
	if root1!=root2:
		return False
	for i in range(len(arrayOne)):
		if arrayOne[i]<root1:
			smaller1.append(arrayOne[i])
		else:
			larger1.append(arrayOne[i])

		if arrayTwo[i]<root1:
			smaller2.append(arrayTwo[i])
		else:
			larger2.append(arrayTwo[i])
	if smaller1 or larger1:
		small_valid = sameBsts(smaller1, smaller2)
		large_valid = sameBsts(larger1, larger2)
	else:
		small_valid = True
		large_valid = True
		
	if not small_valid or not large_valid:
		return False
	return True

#Helper functions
def output(root, depth=0,isleft=0):
    # Write your code here.
    if isleft==0:
    	pos="Root"
    elif isleft==-1:
    	pos="Left"
    elif isleft==1:
    	pos="Right"
    print("%s %s (%s)" % ("    "*(depth+1),root.value,pos))
    newdepth=depth+1
    if root.left:
        output(root.left,depth=newdepth,isleft=-1)
    if root.right:
        output(root.right,depth=newdepth,isleft=1)

tests = [
{
  "arrayOne": [10, 15, 8, 12, 94, 81, 5, 2, 11],
  "arrayTwo": [10, 8, 5, 15, 2, 12, 11, 94, 81],
  "expect": "True"
},
{
  "arrayOne": [1, 2, 3, 4, 5, 6, 7],
  "arrayTwo": [1, 2, 3, 4, 5, 6, 7],
  "expect": "True"
},
{
  "arrayOne": [7, 6, 5, 4, 3, 2, 1],
  "arrayTwo": [7, 6, 5, 4, 3, 2, 1],
  "expect": "True"
},
{
  "arrayOne": [10, 15, 8, 12, 94, 81, 5, 2],
  "arrayTwo": [10, 8, 5, 15, 2, 12, 94, 81],
  "expect": "True"
},

{
  "arrayOne": [10, 15, 8, 12, 94, 81, 5, 2],
  "arrayTwo": [11, 8, 5, 15, 2, 12, 94, 81],
  "expect": "False"
}

]

idx=0
for case in tests:
    idx+=1
    print ("\n%s test %i *********" % ("*"*20 , idx))
    arr1=[str(i) for i in case["arrayOne"]]
    arr2=[str(i) for i in case["arrayTwo"]]
    print("Array 1: [%s]" % ", ".join(arr1))
    print("Array 2: [%s]" % ", ".join(arr2))
 
    retval = sameBsts(case["arrayOne"],case["arrayTwo"])
    retstr = "True" if retval else False
    print("Returned: %s (Expecting %s)" % ( retstr, case["expect"]) )
