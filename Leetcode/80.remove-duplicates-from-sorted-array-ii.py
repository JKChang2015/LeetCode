#
# [80] Remove Duplicates from Sorted Array II
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii
#
# algorithms
# Medium (36.32%)
# Total Accepted:    130.4K
# Total Submissions: 359K
# Testcase Example:  '[]'
#
# 
# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
# 
# 
# For example,
# Given sorted array nums = [1,1,1,2,2,3],
# 
# 
# Your function should return length = 5, with the first five elements of nums
# being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new
# length.
# 
#
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
    
        index = 2
        for i in range (2,len(nums)):
            if nums[index-2] != nums[i]:
                nums[index] = nums[i]
                index += 1
        return index
            
#     def removeDuplicates(self, A):
#         if len(A) <= 2: return len(A)
#         prev = 1; curr = 2
#         while curr < len(A):
#             if A[curr] == A[prev] and  A[curr] == A[prev - 1]:
#                 curr += 1
#             else:
#                 prev += 1
#                 A[prev] = A[curr]
#                 curr += 1
#         return prev + 1
