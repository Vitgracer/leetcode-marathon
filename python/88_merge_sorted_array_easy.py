"""
https://leetcode.com/problems/merge-sorted-array/
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        m_cur = m - 1
        n_cur = n - 1

        for i in range(len(nums1) - 1, -1, -1):
            if m_cur == -1:
                nums1[i] = nums2[n_cur]
                n_cur -=1
                continue

            if n_cur == -1:
                nums1[i] = nums1[m_cur]
                m_cur -=1
                continue
            
            if nums1[m_cur] > nums2[n_cur]:
                nums1[i] = nums1[m_cur]
                m_cur -= 1
            else:
                nums1[i] = nums2[n_cur]
                n_cur -= 1        
        
        return