"""
https://leetcode.com/problems/max-consecutive-ones/
"""
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        current_consecutive = 0
        max_consecutive = 0

        for num in nums: 
            if num == 1:
                current_consecutive += 1
            else: 
                current_consecutive = 0
            max_consecutive = max(max_consecutive, current_consecutive)
        return max_consecutive

# testing
solution = Solution()
test_1 = [1,1,0,1,1,1]
test_2 = [1,0,1,1,0,1]
test_3 = [0,0,0]
test_4 = [1]
print(solution.findMaxConsecutiveOnes(test_1))
print(solution.findMaxConsecutiveOnes(test_2))
print(solution.findMaxConsecutiveOnes(test_3))
print(solution.findMaxConsecutiveOnes(test_4))
