#!/usr/bin/env python

def debug(my_str):
    print "Debug: ", my_str
class Node(object):
    left_node = None
    right_node = None
    data = None
    def __init__(self,data):
        self.data=data

class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    def insert(self,data):
        if not self.root:
            debug("Inserting Root node %s" % (data))
            self.root=Node(data)
        else:
            debug("Inserting %s data" % str(data) )
            self.insert_node(self.root,data)

    def insert_node(self,current_node,data):

        if data < current_node.data:
            if current_node.left_node:
                debug(" -- %s < %s , left node full. moving to next child" % ( str(data),str(current_node.data)) )
                self.insert_node(current_node.left_node,data)
            else:
                debug(" -- %s < %s , left node empty. adding here" % ( str(data),str(current_node.data)) )
                current_node.left_node=Node(data)

        else:
            if current_node.right_node:
                debug(" -- %s > %s , right node full. moving to next child" % ( str(data),str(current_node.data)) )
                self.insert_node(current_node.right_node,data)

            else:
                debug(" -- %s > %s , right node empty. inserting here" % ( str(data),str(current_node.data)) )
                current_node.right_node=Node(data)

    def get_max(self, current=None):
        if current==None:
            current=self.root
        if current.right_node:
            return self.get_max(current.right_node)
        else:
            return current.data

    def get_min(self, current=None):
        if current==None:
            current=self.root
        if current.left_node:
            return self.get_min(current.left_node)
        else:
            return current.data

    def inorder_traverse(self,current=None):
        if not current:
            print "In order Traversal of tree:"
            current = self.root 

        if current.left_node:
            self.inorder_traverse(current.left_node)

        print "  -- " , current.data

        if current.right_node:
            self.inorder_traverse(current.right_node)

bst=BinarySearchTree()

bst.insert(5)
bst.insert(15)
bst.insert(6)
bst.insert(50)
bst.insert(500)
bst.insert(30)

print "Max:" , bst.get_max()
print "Min:" , bst.get_min()

bst.inorder_traverse()

    
