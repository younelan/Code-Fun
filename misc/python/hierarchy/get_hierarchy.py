#!/usr/bin/python

import json
import urllib
import re

endpoint = "http:/localhost/hierarchy/endpoint.php"


def get_hierarchy(employee_id, level=0):
  url= "%s/employee/%s" % (endpoint,employee_id) 
  fhandle = urllib.urlopen(url)
  content=fhandle.read()
  employee=json.loads(content) 

  if not employee:
    print "-- Error fetching %s" % employee_id

  print "  " * level + "%s - %s" % ( employee[unicode('name')] , employee[unicode('title')] )
  level += 1
 
  if employee['reports']:
    for report in employee['reports']:
      get_hierarchy(report,level)
    

get_hierarchy('A00000001')    
 
