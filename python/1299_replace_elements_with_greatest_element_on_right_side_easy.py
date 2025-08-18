"""
https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/description/
"""

class Solution(object):
    def replaceElements(self, arr):
        # find max elements from the right of array 
        max_right_array = [0] # 0 is a dummy value 
        for i in range(len(arr) - 1, -1, -1):
            # find the max element for the whole sublist right to the value 
            max_i = max(max_right_array[-1], arr[i])
            max_right_array.append(max_i)
        
        max_right_array = max_right_array[1:][::-1]
        for i in range(0, len(arr) - 1, 1):
            arr[i] = max_right_array[i + 1]

        arr[-1] = -1
        return arr