#
# [167] Two Sum II - Input array is sorted
#
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
#
# algorithms
# Easy (47.13%)
# Total Accepted:    103.2K
# Total Submissions: 218.8K
# Testcase Example:  '[2,3,4]\n6'
#
# Given an array of integers that is already sorted in ascending order, find
# two numbers such that they add up to a specific target number.
# 
# The function twoSum should return indices of the two numbers such that they
# add up to the target, where index1 must be less than index2. Please note that
# your returned answers (both index1 and index2) are not zero-based.
# 
# You may assume that each input would have exactly one solution and you may
# not use the same element twice.
# 
# 
# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2
# 
#
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(numbers) < 2:
            return 

        start = 0
        end = len(numbers) -1

        while start < end:
            sum = numbers[start] + numbers[end]  
            if sum > target:
                end -= 1
            elif sum < target:
                start += 1
            else:
                return [start + 1, end+1]
