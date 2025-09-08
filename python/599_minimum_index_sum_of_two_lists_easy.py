"""
https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/
"""

class Solution(object):
    def findRestaurant(self, list1, list2):
        d1 = {}
        for i1, val1 in enumerate(list1):
            d1[val1] = [i1]
        
        min_val = float('inf')
        for i2, val2 in enumerate(list2):
            if val2 in d1:
                d1[val2].append(i2)
                if sum(d1[val2]) < min_val:
                    min_val = sum(d1[val2])
        answer = []
        for key in d1:
            if sum(d1[key]) == min_val and len(d1[key]) == 2:
                answer.append(key)
        return answer