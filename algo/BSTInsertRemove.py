# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if isinstance(value,int):
           newnode=BST(value)
        else:
            newnode=value
            value=newnode.value
        if value<self.value:
            if self.left:
            	self.left.insert(value)
            else:
            	self.left=BST(value)

        elif value>self.value:
            if self.right:
            	self.right.insert(value)
            else:
            	self.right=newnode

        return self

    def output(self, depth=0):
        print("%s %s" % ("    "*(depth+1),self.value))
        newdepth=depth+1
        if self.left:
            self.left.output(depth=newdepth)
        if self.right:
            self.right.output(depth=newdepth)
 
    def contains(self, value):
        # Write your code here.
        if value == self.value:
            return True
        elif value <self.value:
            if self.left:
                return self.left.contains(value)
            else:
                return False
        elif value > self.value:
            if self.right:
                return self.right.contains(value)
            else:
                return False

    def remove(self, value,parent=None,isparentleft=0,root=None):
        isrootnoode=False
        if root is None:

            root=self
            isrootnoode=True

        if value == self.value:
            debug("Removing %i" % self.value)
            if isrootnoode:
                debug("which is a root node")
                if self.left and self.right:
                    debug("Both nodes are present")
                    root=self.left
                    root.insert(self.right)
                    return root
                elif self.left:
                    debug("only left is present")
                    root=self.left
                    return root
                else:
                    debug("Only right is present")
                    root=self.right
                    return root



            else:
                if isparentleft:
                    parent.left=None
                else:
                    parent.right=None
                if self.left:
                    root.insert(self.left)
                if self.right:
                    root.insert(self.right)


        elif value <self.value:
            if self.left:
                return self.left.remove(value,parent=self,isparentleft=True,root=root)
            else:
                return False
        elif value > self.value:
            if self.right:
                return self.right.remove(value,parent=self,isparentleft=False,root=root)
            else:
                return False

        return self
    def __repr__(self):
        return "<<Node %i>>" % self.value

from AlgoHelper import testing,tree,console
def debug(str,color=None):
    console.print_color("%s %s" % (color,str),color="OKGREEN")
    console.log(str,color=color)
    
script_name = "bstInsertRemove"
tests = testing.load_tests(script_name)

console.script_header("BST INSERT/REMOVE")
idx=0
for case in tests:
    idx+=1
    console.section_header ("test %i" % (idx))
    root=BST(case['rootValue'])
    tree.print_node(root)
    for method in case['classMethodsToCall']:
        if method["method"]=="insert":
            print("Insert %s " %(method["arguments"][0]))
            root.insert(method["arguments"][0])
        if method["method"]=="remove":
            print("Remove %s " %(method["arguments"][0]))
            newroot=root.remove(method["arguments"][0])
            root=newroot
            print("New Root: "),
            tree.print_node( newroot)
        if method["method"]=="contains":
            print("Contains %s " %(method["arguments"][0]))
            root.contains(method["arguments"][0])
        if method in ["remove"]:
            root.output()
            
        console.debug_out()
