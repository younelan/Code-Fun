
# Given a string containing only digits, 
# generate all permutations of that string

def isValidPart(string): 
    if int(string) > 255:
        return False 
    if str(int(string)) != string:
        return False
    return True
def validIPAddresses(string): 
    ipAddressesFound = [] 
    parts=[""]*4
    for p1 in range(3):
        for p2 in range(3):
            for p3 in range(3):
                if p1+p2+p3+3 >= len(string):
                    continue
                parts[0]=string[:p1+1]
                parts[1]=string[p1+1:p1+p2+2]
                parts[2]=string[p1+p2+2:p1+p2+p3+3]
                parts[3]=string[p1+p2+p3+3:]
                if isValidPart(parts[0]) and isValidPart(parts[1]) and isValidPart(parts[2]) and isValidPart(parts[3]):
                    ipAddressesFound.append(".".join(parts))

    return ipAddressesFound



from AlgoHelper import testing,tree,console

script_name = "generateIPAddresses"
tests = testing.load_tests(script_name)

console.script_header("generate valid IP addresses")
idx=0
for case in tests:
    idx+=1
    console.test_header("Test %s" % idx)

    retval=validIPAddresses(case["string"])
    case["returned"]=retval

    console.print_variables(case)
    console.debug_out()
