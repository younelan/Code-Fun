#!/usr/bin/python2.7

import csv

with open('input.csv','rb') as csvfile:
  my_reader = csv.reader(csvfile,delimiter=',')
  for row in my_reader:
   row_length=len(row)
   if row_length:
    #print row[0]
    columns = row[0].split('+')
    num_columns = len(columns)
    for i in range(num_columns):
    	print "%s,%s" % (columns[i],row[i+1])
    #print columns



