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
        # Write your code here.
        # Do not edit the return statement of this method.
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
        # Write your code here.
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
            print("Removing",self.value)
            if isrootnoode:
                print("which is a root node")
                if self.left and self.right:
                    print("Both nodes are present")
                    root=self.left
                    root.insert(self.right)
                    return root
                elif self.left:
                    print("only left is present")
                    root=self.left
                    return root
                else:
                    print("Only right is present")
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

# root=BST(5)
# root.insert(7)
# print(root.right)
# root.insert(8)
# root.insert(18)
# root.insert(4)
# print(root.contains(7))
# print(root.contains(11))

tests=[
{
  "classMethodsToCall": [
    {
      "arguments": [5],
      "method": "insert"
    },
    {
      "arguments": [15],
      "method": "insert"
    },
    {
      "arguments": [2],
      "method": "insert"
    },
    {
      "arguments": [5],
      "method": "insert"
    },
    {
      "arguments": [13],
      "method": "insert"
    },
    {
      "arguments": [22],
      "method": "insert"
    },
    {
      "arguments": [1],
      "method": "insert"
    },
    {
      "arguments": [14],
      "method": "insert"
    },
    {
      "arguments": [12],
      "method": "insert"
    },
    {
      "arguments": [10],
      "method": "remove"
    },
    {
      "arguments": [15],
      "method": "contains"
    }
  ],
  "rootValue": 10
}
]
idx=0
for case in tests:
    idx+=1
    print ("%s test %i *********" % ("*"*20 , idx))
    root=BST(case['rootValue'])
    print("Root %s" %root)
    for method in case['classMethodsToCall']:
        if method["method"]=="insert":
            print("Insert %s " %(method["arguments"][0]))
            root.insert(method["arguments"][0])
        if method["method"]=="remove":
            print("Remove %s " %(method["arguments"][0]))
            newroot=root.remove(method["arguments"][0])
            root=newroot
            print("New Root", newroot)
        if method["method"]=="contains":
            print("Contains %s " %(method["arguments"][0]))
            root.contains(method["arguments"][0])

        root.output()
