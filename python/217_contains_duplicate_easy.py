"""
https://leetcode.com/problems/contains-duplicate/description/
"""

class Solution(object):
    def containsDuplicate(self, nums):
        d = set()
        for i in nums:
            if i not in d:
                d.add(i)
            else:
                return True
        return False
        
        