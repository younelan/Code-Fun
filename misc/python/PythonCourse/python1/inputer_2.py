#!/usr/local/bin/python3

fname='inputter.txt'
logFile = open(fname,'a')
logFile.close()

oldText=''


while True:
  inStr=input('Sentence: ')
  if not inStr:
    break
    
  logfile = open(fname,'a')
  logfile.write(inStr)
  logfile.close()
  
  with open(fname, "rt") as in_file:
    oldText = in_file.read()
    in_file.close()
    
  print(oldText)


