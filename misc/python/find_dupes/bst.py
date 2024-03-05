
lst=[1,2,3,4,5,6,9,4]

viewed=[]

class Node(object):
  left = None
  right = None
  data = None

  def __str__(self):
    return str(self.data)
  def __init__(self,data):
    self.data=data

class BSTtree(object):
    head=None
    def add(self,data,node=None):

        if not self.head:
            self.head=Node(data)
            return False

        if not node: 
            node=self.head

        if node and data==node.data:
            print "Dupe found",data,node.data
            return True
        elif data<node.data:
            if not node.left:
                node.left=Node(data)
            else:
                self.add(data,node=node.left)
        else:
            if not node.right:
                node.right=Node(data)
            else:
                self.add(data,node=node.right)

            
t=BSTtree()

for i in lst:
  retval=t.add(i)
  if retval:
    print i, " is a dupe"
