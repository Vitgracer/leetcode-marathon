"""
https://leetcode.com/problems/move-zeroes/description/
"""

class Solution(object):
    def moveZeroes(self, nums):
        zero_index = -1

        for i, num in enumerate(nums):
            # skip first non zero values 
            if zero_index == -1 and num != 0:
                continue
            
            # find first zero value
            if num == 0 and zero_index == -1:
                zero_index = i
                continue
            
            # wait for non-zero value
            if num == 0:
                continue
            
            nums[zero_index] = num
            nums[i] = 0
            zero_index += 1
        
        return nums
            

