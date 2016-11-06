#!/usr/bin/env python

class Node(object):
  def __init__(self,data):
     self.data=data
     self.next_node=None

class LinkedList(object):
  def __init__(self):
     self.head=None
     self.size=0

  def peek(self):
     return self.head.data
 

  def shift(self):
    if self.head:
      retval=self.head.data
      self.head=self.head.next_node
      self.size -= 1 
    else:
      retval=None
    
    return retval

  #insert at beginning
  def unshift(self,data):
     new_node=Node(data)
     if self.head:
       new_node.next_node=self.head
       self.head=new_node
       self.size += 1
     else:
       self.head=new_node
       self.size=1
      


ll=LinkedList()

ll.unshift(1)

print "Peek: " , ll.peek()
ll.unshift(2)
print "Peek: "  ,  ll.peek()


print "shifted",ll.shift()
print "shifted",ll.shift()

print "Size: " , ll.size 
