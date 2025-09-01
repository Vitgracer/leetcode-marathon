"""
https://leetcode.com/problems/reverse-words-in-a-string/description/
"""

# not optimal easiest solution 
class Solution(object):
    def reverseWords(self, s):
        s = s.strip()
        
        elements = [i.strip() for i in s.split(" ") if i != ""]
        new_s = ""

        for i in range(len(elements) - 1, -1 ,-1):
            elem = elements[i]
            new_s += elem + " "
        
        return new_s[:-1]

# o(N) time, o(N) memory
class Solution(object):
    def reverseWords(self, s):
        elements = s.split()
        new_s = " ".join(elements[::-1])
        
        return new_s
