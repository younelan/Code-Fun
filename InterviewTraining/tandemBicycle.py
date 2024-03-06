
def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    total_speed=0
    sortedRed=sorted(redShirtSpeeds)
    sortedBlue=sorted(blueShirtSpeeds)
    for idx in range(len(sortedRed)):
        red_speed=0
        blue_speed=0
        if fastest == True:
            if sortedRed[-1]>sortedBlue[-1]:
                red_speed=sortedRed.pop()
                blue_speed=sortedBlue.pop(0)
            else:
                red_speed=sortedRed.pop(0)
                blue_speed=sortedBlue.pop()
        else:
            red_speed=sortedRed.pop(0)
            blue_speed=sortedBlue.pop(0)
        
        total_speed+=max(red_speed,blue_speed)



    return total_speed

from AlgoHelper import testing,tree,console

script_name = "tandemBicycle"
tests = testing.load_tests(script_name)

console.script_header("Tandem Bicycles")
idx=0
for case in tests:
    idx+=1
    console.test_header("Test %s" % idx)

    retval=tandemBicycle(case["redShirtSpeeds"],case["blueShirtSpeeds"],case["fastest"])
    case["returned"]=retval

    console.print_variables(case)
    console.debug_out()
