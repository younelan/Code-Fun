#number = input("Please enter range: ")+1

def collatz(a):
    if a%2==0:
        return a/2
    else:
        return (3*a)+1


with open("in.txt") as fp:
  numbers = fp.readlines() 

for num_string in numbers:
    try:
      x=int(num_string)
    except:
      print "invalid number %s" %num_string
      continue
    n=x
    count=0
    while n>=1:
        print "%s " % (n),

        if n==1:
            n=0

        n=collatz(n)
        count+=1
    print "\n\n%s: %s\n\n" % (x, count)
    x+=1
