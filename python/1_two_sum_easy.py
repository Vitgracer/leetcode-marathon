"""
https://leetcode.com/problems/two-sum/description/
"""
class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i, val in enumerate(nums):
            if val in d:
                return d[val], i
            else:
                d[target - val] = i