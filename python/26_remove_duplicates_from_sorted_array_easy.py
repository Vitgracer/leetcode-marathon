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

sol = Solution()
test_1 = [0,0,1,1,1,2,2,3,3,4]
test_2 = [1,1,2]
test_3 = [1,1,1]
sol.removeDuplicates(test_1)
sol.removeDuplicates(test_2)
sol.removeDuplicates(test_3)