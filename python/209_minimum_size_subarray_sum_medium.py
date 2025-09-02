"""
https://leetcode.com/problems/minimum-size-subarray-sum/description/
"""

class Solution(object):
    def minSubArrayLen(self, target, nums):
        l = 0
        r = 0
        min_len = float("inf") 
        sum = nums[0]

        while True:
            if sum >= target:
                min_len = min(min_len, r - l + 1)
                sum -= nums[l]
                l += 1
            elif r < len(nums) - 1:
                r += 1
                sum += nums[r]
            else:
                break
        return 0 if min_len == float("inf") else min_len

sol = Solution()
sol.minSubArrayLen(5, [5])
        