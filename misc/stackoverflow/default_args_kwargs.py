#!/usr/bin/env/python

#http://stackoverflow.com/questions/41233546
#setting default args/kwargs values

def arg_test(*args,**kwargs):
   if not args:
      print "* not args provided set default here"
      print args
   else:
      print "* Positional Args provided"
      print args


   if not kwargs:
      print "* not kwargs provided set default here"
      print kwargs
   else:
      print "* Named arguments provided"
      print kwargs

#no args, no kwargs
print "____ calling with no arguments ___"
arg_test()

#args, no kwargs
print "____ calling with positional arguments ___"
arg_test("a", "b", "c")

#no args, but kwargs
print "____ calling with named arguments ___"
arg_test(a = 1, b = 2, c = 3)
