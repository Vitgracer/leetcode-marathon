"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = 0
        seen = {}
        max_len = 0

        for r, char in enumerate(s):
            if char in seen and seen[char] >= l:
                l = seen[char] + 1
            
            seen[char] = r
            max_len = max(max_len, r - l + 1)
                
        return max_len


sol = Solution()
sol.lengthOfLongestSubstring(["abcdecprfk"])
        