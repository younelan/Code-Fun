
my_str="hello world"
my_len=len(my_str)

my_list=list(my_str)

for i in range(my_len/2):
  print i , my_len-i
  print "  ",my_list[i],my_list[my_len-i-1]
  (my_list[i],my_list[my_len-i-1])=(my_list[my_len-i-1],my_list[i])

my_str="".join(my_list)

print my_list
