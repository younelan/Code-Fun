# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def __repr__(self):
    	leftval = repr(self.left.value) if self.left else "None"
    	rightval = repr(self.right.value) if self.right else " None"
    	idval = repr(self.value)
    	return "  <<Node %s %s %s>> " % (idval,leftval,rightval)


def branchSums(root,sums=None,cur_total=0):
	print("Visiting %i" % (root.value))
	if sums is None:
		sums=[]
	# Write your code here.
	# traverse=[root]
	# while traverse:

	if root.left:
		branchSums(root.left,sums,cur_total+root.value)
	if root.right:
		branchSums(root.right,sums,cur_total+root.value)
	if root.left is None and root.right is None:
		print("%i is a leaf node %i is running sum" % (root.value,cur_total+root.value))
		sums.append(cur_total+root.value)
	return sums


def output(root, depth=0):
    # Write your code here.
    print("%s %s" % ("    "*(depth+1),root.value))
    newdepth=depth+1
    if root.left:
        output(root.left,depth=newdepth)
    if root.right:
        output(root.right,depth=newdepth)
def insert(root, value):
    # Write your code here.
    # Do not edit the return statement of this method.
    newnode=BinaryTree(value)
    if value<self.value:
        if self.left:
        	insert(root.left,value)
        else:
        	self.left=newnode

    elif value>self.value:
        if self.right:
        	insert(root.right,value)
        else:
        	self.right=newnode

    return self

tests=[
 {
  "tree": {
    "nodes": [
      {"id": "1", "left": "2", "right": "3", "value": 1},
      {"id": "2", "left": None, "right": None, "value": 2},
      {"id": "3", "left": None, "right": None, "value": 3}
    ],
    "root": "1"
  },
  "expect":[3,4]
},

{
  "tree": {
    "nodes": [
      {"id": "1", "left": "2", "right": None, "value": 1},
      {"id": "2", "left": None, "right": None, "value": 2}
    ],
    "root": "1"
  },
  "expect":[3]

},
{
  "tree": {
    "nodes": [
      {"id": "1", "left": "2", "right": "3", "value": 1},
      {"id": "2", "left": "4", "right": "5", "value": 2},
      {"id": "3", "left": None, "right": None, "value": 3},
      {"id": "4", "left": None, "right": None, "value": 4},
      {"id": "5", "left": None, "right": None, "value": 5}
    ],
    "root": "1"
  },
  "expect":[7, 8, 4]
},
]
idx=0
for case in tests:
	idx+=1
	print ("\n%s test %i *********" % ("*"*20 , idx))

	nodes={}
	for node in case["tree"]["nodes"]:
		idval=int(node["id"])
		if node["left"]:
			leftval=int(node["left"]) 
		else:
			leftval=None
		if node["right"]:
			rightval=int(node["right"]) 
		else:
			rightval = None

		if idval not in nodes:
			nodes[idval]=BinaryTree(idval)
		if leftval is not None:
			if leftval not in nodes:
				nodes[leftval]=BinaryTree(leftval)
			nodes[idval].left=nodes[leftval]
		if rightval is not None:
			if rightval not in nodes:

				nodes[rightval]=BinaryTree(rightval)
			nodes[idval].right=nodes[rightval]

	root = nodes[int(case["tree"]["root"])]
	print(" -- Root --")
	print(root)
	print(" -- Tree --")
	output(root)
	for node in nodes:
		print(nodes[node])
	print(" -- Sum --")
	print(branchSums(root))
	print(" -- Expect --")
	print(case["expect"])






