"""
https://leetcode.com/problems/group-anagrams/description/
"""

class Solution(object):
    def groupAnagrams(self, strs):
        d = {}

        for word in strs:
            d_hash = dict.fromkeys([chr(i) for i in range(ord('a'), ord('z') + 1)], 0)
            for symbol in word:
                d_hash[symbol] += 1
            
            str_hash = "".join([str(i) + str(d_hash[i]) for i in d_hash])
            
            if str_hash in d:
                d[str_hash].append(word)
            else:
                d[str_hash] = [word]
        return list(d.values())

        