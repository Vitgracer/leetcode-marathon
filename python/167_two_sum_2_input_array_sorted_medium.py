"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""

class Solution(object):
    def twoSum(self, numbers, target):
        l = 0
        r = len(numbers) - 1

        while True:
            cur_val = numbers[l] + numbers[r]

            if cur_val == target:
                return l+1, r+1
            elif cur_val > target:
                r -= 1
            else:
                l += 1