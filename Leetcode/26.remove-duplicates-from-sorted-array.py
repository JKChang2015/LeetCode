#
# [26] Remove Duplicates from Sorted Array
#
# https://leetcode.com/problems/remove-duplicates-from-sorted-array
#
# algorithms
# Easy (35.39%)
# Total Accepted:    272.2K
# Total Submissions: 769K
# Testcase Example:  '[]'
#
# 
# Given a sorted array, remove the duplicates in place such that each element
# appear only once and return the new length.
# 
# 
# Do not allocate extra space for another array, you must do this in place with
# constant memory.
# 
# 
# 
# For example,
# Given input array nums = [1,1,2],
# 
# 
# Your function should return length = 2, with the first two elements of nums
# being 1 and 2 respectively. It doesn't matter what you leave beyond the new
# length.
# 
#
class Solution(object):
    def removeDuplicates(self, nums):

        if len(nums) < 2:
            return len(nums)

        pre = 0
        for cur in range(1, len(nums)):
            if nums[cur] != nums[pre]:
                pre += 1
                nums[pre] = nums[cur]

        return pre + 1
