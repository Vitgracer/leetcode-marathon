"""
https://leetcode.com/problems/jewels-and-stones/description/
"""

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        d = {}
        for stone in stones:
            if stone in d:
                d[stone] += 1
            else:
                d[stone] = 1
        
        return sum([d[i] for i in jewels if i in d])
        