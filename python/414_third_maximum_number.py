"""
https://leetcode.com/problems/third-maximum-number/description/
"""

class Solution(object):
    def thirdMax(self, nums):
        max_el_list = [nums[0]]

        for _, num in enumerate(nums[1:]):
            # we need distinct elements 
            if num in max_el_list:
                continue

            inserted = False 
            for i in range(len(max_el_list) - 1, -1, -1):
                max_el = max_el_list[i]

                if num > max_el:
                    max_el_list.insert(i+1, num)
                    inserted = True
                    if len(max_el_list) > 3:
                        max_el_list.pop(0)
                    break

            # if length of the list != 3
            if len(max_el_list) < 3 and not inserted:
                max_el_list.insert(0, num)
        
        if len(max_el_list) == 3:
            return max_el_list[0]
        else:
            return max_el_list[-1]