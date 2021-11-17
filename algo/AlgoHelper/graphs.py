class Node(object):
    def __init__(self,value,name=None):
        self.value=value
        if not id:
            self.id=str(value)
        self.children = []
    def __repr__(self):
        child_arr=  []
        for child in self.children:
            if child:
                child_arr.append(child.id)
        child_str=",".join(child_arr)
        return "<<GraphNode id: %s val: %s children: %s" % (self.id,self.value,self.child_str)

def load_graph(vertices,start_at,graph_class=Node,debug=False):
    nodes={}
    for node in vertices:
        nodes[node["id"]]=graph_class(node["value"])
        nodes[node["id"]].id=node["id"]
        if debug:
            print("Created node %s" % node["id"])
    for node in vertices:
        for child in node["children"]:
            nodes[ node["id"] ].children.append(nodes[child])
            if debug:
                print("Added child %s to %s " % (child,node["id"]))
    if debug:
        print("-- BST node list")
    start_node=nodes[start_at]

    return  start_node,nodes