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


from AlgoHelper import debug,testing,linkedlist
tests = testing.load_tests("linkedListDupe")

debug.script_header("Remove Duplicates from linked List")
idx=0
for case in tests:
    idx+=1
    debug.test_header ("Test %i" % ( idx))
    items={}
    for item in case["linkedList"]["nodes"]:
    	items[item["id"]] = LinkedList(item["value"])
    for item in case["linkedList"]["nodes"]:
    	if item["next"]:
    		items[item["id"]].next = items[item["next"]]

    head = items[ case["linkedList"]["head"] ]

    vars={}
    vars["Original"]=linkedlist.get_list_str(head)
    vars["No Dupes"]=linkedlist.get_list_str(removeDuplicatesFromLinkedList(head))

    debug.print_variables(vars)