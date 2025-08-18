"""
https://leetcode.com/problems/duplicate-zeros/
"""

class Solution(object):
    # works o(n^2) in worst case 
    def duplicateZeros(self, arr):
        i = 0
        while i < len(arr) - 1:
            if arr[i] == 0: 
                left_part = arr[i+1:]
                arr[i+1] = 0
                arr[i+2:] = left_part[:-1]
                i+=1
            i+=1
        return