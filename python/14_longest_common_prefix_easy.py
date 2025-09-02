"""
https://leetcode.com/problems/longest-common-prefix/
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        common_prefix = ""
        lengths = [len(s) for s in strs]

        for len_counter in range(min(lengths)):
            equal = True
            for word_counter in range(len(strs) - 1):
                if strs[word_counter][len_counter] != strs[word_counter + 1][len_counter]:
                    equal = False
                    break
            if equal:
                common_prefix += strs[0][len_counter]
            else:
                break
        return common_prefix

sol = Solution()
sol.longestCommonPrefix(["cir","car"])