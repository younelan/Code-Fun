#!/usr/local/bin/python3

#this list of words will be lowercase, all other words are capitalized
small_words = ('into', 'the', 'a', 'of', 'at', 'in', 'for', 'on')

def book_title(title):
    """ Takes a string and returns a title-case string.
    All words EXCEPT for small words are made title case
    unless the string starts with a preposition, in which
    case the word is correctly capitalized.

    >>> book_title('DIVE Into python')
    'Dive into Python'

    >>> book_title('the great gatsby')
    'The Great Gatsby'

    >>> book_title('the WORKS OF AleXANDer dumas')
    'The Works of Alexander Dumas'
    """
    
    #first get all words capitalized
    wordlist=title.title().split()

    #then iterate through all words
    for idx,val in enumerate(wordlist):
        #and when one is in the exceptions but not in the first position
        if val.lower() in small_words and idx>0:
            #make it lowercase
            wordlist[idx]=val.lower()
    #return the final string
    return ' '.join(wordlist)

def _test():
    """This function makes sure the tests defined
       in the docstring of refactory run"""
    import doctest, refactory
    return doctest.testmod(refactory)

if __name__ == "__main__":
    _test()
