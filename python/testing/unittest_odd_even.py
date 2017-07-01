#!/usr/bin/env python

import unittest

def odd_or_even(num):
    if num%2==0:
        return 'even'
    else:
        return 'odd'


class TestOddEven(unittest.TestCase):
    def unittest_odd_or_even(self):
        self.assertEqual(odd_or_even(2),'even')


unittest.main()
    
