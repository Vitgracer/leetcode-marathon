"""
https://leetcode.com/problems/single-number/
"""

class Solution(object):
    def singleNumber(self, nums):
        d = {}

        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        
        for key in d:
            if d[key] == 1:
                return key
        