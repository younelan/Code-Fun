#!/usr/local/bin/python3
#  input counter, it will count the occurences of words in a string
#        input_counter.py
#
#  by: Youness El Andaloussi
#       22 Nov 2014
#
#  Lesson 6, Quiz 1, Attempt 2
#

word_set=set()
word_dict={}

while True:
    in_str=input('Enter text: ')
    if in_str=='':
        break

    for cur_word in in_str.split():
        old_length=len(word_set)
        word_set.add(cur_word)
        new_length=len(word_set)

        if new_length>old_length:
            word_dict[cur_word]=new_length

    for cur_word,idx in word_dict.items():
        print (cur_word,idx)
