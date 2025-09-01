"""
https://leetcode.com/problems/pascals-triangle-ii/
"""

class Solution(object):
    def getRow(self, rowIndex):
        def generate_triangle(triangle):
            new_triangle = [1]
            for i in range(len(triangle) - 1):
                new_triangle.append(triangle[i] + triangle[i+1])
            return new_triangle + [1]

        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1] 
        
        last_triangle = [1, 1]

        for _ in range(2, rowIndex + 1):
            last_triangle = generate_triangle(last_triangle)
        return last_triangle
        