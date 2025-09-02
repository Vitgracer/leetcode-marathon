"""
https://leetcode.com/problems/minimum-size-subarray-sum/description/
"""

class Solution(object):
    def minSubArrayLen(self, target, nums):
        l = 0
        r = 0
        min_len = 0
        sum = nums[0]

        while l!= len(nums) - 1:
            if sum < target and r < len(nums) - 1:
                r += 1
                sum += nums[r]
            if sum >= target:
                min_len = r - l + 1
                sum -= nums[l]
                l += 1
            if r == len(nums) - 1 and sum < target:
                return min_len
        return min_len

sol = Solution()
sol.minSubArrayLen(5, [5])
        