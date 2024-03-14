def minimumCharactersForWords(words):
    retfrequencies={}
    for word in words:
        frequencies={}
        for letter in word:
            frequencies[letter]=frequencies.get(letter,0)+1

            if frequencies[letter]>retfrequencies.get(letter,0):
                retfrequencies[letter]=frequencies[letter]
        print(frequencies)
    retval=[]
    #print (retfrequencies)
    for letter,count in retfrequencies.items():
        retval = retval + [letter] *count
    return retval

from AlgoHelper import testing,tree,console

script_name = "minCharsForWords"
tests = testing.load_tests(script_name)

console.script_header("Min Characters for wordss")
idx=0
for case in tests:
    idx+=1
    console.test_header("Test %s" % idx)

    retval=minimumCharactersForWords(case["words"])
    case["returned"]=retval

    console.print_variables(case)
    console.debug_out()


