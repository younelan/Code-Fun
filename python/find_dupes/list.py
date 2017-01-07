
lst=[1,2,3,4,5,6,9,4]

viewed=[]

for i in lst:
  if i in viewed:
    print i, " is a dupe"
    break
  else:
    viewed.append(i)
  print i
