def firstNonRepeatingCharacter(string):
    # Write your code here.
    counts={}
    for idx in range(len(string)):
        ch = string[idx]
        if ch in counts:
            counts[ch] +=1
        else:
            counts[ch]=1
        
    for idx in range(len(string)):
        ch = string[idx]
        if counts[ch]==1:
            return idx
            
    return -1

from AlgoHelper import console,testing	
script_name = "nonRepeat"
tests = testing.load_tests(script_name)

console.script_header("First Non Repeating ")
idx=0
for test in tests:
    idx+=1
    #console.test_header("Test %s" % idx)
    #print(test)
    retval = firstNonRepeatingCharacter(test["string"])

    print ("retval: %3i Expected: %i String: %s" % (retval,test["expected"],test["string"]))