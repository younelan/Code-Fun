#!/usr/bin/env/python
#Ask the user to input a value that will be the range
x = int(input("Please enter a number and I will generate the primes in that range."))
s = 0
oddNumbers = [] # create a list that will store the odd numbers that are candidates to be prime
PrimeNumbers = [] # create a list that will store the primes
NotPrimes = [] # create list for non primes 
for i in range(2, x + 1): # tests to see    
    if ( i % 2 ):  # if the numbers are odd       
        oddNumbers.append(i)# store them in list
        s = s + 1 #counter to see how many odds are there

#1st change iterate to s (last number could be prime)
for e in range( 0, s):
    #added is_prime value that defaults to true
    is_prime=True
    #using oddNumbers/2, slight optimization to perform less calculations
    for counter in range (2 , oddNumbers[e]//2):
        if ( oddNumbers[e] % counter == 0):
            NotPrimes.append(oddNumbers[e])
            is_prime=False
            #adding a break here, if we found one divisor, it is not prime
            # no need to keep computing, move to next number
            break
    #a prime number is only added if all other combinations failed
    #that was the biggest issue with your code
    if is_prime:
       PrimeNumbers.append(oddNumbers[e])
    
print (PrimeNumbers)
print (NotPrimes)
