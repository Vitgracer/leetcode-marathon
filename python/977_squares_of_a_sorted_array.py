"""
https://leetcode.com/problems/squares-of-a-sorted-array/description/
"""

class Solution(object):
    def sortedSquares(self, nums):
        nums_new = []
        for i in nums:
            nums_new.append(i**2)
        return sorted(nums_new)
    
        