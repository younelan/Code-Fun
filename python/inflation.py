#!/usr/bin/env python 
import requests
from bs4 import BeautifulSoup
import pandas as pd
from collections import OrderedDict

url='http://www.usinflationcalculator.com/inflation/historical-inflation-rates/'
url='http://nicerhost.com/inflation.html'

site_resp = requests.get(url)

html = site_resp.text

soup = BeautifulSoup(html,'html.parser')
#print soup
tbl = soup.find("table",border=1)
#print tbl
tbody = tbl.find('tbody')
rows = tbl.find_all('tr')
header=[]
cells=rows[0].find_all('th')
for cell in cells:
#    print "%6s" % cell.get_text() + "  " ,
    header.append(cell.get_text())
#print ""
data=OrderedDict()

for row in rows[1:]:
     year = row.find("th").get_text()
     #row_dict=OrderedDict({'Year':year})
     row_dict=OrderedDict()
     #print year, 
  
     cells = row.find_all("td")
     for cell_id,cell in enumerate(cells):
       #print "%6s" % cell.get_text() + "  " ,
       try:
         row_dict[header[cell_id+1]]=float(cell.get_text())
       except:
         print "Bad float value: %s" % cell.get_text()
     #print ''
     data[year] = row_dict
     #print row_dict

#print data['2016']['Jan']
df = pd.DataFrame.from_dict(data,orient='index')
df=df.sort_values(['Ave'],ascending=[0])
print df
