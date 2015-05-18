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
  sys.exit()

contents=[]
wordcounts={}

#check we can read the file
try:
  fh=open(sys.argv[1],'r')
  contents=fh.read().splitlines()
  fh.close()
except:
  print("Error: Unable to open specified file, %s" %sys.argv[1])
  sys.exit()

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
print("Length count:")
for cur_length,count in wordcounts.items():
  print ( "%s : %s" % (cur_length,count) )
