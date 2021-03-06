# -*- coding: utf-8 -*-
"""
Created on Fri May  4 13:02:16 2018

@author: zhuoj
"""


#Python solution using hash
class Solution:
    # @return a tuple, (index1, index2)
    # 8:42
    def twoSum(self, num, target):
        map = {}
        for i in range(len(num)):
            if num[i] not in map:
                map[target - num[i]] = i 
            else:
                return map[num[i]], i 

        return -1, -1
        
        