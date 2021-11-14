
def dafirstDuplicateValue(array):
	# Write your code here.
	doubles={}
	sort_array=sorted(array)
	prev_el=sort_array[0]
	idx=0
	for el in sort_array[1:]:
		if prev_el==el:
			print("Found duplicate %s" % el)
			doubles[idx]=el
		prev_el=el
		idx+=1
	print("Doubles::" , doubles)

	for el in array:
		print("el",el,"doubles",doubles[0])
		if el in doubles:
			return el
	return -1

def firstDuplicateValue(array):
	# Write your code here.
	counts = {el:0 for el in array}
	for el in array:
		counts[el]+=1
		if counts[el]>1:
			return el
	return -1



tests = [
{
  "array": [2, 1, 5, 2, 3, 3, 4],
  "expect": 2
},
{
  "array": [2, 1, 5, 3, 3, 2, 4],
	"expect":3

},
{
	"array": [3, 1, 3, 1, 1, 4, 4],
	"expect":1
}


]



testid=0
idx=0
for case in tests:
	idx+=1
	retval = firstDuplicateValue(case["array"])
	print ("Test %i:          Output %i   (Expected: %i) Input:" % (idx,retval,case["expect"])),
	print(case["array"])
