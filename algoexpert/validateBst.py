import sys
# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
	def getrepr(self):
		leftval = repr(self.left.value) if self.left else "None"
		rightval = repr(self.right.value) if self.right else " None"
		idval = repr(self.value)
		print("hello")
		sys.exit()
		return "  <<Node %s %s %s>> " % (idval,leftval,rightval)

 
def validateBst(tree,minval=-float("inf"),maxval=float("inf")):
	if not tree:
		return True

	if tree.value<minval or tree.value>=maxval:
		return False

	leftvalid=validateBst(tree.left,minval,tree.value)
	rightvalid=validateBst(tree.right,tree.value,maxval)

	if leftvalid and rightvalid:
		return True
	else:
		return False



def oldvalidateBst(tree,parent=None):
    # Write your code here.
    if parent:
    	leftval=str(tree.left.value) if tree.left else "None"
    	rightval=str(tree.right.value) if tree.right else "None"
    	print("<<Current Node %i left %s right %s parent %i>>" % (tree.value,leftval,rightval,parent.value))
    else:
    	print("No parent")
	if tree.left:
		if tree.value<tree.left.value:
			print("Invalid left tree %i > %i failed comparison" % (tree.value,tree.left.value))
			return False
		# if parent and tree.left.value>parent.value:
		# 	print("Invalid left tree Parent %i > %i failed comparison" % (tree.left.value,parent.value))
		# 	return False
		leftvalid=validateBst(tree.left,parent=tree)
	else:
		leftvalid=True
	if tree.right:
		if tree.value>tree.right.value:
			print("Invalid right tree %i <= %i failed comparison" % (tree.value,tree.right.value))
			return False
		# if parent and tree.right.value<=parent.value:
		# 	print("Invalid right tree Parent %i > %i failed comparison" % (tree.right.value,parent.value))
		# 	return False
		rightvalid=validateBst(tree.right,parent=tree)
	else:
		rightvalid=True
	if leftvalid and rightvalid:
		return True
	else:
		return False
		




def printnode(root):
		leftval = repr(root.left.value) if root.left else "None"
		rightval = repr(root.right.value) if root.right else " None"
		idval = repr(root.value)

		print("  <<Node %s %s %s>> " % (idval,leftval,rightval))
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
      {"id": "10", "left": "5", "right": "15", "value": 10},
      {"id": "15", "left": "13", "right": "22", "value": 15},
      {"id": "22", "left": None, "right": None, "value": 22},
      {"id": "13", "left": None, "right": "14", "value": 13},
      {"id": "14", "left": None, "right": None, "value": 14},
      {"id": "5", "left": "2", "right": "5-2", "value": 5},
      {"id": "5-2", "left": None, "right": None, "value": 5},
      {"id": "2", "left": "1", "right": None, "value": 2},
      {"id": "1", "left": None, "right": None, "value": 1}
    ],
    "root": "10"
  },
  "expect":"True"
},
{

  "tree": {
    "nodes": [
      {"id": "10", "left": "5", "right": "15", "value": 10},
      {"id": "15", "left": None, "right": "22", "value": 15},
      {"id": "22", "left": None, "right": "500", "value": 22},
      {"id": "500", "left": "50", "right": "1500", "value": 500},
      {"id": "1500", "left": None, "right": "10000", "value": 1500},
      {"id": "10000", "left": "2200", "right": "9999", "value": 10000},
      {"id": "9999", "left": None, "right": None, "value": 9999},
      {"id": "2200", "left": None, "right": None, "value": 2200},
      {"id": "50", "left": None, "right": "200", "value": 50},
      {"id": "200", "left": None, "right": None, "value": 200},
      {"id": "5", "left": "2", "right": "5-2", "value": 5},
      {"id": "5-2", "left": None, "right": None, "value": 5},
      {"id": "2", "left": "1", "right": None, "value": 2},
      {"id": "1", "left": None, "right": None, "value": 1}
    ],
    "root": "10"
  },
  "expect":"False",
},
{
  "expect":"False",
  "tree": {
    "nodes": [
      {"id": "100", "left": "5", "right": "502", "value": 100},
      {"id": "502", "left": "204", "right": "55000", "value": 502},
      {"id": "55000", "left": None, "right": None, "value": 55000},
      {"id": "204", "left": "203", "right": "205", "value": 204},
      {"id": "205", "left": "300", "right": "207", "value": 205},
      {"id": "207", "left": "206", "right": "208", "value": 207},
      {"id": "208", "left": None, "right": None, "value": 208},
      {"id": "206", "left": None, "right": None, "value": 206},
      {"id": "300", "left": None, "right": None, "value": 300},
      {"id": "203", "left": None, "right": None, "value": 203},
      {"id": "5", "left": "2", "right": "15", "value": 5},
      {"id": "15", "left": "5-2", "right": "22", "value": 15},
      {"id": "22", "left": None, "right": None, "value": 22},
      {"id": "5-2", "left": None, "right": None, "value": 5},
      {"id": "2", "left": "1", "right": "3", "value": 2},
      {"id": "3", "left": None, "right": None, "value": 3},
      {"id": "1", "left": None, "right": "1-2", "value": 1},
      {"id": "1-2", "left": None, "right": "1-3", "value": 1},
      {"id": "1-3", "left": None, "right": "1-4", "value": 1},
      {"id": "1-4", "left": None, "right": "1-5", "value": 1},
      {"id": "1-5", "left": None, "right": None, "value": 1}
    ],
    "root": "100"
  },
},

{
  "tree": {
    "nodes": [
      {"id": "10", "left": "5", "right": "15", "value": 10},
      {"id": "15", "left": None, "right": None, "value": 15},
      {"id": "5", "left": None, "right": "10-2", "value": 5},
      {"id": "10-2", "left": None, "right": None, "value": 10}
    ],
    "root": "10"
  },
  "expect":"True"
},
{
  "tree": {
    "nodes": [
      {"id": "10", "left": "5", "right": "15", "value": 10},
      {"id": "15", "left": None, "right": "22", "value": 15},
      {"id": "22", "left": None, "right": None, "value": 22},
      {"id": "5", "left": "2", "right": "5-2", "value": 5},
      {"id": "5-2", "left": None, "right": "11", "value": 5},
      {"id": "11", "left": None, "right": None, "value": 11},
      {"id": "2", "left": "1", "right": None, "value": 2},
      {"id": "1", "left": None, "right": None, "value": 1}
    ],
    "root": "10"
  },
  "expect":"False"
}
]
print("""


BST VALID




""")
idx=0
for case in tests:
	idx+=1
	print ("\n%s test %i *********" % ("*"*20 , idx))

	nodes={}
	for node in case["tree"]["nodes"]:
		nodes[node["id"]]=BST(node["value"])
	for node in case["tree"]["nodes"]:
		if node["left"]:
			nodes[ node["id"] ].left = nodes[node["left"] ]
		if node["right"]:
			nodes[node["id"]].right = nodes[node["right"] ]

	# for node in case["tree"]["nodes"]:
	# 	idval=int(node["id"])
	# 	if node["left"]:
	# 		leftval=int(node["left"]) 
	# 	else:
	# 		leftval=None
	# 	if node["right"]:
	# 		rightval=int(node["right"]) 
	# 	else:
	# 		rightval = None

	# 	if idval not in nodes:
	# 		nodes[idval]=BST(idval)
	# 	if leftval is not None:
	# 		if leftval not in nodes:
	# 			nodes[leftval]=BST(leftval)
	# 		nodes[idval].left=nodes[leftval]
	# 	if rightval is not None:
	# 		if rightval not in nodes:

	# 			nodes[rightval]=BST(rightval)
	# 		nodes[idval].right=nodes[rightval]

	root = nodes[ case["tree"]["root"] ]
	print(" -- Root --")
	printnode(root)
	print(" -- Tree --")
	output(root)
	# for node in nodes:
	# 	print(nodes[node])
	# print(" -- Valid --")
	print(validateBst(root))
	print(" -- Expect --")
	print(case["expect"])






