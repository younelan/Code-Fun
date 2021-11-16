from debug import get_color_str
class BinarySearchTree():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def print_node(root):
		leftval = repr(root.left.value) if root.left else "None"
		rightval = repr(root.right.value) if root.right else " None"
		idval = repr(root.value)

		print("  <<Node %s %s %s>> " % (idval,leftval,rightval))
def output_tree(root, depth=0,isleft=0):
    # Write your code here.
    if isleft==0:
    	pos="Root"
    elif isleft==-1:
    	pos="Left"
    elif isleft==1:
    	pos="Right"
    root_color=get_color_str(root.value,color="OKCYAN")
    pos_color=get_color_str(pos,color="OKGREEN")
    print("%s %s (%s)" % ("    "*(depth+1),root_color,pos_color) )
    newdepth=depth+1
    if root.left:
        output_tree(root.left,depth=newdepth,isleft=-1)
    if root.right:
        output_tree(root.right,depth=newdepth,isleft=1)

def build_tree(tree,root):
    nodes={}
    for item in tree:
        print(item)
        nodes[item["id"]]=BinarySearchTree(item["value"])
    for node in tree:
        if node["left"]:
            print(node)

            new_node = nodes[node["left"] ]
            nodes[ node["id"] ].left = new_node
        if node["right"]:
            nodes[node["id"]].right = nodes[node["right"] ]
    root = nodes[ root ]

    return root, nodes