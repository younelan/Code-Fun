#!/usr/bin/env python

dialpad={
1:"1",
2:"2ABC",
3:"3DEF",
4:"4GHI",
5:"5JKL",
6:"6MNO",
7:"7PQRS",
8:"8TUV",
9:"9WXYZ"
}


def phoneNumberMnemonics(phoneNumber):
    lists = []
    for digit in phoneNumber:
        lists.append(dialpad[phoneNumber])
    print(lists)
    return lists


