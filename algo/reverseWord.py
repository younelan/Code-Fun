
def reverseWordsInString(string):
    segments=[]
    if len(string)<2:
        return string
    idx=len(string)-1
    current_segment=""
    while idx>-1:
        current=string[idx]
        if current==" ":
            if current_segment:
                segments.append(current_segment)
                current_segment=""
            segments.append(current)
        else:
            current_segment = current + current_segment
        idx-=1

    if current_segment:
        segments.append(current_segment)
    return "".join(segments)

from AlgoHelper import testing,tree,console

script_name = "reverseWord"
tests = testing.load_tests(script_name)

console.script_header("Reverse Words")
idx=0
for case in tests:
    idx+=1
    console.test_header("Test %s" % idx)

    retval=reverseWordsInString(case["string"])
    case["returned"]=retval

    console.print_variables(case)
    console.debug_out()
