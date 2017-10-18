#
# [88] Merge Sorted Array
#
# https://leetcode.com/problems/merge-sorted-array
#
# algorithms
# Easy (32.10%)
# Total Accepted:    189.6K
# Total Submissions: 590.6K
# Testcase Example:  '[1]\n1\n[]\n0'
#
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
# one sorted array.
# 
# 
# Note:
# You may assume that nums1 has enough space (size that is greater or equal to
# m + n) to hold additional elements from nums2. The number of elements
# initialized in nums1 and nums2 are m and n respectively.
#
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        indexA = m-1
        indexB = n-1
        while indexA >= 0 and indexB >= 0:
            if nums1[indexA] >= nums2[indexB]:
                nums1[indexA + indexB +1] = nums1[indexA]
                indexA -= 1
            else:
                nums1[indexA + indexB +1] = nums2[indexB]
                indexB -= 1
        while indexB >=0:
            nums1[indexB] = nums2[indexB]
            indexB -=1

