"""
https://leetcode.com/problems/valid-mountain-array/
"""

class Solution(object):
    def validMountainArray(self, arr):
        if len(arr) < 3:
            return False 
        
        max_index = arr.index(max(arr))
        if max_index == 0 or max_index == len(arr) - 1:
            return False 
        
        # left run
        anchor = arr[max_index]
        for i in range(max_index - 1, -1, -1):
            if arr[i] >= anchor:
                return False
            anchor = arr[i]
        
        # right run
        anchor = arr[max_index]
        for i in range(max_index + 1, len(arr), 1):
            if arr[i] >= anchor:
                return False
            anchor = arr[i]
        
        return True 
