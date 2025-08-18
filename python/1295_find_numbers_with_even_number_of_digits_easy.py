"""
https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
"""

class Solution(object):
    def findNumbers(self, nums):
        even_num_number = 0

        for num in nums: 
            str_num = str(num)
            digits_num = len(str_num)

            if digits_num % 2 == 0: 
                even_num_number += 1

        return even_num_number
