"""
https://leetcode.com/problems/max-consecutive-ones/
"""
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        current_consecutive = 0
        max_consecutive = 0

        for num in nums: 
            if num == 1:
                current_consecutive += 1
            else: 
                current_consecutive = 0
            max_consecutive = max(max_consecutive, current_consecutive)
        return max_consecutive