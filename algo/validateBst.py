debug_tests = []
# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

 
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


from AlgoHelper import console,tree,testing,ROOT_DIR

script_name = "validateBst"
tests = testing.load_tests(script_name)

console.script_header("BST TRAVERSE")
idx=0
for case in tests:
    idx+=1
    console.test_header("Test %s" % idx)

    root,nodes = tree.build_tree(case["tree"]["nodes"],case["tree"]["root"])

    if idx in debug_tests or 1:
        tree.output_tree(root)
    
    vars={}
    retval=validateBst(root)
    print("")

    if "expect" in case:
        color = "OKGREEN" if case["expect"]==retval else "FAIL"
        vars["Returned"]=console.get_color_str(retval,color)
        vars["Expect"]=case["expect"]
    else:
        vars["Returned"]=retval

    console.print_variables (vars)




