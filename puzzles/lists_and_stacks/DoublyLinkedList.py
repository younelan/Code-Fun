#!/usr/bin/env python

class Node(object):
  def __str__(self):
     return "<Node:"+str(self.data)+">"
  def __init__(self,data):
     self.data=data
     self.next_node=None
     self.prev_node=None

class LinkedList(object):
  def __init__(self):
     self.head=None
     self.size=0

  def peek_head(self):
     #print "PeekHead Prev: " , self.head.prev_node, "Next",self.head.next_node
     try:
       return self.head.data
     except:
       return None

  def peek_tail(self):
     #print "PeekTail Prev: " , self.head.prev_node, "Next",self.head.next_node
     try:
       return self.tail.data
     except:
       return None

  #remove from beginning 
  def shift(self):
    if self.head:
      retval=self.head.data
      self.head=self.head.next_node
      self.head.prev_node=None
      self.size -= 1 
    else:
      retval=None

    if self.size==0:
      self.tail=None
 
    return retval
  def traverse(self):
    current=self.head
    i=0
    while current:
     i += 1 
     try:
       data=current.data
     except:
       pass
     print "Traverse step %i: " %i , "Prev:", current.prev_node, "Next: ",current.next_node , "Val: " , data
     current=current.next_node

  def back_traverse(self):
    current=self.tail
    i=0
    while current:
     i += 1
     try:
       data=current.data
     except:
       pass
     print "Traverse step %i: " %i , "Prev:", current.prev_node, "Next: ",current.next_node , "Val: " , data
     current=current.prev_node

  #insert at beginning
  def unshift(self,data):
     new_node=Node(data)
     if self.head:
       new_node.next_node=self.head
       self.head.prev_node=new_node
       self.head=new_node
       self.size += 1
     else:
       self.head=new_node
       self.tail=new_node
       self.size=1
      
  def pop(self):
     if not self.tail:
        retval=None
     else:
        retval=self.tail.data
        self.tail=self.tail.prev_node
        if self.tail:
          self.tail.next_node=None 

     if self.size:
        self.size -= 1

     return retval

  def push(self,data):
     new_node=Node(data)
     new_node.prev_node=self.tail
     self.tail.next_node=new_node
     self.tail=new_node
     self.size += 1

ll=LinkedList()

ll.unshift(1)

print "Peek: " , ll.peek_head()
print "Peek Tail:", ll.peek_tail()
ll.unshift(2)
ll.unshift(3)
print "Peek: "  ,  ll.peek_head()

print "Peek Tail:" , ll.peek_tail()

#print "shifted",ll.shift()
#print "shifted",ll.shift()

print "-- Forward Traversal of list"
ll.traverse()

print "popped",ll.pop()
#print "Peek Tail:" , ll.peek_tail()

print "popped",ll.pop()
#print "Peek Tail:" , ll.peek_tail()
ll.unshift(2)
ll.unshift(1)
ll.push(4)
print "-- Forward Traversal of list"
ll.traverse()

print "-- Backward Traversal of list: "
ll.back_traverse()
print "Size: " , ll.size 
