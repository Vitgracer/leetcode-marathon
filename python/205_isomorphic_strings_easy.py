"""
https://leetcode.com/problems/isomorphic-strings/description/
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False
        
        d_s = {}
        d_v = {}

        for s_val, t_val in zip(s, t):
            if t_val not in d_v:
                d_v[t_val] = s_val
            else:
                if d_v[t_val] != s_val:
                    return False
            
            if s_val not in d_s:
                d_s[s_val] = t_val
            else:
                if d_s[s_val] != t_val:
                    return False
        return True
            
sol = Solution()
sol.isIsomorphic("badc", "baba")