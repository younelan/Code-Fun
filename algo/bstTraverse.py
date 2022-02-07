
def inOrderTraverse(tree, array):
	if not tree:
    		return array
	inOrderTraverse(tree.left,array)
	array.append(tree.value)
	inOrderTraverse(tree.right,array)
 
	return array
 

def preOrderTraverse(tree, array):
	if not tree:
    		return array
	array.append(tree.value)
	preOrderTraverse(tree.left,array)
	preOrderTraverse(tree.right,array)
 
	return array
 
def postOrderTraverse(tree, array):
	if not tree:
		return array
	postOrderTraverse(tree.left,array)
	postOrderTraverse(tree.right,array)
	array.append(tree.value)
	return array 

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
