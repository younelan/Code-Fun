class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
	cur_ptr = linkedList
	next_ptr = None
	while cur_ptr and cur_ptr.next:
		if cur_ptr.next.value == cur_ptr.value:
			next_ptr = cur_ptr.next.next
			while next_ptr and next_ptr.value == cur_ptr.value:
				next_ptr = next_ptr.next
			cur_ptr.next = next_ptr
		cur_ptr=cur_ptr.next
	return linkedList

def print_list(head):
	ptr=head
	vals = []

	while ptr.next:
		vals.append(str(ptr.value))
		ptr = ptr.next
	if ptr:
		vals.append(str(ptr.value))

	print( " -> ".join(vals) )

tests = [

	{
	  "linkedList": {
		  "head": "1",
		  "nodes": [
		    {"id": "1", "next": "9", "value": 1},
		    {"id": "9", "next": "11", "value": 9},
		    {"id": "11", "next": "15", "value": 11},
		    {"id": "15", "next": "16", "value": 15},
		    {"id": "16", "next": "17", "value": 16},
		    {"id": "17", "next": None, "value": 17}
		  ]
		}
	},
	{
	  "linkedList": {
	    "head": "1",
	    "nodes": [
	      {"id": "1", "next": "1-2", "value": 1},
	      {"id": "1-2", "next": "1-3", "value": 1},
	      {"id": "1-3", "next": "2", "value": 1},
	      {"id": "2", "next": "3", "value": 3},
	      {"id": "3", "next": "3-2", "value": 4},
	      {"id": "3-2", "next": "3-3", "value": 4},
	      {"id": "3-3", "next": "4", "value": 4},
	      {"id": "4", "next": "5", "value": 5},
	      {"id": "5", "next": "5-2", "value": 6},
	      {"id": "5-2", "next": None, "value": 6}
	    ]
	  }
	},
	{
	  "linkedList": {
	    "head": "1",
	    "nodes": [
	      {"id": "1", "next": "1-2", "value": 1},
	      {"id": "1-2", "next": "1-3", "value": 1},
	      {"id": "1-3", "next": "1-4", "value": 1},
	      {"id": "1-4", "next": "1-5", "value": 1},
	      {"id": "1-5", "next": "4", "value": 1},
	      {"id": "4", "next": "4-2", "value": 4},
	      {"id": "4-2", "next": "5", "value": 4},
	      {"id": "5", "next": "6", "value": 5},
	      {"id": "6", "next": "6-2", "value": 6},
	      {"id": "6-2", "next": None, "value": 6}
	    ]
	  }
	}
]

idx=0
for case in tests:
    idx+=1
    print ("\n%s test %i *********" % ("*"*20 , idx))
    items={}
    for item in case["linkedList"]["nodes"]:
    	items[item["id"]] = LinkedList(item["value"])
    for item in case["linkedList"]["nodes"]:
    	if item["next"]:
    		items[item["id"]].next = items[item["next"]]

    head = items[ case["linkedList"]["head"] ]

    print("-- Original List ")
    print_list(head)
    print("-- No Dupe List ")

    print_list(removeDuplicatesFromLinkedList(head))

