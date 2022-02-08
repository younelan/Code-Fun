from os import curdir
from AlgoHelper.linkedlist import print_list
def longestPeak(array):
    max_peak=0
    if len(array)<3:
        return 0
    prev = array[0]

    idx=0
    while idx < len(array) - 2:
        idx+=1
        #current = array[idx]
        is_peak = array[idx-1]<array[idx] and array[idx+1]<array[idx]
        if is_peak:
            print("Peak at %i<%i<%i"% (array[idx-1],array[idx],array[idx+1]))
            start=idx
            while start>0 and array[start-1]<array[start]:
                start-=1
            end=idx
            while end<len(array)-1 and array[end+1]<array[end]:
                end+=1
            
            print("Start %i End %i Max Peak %i Current %i " % (start,end,max_peak,end-start ))
            if end-start>max_peak:
                max_peak=end-start+1
            idx = end
    return max_peak            

def oldlongestPeak(array):
    FLAT,UP,DOWN = 0,1,-1
    direction=FLAT
    new_dir=FLAT
    max_peak=0
    p_start = 0
    p_end = 0
    if len(array)<2:
        console.log("too small")
        return 0
    prev = array[0]
    for idx in range(1,len(array)):
        current = array[idx]
        
        if direction==FLAT:
            if prev<current:
                direction=UP
                #p_start = idx - 1
            else:
                wp_start=idx
            #     prev=current
            #     continue
        elif direction == UP:
            if current<prev:
                max_peak=idx-p_start
                direction=DOWN 
            elif current == prev:
                direction=FLAT
        elif direction == DOWN:
            if current==prev:
                direction=FLAT
            elif current>prev:
                #console.log("cur_peak %i = idx %i -p_start %i"%(idx-p_start,idx,p_start))
                cur_peak = idx-p_start
                if cur_peak>max_peak:
                    max_peak = cur_peak                
                p_start=current
                direction=UP
            else:
                cur_peak = idx - p_start
                if cur_peak>max_peak:
                    max_peak=cur_peak
        console.log("idx %2i direction %2i prev %i current %i p_start %i p_end %i max_peak %i" % (idx,direction,prev,current,p_start,p_end,max_peak))
        prev = current
        
    return max_peak +1 if max_peak>2 else 0
from AlgoHelper import console,testing,graphs

script_name = "longestPeak"
tests = testing.load_tests(script_name)

details=[6]
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
    if idx in details:
        console.debug_out()
    else:
        console.flush()

