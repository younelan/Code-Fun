#!/usr/bin/env/python

#stack overflow answer:
#find out which letters are different, taking account length of shortest string

list1= "ABCDEFABCDEF"
list2= "AZBYCXDWEVFABCDEF"

minlen=min(len(list1),len(list2))

identicals=[]
differents=[]

for i in range(minlen):
  if list1[i]==list2[i]:
    identicals.append(list1[i])
  else:
    differents.append(list1[i])

print "Differents: ", differents
print "Identicals: ", identicals

