"""
https://leetcode.com/problems/duplicate-zeros/
"""

class Solution(object):
    # works o(n^2) in worst case 
    def duplicateZeros(self, arr):
        i = 0
        while i < len(arr) - 1:
            if arr[i] == 0: 
                left_part = arr[i+1:]
                arr[i+1] = 0
                arr[i+2:] = left_part[:-1]
                i+=1
            i+=1
        return

solution = Solution()
test_1 = [1,0,2,3,0,4,5,0]
test_2 = [1,2,3]
test_3 = [0, 1]
test_4 = [1, 0, 0, 2]
test_5 = [0 ,0, 0, 0]
test_6 = [0]
test_7 = [1, 0]
test_8 = [0,0,0,3,4,5]
print(solution.duplicateZeros(test_1))
print(solution.duplicateZeros(test_2))
print(solution.duplicateZeros(test_3))
print(solution.duplicateZeros(test_4))
print(solution.duplicateZeros(test_5))
print(solution.duplicateZeros(test_6))
print(solution.duplicateZeros(test_7))
print(solution.duplicateZeros(test_8))