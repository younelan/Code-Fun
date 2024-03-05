mySTR=input("Please enter an upper case string ending with a period: ")

checks=0

if(mySTR.isupper()):
  print("Pass: String is uppercase")
  checks=checks+1
else:
  print("Fail: String is not all uppercase")
  
if(mySTR.endswith(".")):
  print("Pass: String ends with a period")
  checks=checks+1
else:
  print("Fail: String does not end with a period")

if checks>1:
  print('Success: Input meets both requirements')
else:
  print('Failure: At least one of the tests failed')
