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


from AlgoHelper import console,testing,linkedlist
tests = testing.load_tests("linkedListDupe")

console.script_header("Remove Duplicates from linked List")
idx=0
for case in tests:
    idx+=1
    #console.test_header ("Test %i" % ( idx))
    head,nodes=linkedlist.load_list(case["linkedList"]["nodes"],case["linkedList"]["head"])
   
    vars={"Test":idx}
    vars["Original"]=linkedlist.get_list_str(head)
    vars["No Dupes"]=linkedlist.get_list_str(removeDuplicatesFromLinkedList(head))

    console.print_variables(vars)


