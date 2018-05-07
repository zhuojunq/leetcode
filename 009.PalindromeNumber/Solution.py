# -*- coding: utf-8 -*-
"""
Created on Mon May  7 16:24:47 2018

@author: zhuoj
"""

class Solution(object):
    def isPalindrome(self, x):
        return x >= 0 and x == int(str(x)[::-1])