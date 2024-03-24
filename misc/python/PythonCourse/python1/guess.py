#!/usr/local/bin/python3

import random

secret=random.randint(1,20)
correct=False
attempt=0

while attempt<5:
   try:
     guess=int(input("Please guess a number: "))
   except:
     print("Please enter a number")
   if guess>secret:
   	print("Please guess lower")
   elif guess<secret:
   	print("Please guess higher")
   else:
   	correct=True
   	print("Correct! Well done, you guessed the correct number")
   	break
   	
   attempt=attempt+1
   
if not correct:
	print("Unfortunately you were not able to guess in 5 tries, you lost")