"""
https://leetcode.com/problems/largest-number-at-least-twice-of-others/description/
"""

# simpliest solution: sort and compare max and before-max element. o(n*log(n))
class Solution(object):
    def dominantIndex(self, nums):
        max_el, max_ind = 0, -1
        sec_max_el = 0

        for i, el in enumerate(nums):
            if el >= max_el:
                prev_max = max_el
                max_el = el
                max_ind = i
                sec_max_el = prev_max
            else:
                if el > sec_max_el:
                    sec_max_el = el
        
        if sec_max_el == 0:
            sec_max_el = 1e-8
        
        if max_el / sec_max_el >= 2:
            return max_ind
        else:
            return -1