#!/usr/local/bin

import sys
import re

SKIP_ZEROLENGTH=True

#return word length minus non alpha numerical values
def get_len(my_str):
   trimmed_str = re.sub('[^a-zA-Z0-9]+', '', my_str) 
   return len(trimmed_str)

#check we have a file name
argc=len(sys.argv)
if argc != 2:
  print("Word counter")
  print("Error: expecting 1 argument, a filename")

contents=[]
wordcounts={}

#check we can read the file
try:
  fh=open(sys.argv[1],'r')
  contents=fh.read().splitlines()
  fh.close()
except:
  print("Error: Unable to open specified file, %s" %sys.argv[1])

#iterate through all words and count them
for line in contents:
  wordlist=line.split()

  for word in wordlist:
    cur_length=get_len(word)
    
    #handle zero length words
    if cur_length==0 and SKIP_ZEROLENGTH:
      continue

    if cur_length in wordcounts:
      wordcounts[cur_length] += 1
    else:
      wordcounts[cur_length] = 1

#output totals
print("Length count")
max_count=0
max_length=0

for cur_length,cur_count in wordcounts.items():
  print ( str(cur_length).rjust(6),str(cur_count).rjust(5)  )
  if cur_length>max_length:
    max_length=cur_length
  if cur_count>max_count:
    max_count=cur_count

print()

#output histogram
magnitude=10 ** (len(str(max_count))-1)
adjusted_max=((max_count//magnitude)+1)*magnitude
step=adjusted_max//20

if step<1:
  step=1

for y in range(adjusted_max,0,-step):
  cur_val=adjusted_max//y
  if (y%(step*5)) ==0:
    line=str(y).rjust(5) + "_|"
  else:
    line="      |"
  for x in range(1,max_length+2):
    if x not in wordcounts:
      line+="   "
    elif wordcounts[x]>=y:
      line+=" **"
    else:
      line+="   "
  print(line)

print ("    0_|"+"--|"*(max_length+1) )
print ("       ",end="")
for i in range(1,max_length+2):
  print(str(i).rjust(3),end="")
print()
