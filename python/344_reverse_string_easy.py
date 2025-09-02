"""
https://leetcode.com/problems/reverse-string/description/
"""

class Solution(object):
    def reverseString(self, s):
        for i in range(len(s) // 2):
            s[i], s[-(1 + i)] = s[-(1 + i)], s[i]
        return s