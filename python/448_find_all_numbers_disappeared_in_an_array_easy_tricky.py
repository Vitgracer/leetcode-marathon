"""
https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
"""

# dummy solution
# class Solution(object):
#     def findDisappearedNumbers(self, nums):
#         return list(set(range(1, len(nums) + 1)) - set(nums))

# elegant solution with o(1) in memory
class Solution(object):
    def findDisappearedNumbers(self, nums):
        for num in nums:
            index = abs(num) - 1

            if nums[index] > 0:
                nums[index] *= -1

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]