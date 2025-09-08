"""
https://leetcode.com/problems/happy-number/description/
"""

class Solution(object):
    def isHappy(self, n):
        new_n = n
        seen = set()
        
        while True:
            seen.add(new_n)
            new_n = sum([int(i)**2 for i in str(new_n)])
            if new_n == 1:
                return True
            if new_n in seen:
                return False
        