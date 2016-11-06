#!/usr/local/bin/python3

inStr=input('Message: ')

outStr=''

for curChr in inStr:
   outStr+=chr(ord(curChr)+1)

print(outStr[::-1])