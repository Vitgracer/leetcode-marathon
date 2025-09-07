"""
https://leetcode.com/problems/first-unique-character-in-a-string/description/
"""

class Solution(object):
    def firstUniqChar(self, s):
        d = {}

        for val in s:
            if val not in d:
                d[val] = 1
            else:
                d[val] += 1
        
        for i, val in enumerate(s):
            if d[val] == 1:
                return i
        return -1