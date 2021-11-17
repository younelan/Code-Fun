
def inOrderTraverse(tree, array):
	retval=[]
	if not tree:
		return retval
	array+=inOrderTraverse(tree.left,array)
	array.append(tree.value)
	array+=inOrderTraverse(tree.right,array)
	array=retval
	return retval

def preOrderTraverse(tree, array):
    # Write your code here.
    pass


def postOrderTraverse(tree, array):
    # Write your code here.
    pass


from AlgoHelper import testing,tree,console

script_name = "bstTraverse"
tests = testing.load_tests(script_name)

console.script_header("BST TRAVERSE")
idx=0
for case in tests:
	idx+=1
	console.test_header("Test %s" % idx)

	root,nodes = tree.build_tree(case["tree"]["nodes"],case["tree"]["root"])
	console.section_header("Root")
	tree.print_node(root)
	console.section_header("Tree")
	tree.output_tree(root)

	sections=["inOrderTraverse","postOrderTraverse","preOrderTraverse"]

	test_arrays={}
	for name in sections:
		console.section_header(name)
		test_arrays[name]=[]
		retval = globals()[name](root,test_arrays[name])
		expected_str=case.get(name)
		if name in case["expected"]:
			expected_str = console.array_to_str(case["expected"][name])
			print("Expected: %s" % console.get_color_str(expected_str,"BOLD") )
			
		print("Returned: %s" % console.get_color_str(test_arrays[name]) )
