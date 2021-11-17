# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def shiftLinkedList(head, k):
	idx = None
	length=0
	ptr=head
	while ptr:
		if not ptr.next:
			tail=ptr
		ptr=ptr.next
		length+=1
	#tail=ptr	
	print("Tail is %i" % tail.value)
	if k==length or k==0:
		print("k (%i is length %i) returning value")
		return head
	k=-2
	if k<0:
		#pivot = length - abs(k)%length+1
		pivot = abs(k)%length
	elif abs(k)>length:
		increment = abs(k)%length-1
		pivot=length-increment
	else:
		pivot = k
	print ("Len %i --- k %i"%(length,k))
	idx=0
	ptr=head
	print ("New pivot value %i " %pivot)

	pivotptr=None
	while ptr:
		print(idx)
		if idx==pivot-1:
			print("Found pivot %i" % ptr.value)
			newtail=ptr
		if idx==pivot:
			break
		ptr=ptr.next
		idx+=1
	newhead=ptr

	newtail.next=None
	if k>0:
		newtail.next=None
		ptr.next=head
	else:
		ptr.next=head
		tail.next=None
		

	return newhead

tests = [
{
  "k": 2,
  "linkedList": {
    "head": "0",
    "nodes": [
      {"id": "0", "next": "1", "value": 0},
      {"id": "1", "next": "2", "value": 1},
      {"id": "2", "next": "3", "value": 2},
      {"id": "3", "next": "4", "value": 3},
      {"id": "4", "next": "5", "value": 4},
      {"id": "5", "next": None, "value": 5}
    ]
  },

},
{
  "k": 5,
  "linkedList": {
    "head": "0",
    "nodes": [
      {"id": "0", "next": "1", "value": 0},
      {"id": "1", "next": "2", "value": 1},
      {"id": "2", "next": "3", "value": 2},
      {"id": "3", "next": "4", "value": 3},
      {"id": "4", "next": "5", "value": 4},
      {"id": "5", "next": None, "value": 5}
    ]
  }
}
]
def print_list(head):
	array = []
	ptr=head
	while ptr:
		array.append(str(ptr.value))
		ptr=ptr.next
	print ("[ %s ]" % " -> ".join(array))
idx=0
for case in tests:
	idx+=1
	print ("\n%s test %i *********" % ("*"*20 , idx))

	nodes={}
	for node in case["linkedList"]["nodes"]:
		nodes[node["id"]]=LinkedList(node["value"])
	for node in case["linkedList"]["nodes"]:
		if node["next"] in nodes:
			nodes[node["id"]].next = nodes[node["next"]]
	head=nodes[case["linkedList"]["head"]]
	print("k: %i     List:   " %case["k"]),
	print_list(head) 

	retval=shiftLinkedList(head,case["k"])
	print ("Return "),
	print_list(retval)