"""
https://leetcode.com/problems/rotate-array/
"""

# not inplace, but graceful 
class Solution(object):
    def rotate(self, nums, k):
        real_rotation = k % len(nums)

        first_part = nums[:-real_rotation]
        second_part = nums[-real_rotation:]

        return second_part + first_part
    
# inplace 
class Solution(object):
    def rotate(self, nums, k):
        real_rotation = k % len(nums)

        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, real_rotation - 1)
        reverse(nums, real_rotation, len(nums) - 1)
