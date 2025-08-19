"""
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
"""


class Solution(object):
    def findDisappearedNumbers(self, nums):
        return list(set(range(1, len(nums) + 1)) - set(nums))
        