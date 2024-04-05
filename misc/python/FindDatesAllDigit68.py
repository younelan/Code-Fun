#!/usr/bin/env python
#Find dates where all digits add to 68,

start=1914
end=2022
count=0
target=68

days=[31,28,31,30,31,30,31,31,30,31,30,31]
for y in range(start,end):
	for m in range(12):
		cur_days=days[m]
		for d in range(cur_days):
		  hundreds=(y+1)//100
		  units=(y+1)%100
		  day=d+1
		  month=m+1
		  year=y+1
		  total= hundreds+units+day+month
		  if total == target:
		    count+=1
		    print("%i/%i/%i " % (month,day,year)),
		    print(": %i + %i + %i + %i + %i = %i" % (month,day,year,hundreds,units,total) )

print("Total matches: %i" %count)
