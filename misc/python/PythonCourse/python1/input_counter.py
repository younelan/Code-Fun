#!/usr/local/bin/python3

wordlist={}

while True:
    inStr=input('Enter text: ')
    if inStr=='':
        break

    for curWord in inStr.split():
        if curWord not in wordlist:
            wordlist[curWord]=len(wordlist)+1

    for curWord,idx in wordlist.items():
        print (curWord,idx)
