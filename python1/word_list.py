#!/usr/local/bin/python3

inStr=input('Please enter a string: ')

inWords=inStr.split()

ucaseWords=[]
lcaseWords=[]

for curWord in inWords:
    if any(l.isupper() for l  in curWord):
        ucaseWords.append(curWord)
    else:
        lcaseWords.append(curWord)

output = "\n".join(ucaseWords)
output += "\n".join(lcaseWords)

print (output)