#!/usr/bin/python

for i in range(1,101):
   if i%4 == 0 and i%6==0:
     print "Fizz Buzz."
   elif i%4 == 0:
     print "Fizz"
   elif i%6 == 0:
     print "Buzz"
   else:
     print i
