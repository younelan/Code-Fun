def generateDocument(characters, document):
	# Write your code here.
	print ("++:",document)
	for char in document:
		pos = characters.find(char)
		print(char, "--", pos)
		if pos==-1:
			#print("%s not found in %s" (char,characters))
			return False
		else:	
			#print("before %s     " % characters),
			characters=characters[:pos]+characters[pos+1:]
			#print(" after %s " % characters)
			
	return True

tests=[
{
  "document": "hello",
  "characters":"a hello world",
  "expect":True
},
{
  "characters": "a",
  "document": "a"
}
]
idx=0
for test in tests:
	idx+=1
	print ("\n%s test %i %s \n" % ("*"*30 , idx, "*"*30))
	characters, document = test["characters"],test["document"]
	print("Character %s / Document %s " % (characters,document)), 
	print("-/ return "),
	print generateDocument(characters,document)