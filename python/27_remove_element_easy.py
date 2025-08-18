"""
https://leetcode.com/problems/remove-element/description/
"""

"""
The easiest solution: 
1. Sort first 
2. Find the val occurrences and the lenght 
3. Shift needed values from the right to these length 
(not implemented)

Proposed solution: 
1. Find all val indexes 
2. From the right side of the array go and write all non-val elements to the needed indexes
"""
class Solution(object):
    def removeElement(self, nums, val):
        val_indexes = []        

        for i, num in enumerate(nums):
            if num == val:
                val_indexes.append(i)

        number_of_val_occ = len(val_indexes)

        current_val_index = 0
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] != val and current_val_index < len(val_indexes):
                nums[val_indexes[current_val_index]] = nums[i]
                current_val_index += 1
            else:
                # if we already have this val i nthe right side, we don't need to make a replace.
                val_indexes = val_indexes[:-1]

        k = len(nums) - number_of_val_occ
        nums = nums[:-number_of_val_occ]
        return k