#!/usr/local/bin/python3

from random import randint

randNum=randint(1,99)

while True:
  inStr=int(input('Guess a  number: '))
  if inStr==randNum:
    print("You guessed it!")
    break
  elif inStr>randNum:
    print("too high")
  else:
    print("too low")