#!/usr/local/bin/python3

print("Dividing 10 by an integer")
while True:
    divider=input('Provide an integer: ')
    if not divider:
       break
    try:
        divider=int(divider)
        result=10/float(divider)
        print(result)
    except ValueError:
        print("Input Error: input must be an integer")
    except ZeroDivisionError as detail:
        print("Input error: your input must not be zero (0) ")