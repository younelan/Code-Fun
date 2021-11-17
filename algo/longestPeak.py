def longestPeak(array):
    UP,DOWN=1,1
    has_up=False
    has_down=False
    going=UP
    up_count=0
    down_count=0
    if not array:
      return 0
    prev=array[0]
    retval=0
    for idx in range(1,len(array)-1):
        current=array[idx]
        #no equal elements
        if current == prev:
            return 0
        #no up and going down
        if has_up==False and current<prev:
            return 0

        if going==UP:
            if current>prev:
                has_up=True
                up_count+=1
            elif current<prev:
                has_down=True
                down_count+=1
        if going==DOWN:
            if current<prev:
                down_count+=1  
            else:
                return down_count+up_count       

    return down_count+up_count


from AlgoHelper import console,testing,graphs

script_name = "longestPeak"
tests = testing.load_tests(script_name)

console.script_header(script_name)
idx=0
for case in tests:
    idx+=1
    console.test_header("test %i" % ( idx))

    input_array,expect=case["array"],case["expect"]
    vars={}
    vars["Array"]=input_array
    console.print_variables(vars)
    vars={}
    retval=longestPeak(input_array)
    vars["Returned"]=retval
    
    color="OKGREEN" if retval==expect else "FAIL"
    vars["Expected"]=console.get_color_str(case["expect"],color)

    console.print_variables(vars)

