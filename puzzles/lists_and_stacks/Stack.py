#!/usr/bin/env/python

class Stack(object):

  def __init__(self):
    self.stack=[]

  def push(self, data):
    self.stack.append(data)

  def pop(self):
    return self.stack.pop()

  def peek(self):
    return self.stack[-1]


st=Stack()

st.push(10)
st.push(20)
st.push(30)

print st.stack

print st.pop()
print st.pop() 

print st.peek()
