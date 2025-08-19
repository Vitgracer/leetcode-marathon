"""
https://leetcode.com/problems/height-checker/description/
"""

# probably it's better to do with counting sort 
class Solution(object):
    def heightChecker(self, heights):
        heights_sorted = sorted(heights)
        indices = [i for i in range(len(heights)) if heights[i] != heights_sorted[i]]
        return len(indices)