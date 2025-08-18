"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""

class Solution(object):
    def removeDuplicates(self, nums):
        current_unique = nums[0]
        index_to_replace = 1

        for _, num in enumerate(nums, start = 1):
            if num == current_unique: 
                continue 
            else:
                current_unique = num 
                nums[index_to_replace] = num
                index_to_replace += 1
        return index_to_replace