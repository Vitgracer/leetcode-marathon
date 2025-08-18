"""
https://leetcode.com/problems/check-if-n-and-its-double-exist/
"""

# resolved with a hint 
class Solution(object):
    def checkIfExist(self, arr):
        seen = set()
        for num in arr:
            if num in seen:
                return True
            seen.add(num * 2)
            if num % 2 == 0: 
                seen.add(num // 2)
        return False 