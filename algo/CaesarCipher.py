def caesarCipherEncryptor(string, key):
    if key>25:
        key=key%26
        print("Key greater than 26, wrapping to %i" % key )
    retval=""
    for ch in string:
        newval = ord("a")+(ord(ch)-ord("a")+key)%26
        retval += chr(newval)
        # if newval>ord("z"):
        #     newval=ord("a")+newval-ord("z")
        # retval += chr(newval)
    return retval

tests = [

    {
      "expect":"def",
      "key": 3,
      "string": "abc"

    },
    {
        "expect":"abc",
      "key": 26,
      "string": "abc"
    },
    {
      "expect":"abc",
      "key": 52,
      "string": "abc"

    },
    {
      "key": 5,
     "string": "xyz",
     "expect":"cde"
    },
    {
        "expect":"wxy",
          "key": 25,
         "string": "xyz"

    }
]
idx=0
for case in tests:
    idx+=1
    print ("\n%s test %i *********" % ("*"*20 , idx))
    print("-- String ")
    print(case["string"],"key",case["key"])
    print("-- Output ")
    val=caesarCipherEncryptor(case["string"],case["key"])
    print(val)
    print("-- Expected ")
    print(case["expect"])
