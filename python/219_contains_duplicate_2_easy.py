"""
https://leetcode.com/problems/contains-duplicate-ii/description/
"""

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        d = {}
        for i, val in enumerate(nums):
            if val in d:
                if abs(i - d[val]) <= k:
                    return True
            d[val] = i
        return False

sol = Solution()
sol.containsNearbyDuplicate([1,2,3,1], 3)