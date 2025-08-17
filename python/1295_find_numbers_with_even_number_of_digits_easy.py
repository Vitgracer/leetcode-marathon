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




solution = Solution()
test_1 = [12,345,2,6,7896]
test_2 = [555,901,482,1771]
test_3 = [0]
test_4 = [0, 1, 2, 3]
test_5 = [11, 12, 13, 14]
print(solution.findNumbers(test_1))
print(solution.findNumbers(test_2))
print(solution.findNumbers(test_3))
print(solution.findNumbers(test_4))
print(solution.findNumbers(test_5))
