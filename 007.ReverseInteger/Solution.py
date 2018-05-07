# -*- coding: utf-8 -*-
"""
Created on Mon May  7 15:09:19 2018

@author: zhuoj
"""

        
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = lambda x: x and (1, -1)[x < 0]
        r = int(str(sign(x)*x)[::-1])
        return (sign(x)*r, 0)[r > 2**31 - 1] 
        
print(Solution().reverse(123))
print(Solution().reverse(-123))
print(Solution().reverse(120))