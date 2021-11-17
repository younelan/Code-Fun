from debug import get_color_str

class LinkedList(object):
    def __init__(self,value):
        self.value=value
        self.next=None

def get_list_str(head):
    ptr=head
    vals = []

    while ptr.next:
        vals.append(str(ptr.value))
        ptr = ptr.next
    if ptr:
        vals.append(str(ptr.value))

    output= " -> ".join(vals) 
    return output


def print_list(head,color=None):
    print_color(get_list_str(head))
