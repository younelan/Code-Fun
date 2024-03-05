#!/usr/bin/env python

SHOW_DEBUG=False
class Node(object):
   left=None
   right=None
   data=None

   def __str__(self):
     return "<Node:"+str(self.data)+">"

   def __init__(self,data):
     self.data=data


#initialize example trees
tree1=Node(4)
tree1.left=Node(6)
tree1.right=Node(10)

tree2=Node(2)
tree2.left=Node(1)
tree2.right=Node(3)

tree3=Node(2)
tree3.left=Node(1)
tree3.left.left=Node(0)
tree3.left.left.left=Node(-5)
tree3.left.left.right=Node(-15)
tree3.left.right=Node(10)
tree3.right=Node(3)

def debug(str_debug):
  if SHOW_DEBUG:
    print str_debug

def validate(current):
  debug(">>Node "+str(current))
  if current.left and current.left.data>current.data:
      debug("Left is invalid")
      return False

  if current.right and current.right.data<current.data:
      debug("Right is invalid")
      return False

  if not current.left:
    debug(" no left children")
    left_valid=True
  else:
    left_valid=validate(current.left)
    debug( "Left Valid:" + str(left_valid))
    
  if not current.right:
    right_valid=True
    debug( "  no right children")
  else:
    right_valid=validate(current.right)
    debug( "  Right Valid:" + str(right_valid))

  if left_valid and right_valid:
    debug("  Both Valid")
    return True
  else:
    return False


print "Tree 1 validation: (2-1-3) " , validate(tree2), "\n\n"
print "Tree 2 validation: (4-6-10)" , validate(tree1), "\n\n"
print "Tree 3 validation: (deeper tree)" , validate(tree3)

