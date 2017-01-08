#!/usr/local/bin/python3

def my_func(a,b='b was not entered',c='c was not entered'):
  print (a)
  print (b)
  print (c)

my_func('test')
my_func('test',b='test')
my_func(a='test',b='test',c='test')

print(my_func)