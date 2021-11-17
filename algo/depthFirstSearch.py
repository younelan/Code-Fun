class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):

  		array.append(self.name)

  		for child in self.children:
  			child.depthFirstSearch(array)

  		return array


from AlgoHelper import console,testing,graphs

script_name = "depthFirstSearch"
tests = testing.load_tests(script_name)

console.script_header(script_name)
idx=0
for case in tests:
    idx+=1
    console.test_header("test %i" % ( idx))

    start_node,vertices=graphs.load_graph(case["graph"]["nodes"],case["graph"]["startNode"],graph_class=Node)
    array=[]
    vars={}
    retval=start_node.depthFirstSearch(array)
    vars["Returned"]=retval
    vars["Expected"]=case["expect"]

    console.print_variables(vars)

