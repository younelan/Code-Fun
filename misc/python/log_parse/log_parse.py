#!/usr/bin/python

import collections

fname = "messages"
message_counts = collections.OrderedDict()

with open(fname) as fhandle:
   #parse messages
   for line in fhandle.readlines():
      pieces = line.split()
      if pieces and len(pieces)>1:
        f_date = "%s %s" % (pieces[0],pieces[1])
        f_time = ':'.join(pieces[2].split(':')[0:2] )
        f_host = pieces[3]
        f_message = pieces [4:]
        if f_date not in message_counts:
           message_counts[f_date]=collections.OrderedDict()
        if message_counts and f_time in message_counts[f_date]:
           message_counts[f_date][f_time] += 1
        else:
           message_counts[f_date][f_time] = 1
   #output   
   for date_str,hourly_counts in message_counts.items():
      for key,value in hourly_counts.items():
          print " %s :  %s : %s " % (date_str,key,value)

