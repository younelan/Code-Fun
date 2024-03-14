import sys

def populateMinBst(array,left,right):
	if (right<left):
		return None
	pivot=(left+right)//2
	#print("pivot %i left %i right %i array "%(pivot,left,right),array)

	node=BST(array[pivot])

	node.left=populateMinBst(array,left,pivot-1)
	node.right=populateMinBst(array,pivot+1,right)
	#tree.print_node(node)
	return node


def minHeightBst(array):
    return populateMinBst(array,0,len(array)-1)


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

from AlgoHelper import console,testing,graphs,tree

script_name = "bstMinheighPopulate"
tests = testing.load_tests(script_name)

console.script_header("BST POPULATE")
idx=0
for case in tests:
	idx+=1
	console.test_header("Test %s" % idx)

	root,nodes = tree.build_tree(case["expect"]["nodes"],case["expect"]["root"])
	console.section_header("Root")
	tree.print_node(root)
	console.section_header("Tree")
	tree.output_tree(root)

	input_array,expect=case["array"],case["expect"]
	vars={}
	vars["Array"]=input_array
	console.print_variables(vars)
	vars={}
	retval=minHeightBst(input_array)

	console.section_header("Tree")
	if retval:
		tree.output_tree(retval)
	else:
		print("Retval is none")

	details=[3]
	console.print_variables(vars)
	if idx in details or not details:
		console.debug_out()
	else:
		console.flush()



