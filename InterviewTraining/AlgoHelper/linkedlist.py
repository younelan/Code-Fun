from __future__ import absolute_import
from .console import get_color_str

class LinkedList(object):
    def __init__(self,value,name=None):
        id_str=None
        if name==None:
            id_str=str(value)
        else:
            id_str=name

        self.id_str=id_str
        self.value=value
        self.next=None
    def __repr__(self):
        next_str = self.next.id_str if self.next else "None" 
        return "<<LinkedList id %s value %i next %s >>" % (self.id_str,self.value,next_str )

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

def load_list(nodes,head_str):
    items={}
    for item in nodes:
        items[item["id"]] = LinkedList(item["value"],name=item["id"])
    for item in nodes:
        if item["next"]:
            items[item["id"]].next = items[item["next"]]

    head = items[ head_str ]
    return head,items

def print_list(head,color=None):
    print_color(get_list_str(head))
