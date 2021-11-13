class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
		# Write your code here.
		#array.append(self.name)
		array.append(self.name)

		for child in self.children:
			child.depthFirstSearch(array)

		return array


tests = [

    {
      "graph": {
        "nodes": [
          {"children": ["B", "C", "D"], "id": "A", "value": "A"},
          {"children": ["E", "F"], "id": "B", "value": "B"},
          {"children": [], "id": "C", "value": "C"},
          {"children": ["G", "H"], "id": "D", "value": "D"},
          {"children": [], "id": "E", "value": "E"},
          {"children": ["I", "J"], "id": "F", "value": "F"},
          {"children": ["K"], "id": "G", "value": "G"},
          {"children": [], "id": "H", "value": "H"},
          {"children": [], "id": "I", "value": "I"},
          {"children": [], "id": "J", "value": "J"},
          {"children": [], "id": "K", "value": "K"}
        ],
        "startNode": "A"
      },
    "expect":["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]
    },

    {
      "graph": {
        "nodes": [
          {"children": ["B", "C"], "id": "A", "value": "A"},
          {"children": ["D"], "id": "B", "value": "B"},
          {"children": [], "id": "C", "value": "C"},
          {"children": [], "id": "D", "value": "D"}
        ],
        "startNode": "A"
      },
      "expect": ["A", "B", "D", "C"]
    }
]
idx=0
for case in tests:
    idx+=1
    print ("\n%s test %i *********" % ("*"*20 , idx))

    nodes={}
    for node in case["graph"]["nodes"]:
        nodes[node["id"]]=Node(node["value"])
        print("Created node %s" % node["id"])
    for node in case["graph"]["nodes"]:
        for child in node["children"]:
            nodes[ node["id"] ].children.append(nodes[child])
            print("Added child %s to %s " % (child,node["id"]))
    print("-- BST node list")
    startNode=nodes[case["graph"]["startNode"]]
    array=[]
    print(startNode.depthFirstSearch(array))
    print("-- Expected ")
    print(case["expect"])
