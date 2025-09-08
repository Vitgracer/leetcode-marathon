"""
https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
"""

class Solution(object):
    def intersect(self, nums1, nums2):
        d = {}
        for val in nums1:
            if val in d:
                d[val] += 1
            else:
                d[val] = 1

        result = []
        for val in nums2:
            if val in d:
                result.append(val)
                d[val] -= 1
                if d[val] == 0:
                    del d[val]
        return result
        