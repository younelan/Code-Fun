#!/usr/local/bin/python3

import sys

def capitalize(my_str):
  return my_str.capitalize()

def title(my_str):
  return my_str.title()

def upper(my_str):
  return my_str.upper()

def lower(my_str):
  return my_str.lower()

def exit(my_str):
  print("Goodbye for now!")
  sys.exit()

switch = {
  "capitalize":capitalize,
  "title":title,
  "upper":upper,
  "lower":lower,
  "exit":exit
} 

while True:
  cur_func=input("Enter a function name (capitalize, title, upper, lower, or exit: ")
  cur_str=input("Enter a string: ")
  option = switch.get(cur_func, None)
  if option:
    print(option(cur_str))
  else:
    print("please enter a valid option")

