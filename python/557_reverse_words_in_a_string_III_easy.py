"""
https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
"""

class Solution(object):
    def reverseWords(self, s):
        elems = s.split()
        s = " ".join([i[::-1] for i in elems])
        return s