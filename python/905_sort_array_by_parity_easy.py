"""
https://leetcode.com/problems/sort-array-by-parity/description/
"""

# literally the same as move zeros (283)
class Solution(object):
    def sortArrayByParity(self, nums):
        odd_index = -1
        for i, num in enumerate(nums):
            if num % 2 == 0:
                if odd_index == -1:
                    continue
                else:
                    temp = nums[odd_index]
                    nums[odd_index] = nums[i]
                    nums[i] = temp
                    odd_index += 1
            else:
                if odd_index == -1:
                    odd_index = i
                else:
                    continue
        return nums
