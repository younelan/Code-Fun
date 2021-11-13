def getNthFib(n):
    arr = [0,1]
    if n==0: return 0
    if n == 1: return 0
    for i in range(n-2):
        nextel = arr[-1]+arr[-2]
        arr.append(nextel)
        
    return arr[-1]


tests = [

    {
      "n": 6,
      "expect":5,
    },
    {
      "n": 0,
      "expect":0,
    },
    {
      "n": 7,
      "expect":8,
    },
    {
      "n": 8,
      "expect":13,
    },
    {
      "n": 10,
      "expect":34,
    },
    {
      "n": 11,
      "expect":55,
    },
]
idx=0
for case in tests:
    idx+=1
    val=getNthFib(case["n"])
    print("Test: %3i     n : %3i   expect: %3i   output: %3i" % (idx, case["n"],case["expect"],val) )
