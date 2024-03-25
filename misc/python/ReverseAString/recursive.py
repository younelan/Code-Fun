


def rev_string(my_str):
    if len(my_str)>1:
        return rev_string(my_str[int(len(my_str)/2):])+rev_string(my_str[:int(len(my_str)/2)]) 
    else:
        return my_str


print rev_string("hello world")
    
