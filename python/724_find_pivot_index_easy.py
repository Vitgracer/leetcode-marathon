"""
https://leetcode.com/problems/find-pivot-index/description/
"""

class Solution(object):
    def pivotIndex(self, nums):
        lSum = 0
        rSum = sum(nums)

        for i in range(len(nums)):
            if i-1 >=0:
                lSum += nums[i-1]
            
            rSum -= nums[i]

            if lSum == rSum:
                return i
        
        return -1