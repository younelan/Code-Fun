#!/usr/bin/env/python

class Queue(object):

  def __init__(self):
    self.queue=[]

  def enqueue(self, data):
    self.queue.insert(0,data)

  def dequeue(self):
    return self.queue.pop()

  def peek(self):
    return self.queue[-1]


Q=Queue()

Q.enqueue(10)
Q.enqueue(20)
Q.enqueue(30)

print Q.queue

print Q.dequeue()
print Q.dequeue() 

print Q.peek()
