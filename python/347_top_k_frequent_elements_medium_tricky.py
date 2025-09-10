"""
https://leetcode.com/problems/top-k-frequent-elements/description/
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        d = {}
        for val in nums:
            if val in d:
                d[val] += 1
            else:
                d[val] = 1
        
        sorted_dict = dict(sorted(d.items(), key = lambda i : i[1]))
        return list(sorted_dict.keys())[-k:]

sol = Solution()
sol.topKFrequent([1,2,1,2,1,2,3,1,3,2], k = 2)